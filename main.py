from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import json, os, uuid, datetime

app = FastAPI(title="Landing Page Pattern API", version="1.0",
  description="First-principles landing page pattern library backed by empirical evidence")

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

# Load patterns
def load_patterns():
    with open(os.path.join(DATA_DIR, 'patterns.json')) as f:
        return json.load(f)

def save_patterns(patterns):
    with open(os.path.join(DATA_DIR, 'patterns.json'), 'w') as f:
        json.dump(patterns, f, indent=2)

# ===========================
# Models
# ===========================
class GenerateRequest(BaseModel):
    pattern_id: str
    substitutions: Dict[str, str]
    template: Optional[str] = None

class ArchivePatternRequest(BaseModel):
    name: str
    description: str
    elements: List[Dict[str, Any]]
    html_snippet: str
    tags: List[str]
    source_url: Optional[str] = None

# ===========================
# API Endpoints
# ===========================

@app.get("/")
def root():
    return {
        "name": "Landing Page Pattern API",
        "version": "1.0",
        "patterns_endpoint": "/patterns",
        "explorer": "/explorer",
        "docs": "/docs"
    }

@app.get("/patterns")
def list_patterns(search: Optional[str] = Query(None)):
    patterns = load_patterns()
    if search:
        search_lower = search.lower()
        results = []
        for p in patterns:
            if (search_lower in p['name'].lower() or 
                search_lower in p.get('description','').lower() or
                any(search_lower in t.lower() for t in p.get('tags',[]))):
                results.append({
                    'pattern_id': p['pattern_id'],
                    'name': p['name'],
                    'description': p['description'][:120] + '...',
                    'tags': p.get('tags', []),
                    'element_count': len(p.get('elements', [])),
                    'evidence_count': sum(len(e.get('evidence',[])) for e in p.get('elements',[]))
                })
        return {"count": len(results), "patterns": results}
    return {
        "count": len(patterns),
        "patterns": [{
            'pattern_id': p['pattern_id'],
            'name': p['name'],
            'description': p['description'][:120] + '...',
            'tags': p.get('tags', []),
            'element_count': len(p.get('elements', [])),
            'evidence_count': sum(len(e.get('evidence',[])) for e in p.get('elements',[]))
        } for p in patterns]
    }

@app.get("/patterns/{pattern_id}")
def get_pattern(pattern_id: str):
    patterns = load_patterns()
    for p in patterns:
        if p['pattern_id'] == pattern_id:
            return p
    raise HTTPException(404, f"Pattern '{pattern_id}' not found")

@app.get("/patterns/{pattern_id}/template")
def get_template(pattern_id: str):
    patterns = load_patterns()
    found = None
    for p in patterns:
        if p['pattern_id'] == pattern_id:
            found = p
            break
    if not found:
        raise HTTPException(404, f"Pattern '{pattern_id}' not found")
    
    template_path = os.path.join(TEMPLATE_DIR, f'{pattern_id}.html')
    if not os.path.exists(template_path):
        raise HTTPException(404, f"No template found for '{pattern_id}'")
    
    with open(template_path) as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/patterns/{pattern_id}/evidence")
def get_pattern_evidence(pattern_id: str):
    patterns = load_patterns()
    for p in patterns:
        if p['pattern_id'] == pattern_id:
            all_evidence = []
            for el in p.get('elements', []):
                for ev in el.get('evidence', []):
                    all_evidence.append({
                        'element': el['name'],
                        'element_id': el['element_id'],
                        **ev
                    })
            return {
                'pattern_id': p['pattern_id'],
                'name': p['name'],
                'total_citations': len(all_evidence),
                'evidence': all_evidence
            }
    raise HTTPException(404, f"Pattern '{pattern_id}' not found")

@app.post("/generate")
def generate_section(req: GenerateRequest):
    patterns = load_patterns()
    found = None
    for p in patterns:
        if p['pattern_id'] == req.pattern_id:
            found = p
            break
    if not found:
        raise HTTPException(404, f"Pattern '{pattern_id}' not found")
    
    template_path = os.path.join(TEMPLATE_DIR, f'{req.pattern_id}.html')
    if not os.path.exists(template_path):
        raise HTTPException(404, f"No template for '{req.pattern_id}'")
    
    with open(template_path) as f:
        html = f.read()
    
    # Apply substitutions
    for key, value in req.substitutions.items():
        placeholder = f'[{key}]'
        html = html.replace(placeholder, value)
    
    return {
        "pattern": req.pattern_id,
        "generated": True,
        "html": html
    }

@app.post("/build")
def build_full_page(patterns_req: List[GenerateRequest]):
    """Build a full landing page from multiple pattern sections"""
    full_html_parts = []
    for pr in patterns_req:
        result = generate_section(pr)
        full_html_parts.append(result['html'])
    
    combined = '\n\n'.join(full_html_parts)
    return {
        "sections": len(patterns_req),
        "html": combined
    }

@app.get("/elements")
def list_elements(pattern_id: Optional[str] = Query(None)):
    patterns = load_patterns()
    elements = {}
    for p in patterns:
        if pattern_id and p['pattern_id'] != pattern_id:
            continue
        for el in p.get('elements', []):
            elements[el['element_id']] = {
                'name': el['name'],
                'type': el.get('type'),
                'first_principle_label': el.get('first_principle_label'),
                'specs': el.get('specs', {}),
                'variants': el.get('variants', []),
                'evidence_count': len(el.get('evidence', [])),
                'pattern_id': p['pattern_id'],
                'pattern_name': p['name']
            }
    return {"count": len(elements), "elements": elements}

@app.get("/search")
def search(query: str = Query(...)):
    """Search across patterns, elements, and evidence"""
    patterns = load_patterns()
    q = query.lower()
    results = []
    seen_ids = set()
    
    for p in patterns:
        score = 0
        matches = []
        
        # Pattern name match
        if q in p['name'].lower():
            score += 10
            matches.append(f"Pattern name: {p['name']}")
        
        # Pattern description match
        if q in p.get('description','').lower():
            score += 5
            matches.append(f"Description match")
        
        # Element matches
        for el in p.get('elements', []):
            if q in el['name'].lower():
                score += 3
                matches.append(f"Element: {el['name']}")
            if q in el.get('first_principle_label','').lower():
                score += 3
                matches.append(f"FP: {el['first_principle_label'][:60]}")
            
            # Evidence matches
            for ev in el.get('evidence', []):
                if q in ev.get('study','').lower() or q in ev.get('finding','').lower():
                    score += 2
                    matches.append(f"Study: {ev.get('study','')[:60]}")
        
        if score > 0:
            results.append({
                'pattern_id': p['pattern_id'],
                'name': p['name'],
                'relevance': score,
                'matches': matches
            })
    
    results.sort(key=lambda x: -x['relevance'])
    return {"count": len(results), "query": query, "results": results}

# ===========================
# Explorer (Web UI)
# ===========================
@app.get("/explorer", response_class=HTMLResponse)
def explorer():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page Pattern Explorer</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Inter', sans-serif; background: #0f172a; color: #e2e8f0; }
        .header { padding: 2rem; border-bottom: 1px solid #1e293b; }
        .header h1 { font-size: 2rem; color: #f8fafc; font-weight: 800; }
        .header p { color: #94a3b8; margin-top: 0.5rem; }
        .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
        .pattern-list { display: grid; gap: 1.5rem; }
        .pattern-card {
            background: #1e293b; border-radius: 16px; padding: 2rem;
            border: 1px solid #334155; cursor: pointer;
            transition: all 0.2s;
        }
        .pattern-card:hover { border-color: #3b82f6; transform: translateY(-2px); }
        .pattern-card h2 { font-size: 1.4rem; color: #f8fafc; }
        .pattern-card .tags { display: flex; gap: 0.5rem; flex-wrap: wrap; margin: 0.75rem 0; }
        .pattern-card .tag {
            background: #334155; padding: 4px 12px; border-radius: 20px;
            font-size: 0.75rem; color: #94a3b8;
        }
        .pattern-card .meta { display: flex; gap: 2rem; color: #64748b; font-size: 0.85rem; }
        .pattern-card .desc { color: #94a3b8; margin-top: 0.75rem; font-size: 0.9rem; line-height: 1.5; }
        
        .detail-panel {
            background: #1e293b; border-radius: 16px; padding: 2rem;
            border: 1px solid #334155; margin-top: 2rem;
        }
        .detail-panel h2 { font-size: 1.8rem; color: #f8fafc; margin-bottom: 0.5rem; }
        .detail-panel .desc { color: #94a3b8; margin-bottom: 2rem; }
        
        .element { 
            background: #0f172a; border-radius: 12px; padding: 1.5rem;
            margin-bottom: 1rem; border-left: 3px solid #3b82f6;
        }
        .element h3 { color: #f8fafc; font-size: 1.1rem; }
        .element .fpl { color: #3b82f6; font-size: 0.85rem; margin-top: 0.25rem; font-weight: 600; }
        .element .specs { color: #94a3b8; font-size: 0.85rem; margin-top: 0.5rem; line-height: 1.6; }
        .element .variants { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.75rem; }
        .element .variant {
            background: #1e293b; padding: 6px 14px; border-radius: 8px;
            font-size: 0.8rem; color: #cbd5e1; border: 1px solid #334155;
        }
        
        .evidence { margin-top: 0.75rem; padding: 0.75rem; background: #1a2332; border-radius: 8px; }
        .evidence .study { color: #f59e0b; font-weight: 600; font-size: 0.85rem; }
        .evidence .finding { color: #94a3b8; font-size: 0.85rem; margin-top: 0.25rem; }
        .evidence .lift { color: #10b981; font-size: 0.85rem; font-weight: 600; margin-top: 0.25rem; }
        
        .template-preview {
            background: #0f172a; border-radius: 12px; padding: 2rem;
            margin-top: 1.5rem; border: 1px solid #334155;
        }
        .template-preview pre {
            overflow-x: auto; color: #e2e8f0; font-size: 0.8rem;
            max-height: 400px; overflow-y: auto;
        }
        .tab-bar { display: flex; gap: 1rem; margin-bottom: 1.5rem; }
        .tab {
            padding: 0.5rem 1.5rem; border-radius: 8px; cursor: pointer;
            background: #334155; color: #94a3b8; font-size: 0.85rem; font-weight: 600;
        }
        .tab.active { background: #3b82f6; color: #fff; }
        
        .search-bar {
            width: 100%; padding: 1rem 1.5rem; border-radius: 12px;
            background: #1e293b; border: 1px solid #334155;
            color: #e2e8f0; font-size: 1rem; margin-bottom: 1.5rem;
            font-family: 'Inter', sans-serif;
        }
        .search-bar:focus { outline: none; border-color: #3b82f6; }
        .back-btn {
            display: inline-block; margin-bottom: 1rem; 
            color: #3b82f6; cursor: pointer; font-size: 0.9rem;
            background: none; border: none; font-family: 'Inter', sans-serif;
        }
        .back-btn:hover { color: #60a5fa; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🏗️ Landing Page Pattern Explorer</h1>
        <p>First-principles pattern library backed by empirical evidence</p>
    </div>
    <div class="container" id="app">
        <input class="search-bar" id="search" placeholder="Search patterns, elements, or studies..." oninput="searchPatterns(this.value)">
        <div id="pattern-list" class="pattern-list"></div>
        <div id="detail-panel" style="display:none;"></div>
    </div>
    <script>
        let patterns = [];
        let currentPattern = null;
        
        fetch('/patterns')
            .then(r => r.json())
            .then(d => { patterns = d.patterns; renderList(d.patterns); });
        
        function renderList(list) {
            const container = document.getElementById('pattern-list');
            container.innerHTML = list.map(p => `
                <div class="pattern-card" onclick="showPattern('${p.pattern_id}')">
                    <h2>${p.name}</h2>
                    <div class="tags">${p.tags.map(t => '<span class="tag">' + t + '</span>').join('')}</div>
                    <div class="meta">
                        <span>${p.element_count} elements</span>
                        <span>${p.evidence_count} citations</span>
                    </div>
                    <div class="desc">${p.description}</div>
                </div>
            `).join('');
            document.getElementById('detail-panel').style.display = 'none';
        }
        
        async function showPattern(id) {
            const r = await fetch('/patterns/' + id);
            const p = await r.json();
            currentPattern = p;
            
            const panel = document.getElementById('detail-panel');
            panel.style.display = 'block';
            panel.innerHTML = `
                <button class="back-btn" onclick="renderList(patterns)">← Back to patterns</button>
                <h2>${p.name}</h2>
                <p class="desc">${p.description}</p>
                
                <div class="tab-bar">
                    <div class="tab active" onclick="showElements()">Elements + Evidence</div>
                    <div class="tab" onclick="showTemplate()">HTML Template</div>
                    <div class="tab" onclick="showWhoUses()">Who Uses This</div>
                </div>
                <div id="tab-content"></div>
            `;
            showElements();
            
            document.getElementById('pattern-list').innerHTML = '';
            document.getElementById('search').value = '';
        }
        
        function showElements() {
            if (!currentPattern) return;
            const tc = document.getElementById('tab-content');
            tc.innerHTML = currentPattern.elements.map(el => `
                <div class="element">
                    <h3>${el.name}</h3>
                    <div class="fpl">${el.first_principle_label || ''}</div>
                    <div class="specs"><strong>Specs:</strong> ${Object.entries(el.specs || {}).map(([k,v]) => k + ': ' + v).join(' | ')}</div>
                    ${el.variants ? '<div class="variants">' + el.variants.map(v => '<span class="variant">' + v.label + ': ' + (v.example || '') + '</span>').join('') + '</div>' : ''}
                    ${el.evidence ? el.evidence.map(ev => '<div class="evidence"><div class="study">📚 ' + ev.study + '</div><div class="finding">' + ev.finding + '</div><div class="lift">📈 ' + ev.lift_estimate + '</div></div>').join('') : ''}
                </div>
            `).join('');
            
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
        }
        
        async function showTemplate() {
            if (!currentPattern) return;
            const r = await fetch('/patterns/' + currentPattern.pattern_id + '/template');
            const html = await r.text();
            document.getElementById('tab-content').innerHTML = '<div class="template-preview"><pre>' + html.replace(/</g, '&lt;') + '</pre></div>';
            
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
        }
        
        function showWhoUses() {
            if (!currentPattern) return;
            const tc = document.getElementById('tab-content');
            const uses = currentPattern.who_uses || [];
            tc.innerHTML = '<div style="padding: 1rem 0;"><h3 style="color: #f8fafc; margin-bottom: 1rem;">Industries & Use Cases</h3><ul style="list-style: none; padding: 0;">' + 
                uses.map(u => '<li style="padding: 0.75rem; background: #0f172a; border-radius: 8px; margin-bottom: 0.5rem; color: #94a3b8;">🔹 ' + u + '</li>').join('') +
                '</ul></div>';
            
            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
            event.target.classList.add('active');
        }
        
        function searchPatterns(q) {
            if (!q.trim()) { renderList(patterns); return; }
            fetch('/patterns?search=' + encodeURIComponent(q))
                .then(r => r.json())
                .then(d => renderList(d.patterns));
        }
    </script>
</body>
</html>
"""

# ===========================
# Static files
# ===========================
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

if __name__ == "__main__":
    import uvicorn
    print("Starting Landing Page Pattern API on http://0.0.0.0:8002")
    print("Explorer: http://localhost:8002/explorer")
    print("Docs: http://localhost:8002/docs")
    uvicorn.run(app, host="0.0.0.0", port=8002)
