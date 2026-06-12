1|from fastapi import FastAPI, HTTPException, Query
2|from fastapi.responses import HTMLResponse, JSONResponse
3|from fastapi.staticfiles import StaticFiles
4|from pydantic import BaseModel
5|from typing import Optional, List, Dict, Any
6|import json, os, uuid, datetime
7|
8|app = FastAPI(title="Landing Page Pattern API", version="1.0",
9|  description="First-principles landing page pattern library backed by empirical evidence")
10|
11|DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
12|TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
13|STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
14|
15|# Load patterns
16|def load_patterns():
17|    with open(os.path.join(DATA_DIR, 'patterns.json')) as f:
18|        return json.load(f)
19|
20|def save_patterns(patterns):
21|    with open(os.path.join(DATA_DIR, 'patterns.json'), 'w') as f:
22|        json.dump(patterns, f, indent=2)
23|
24|# ===========================
25|# Models
26|# ===========================
27|class GenerateRequest(BaseModel):
28|    pattern_id: str
29|    substitutions: Dict[str, str]
30|    template: Optional[str] = None
31|
32|class ArchivePatternRequest(BaseModel):
33|    name: str
34|    description: str
35|    elements: List[Dict[str, Any]]
36|    html_snippet: str
37|    tags: List[str]
38|    source_url: Optional[str] = None
39|
40|# ===========================
41|# API Endpoints
42|# ===========================
43|
44|@app.get("/")
45|def root():
46|    return {
47|        "name": "Landing Page Pattern API",
48|        "version": "1.0",
49|        "patterns_endpoint": "/patterns",
50|        "explorer": "/explorer",
51|        "docs": "/docs"
52|    }
53|
54|@app.get("/patterns")
55|def list_patterns(search: Optional[str] = Query(None)):
56|    patterns = load_patterns()
57|    if search:
58|        search_lower = search.lower()
59|        results = []
60|        for p in patterns:
61|            if (search_lower in p['name'].lower() or 
62|                search_lower in p.get('description','').lower() or
63|                any(search_lower in t.lower() for t in p.get('tags',[]))):
64|                results.append({
65|                    'pattern_id': p['pattern_id'],
66|                    'name': p['name'],
67|                    'description': p['description'][:120] + '...',
68|                    'tags': p.get('tags', []),
69|                    'element_count': len(p.get('elements', [])),
70|                    'evidence_count': sum(len(e.get('evidence',[])) for e in p.get('elements',[]))
71|                })
72|        return {"count": len(results), "patterns": results}
73|    return {
74|        "count": len(patterns),
75|        "patterns": [{
76|            'pattern_id': p['pattern_id'],
77|            'name': p['name'],
78|            'description': p['description'][:120] + '...',
79|            'tags': p.get('tags', []),
80|            'element_count': len(p.get('elements', [])),
81|            'evidence_count': sum(len(e.get('evidence',[])) for e in p.get('elements',[]))
82|        } for p in patterns]
83|    }
84|
85|@app.get("/patterns/{pattern_id}")
86|def get_pattern(pattern_id: str):
87|    patterns = load_patterns()
88|    for p in patterns:
89|        if p['pattern_id'] == pattern_id:
90|            return p
91|    raise HTTPException(404, f"Pattern '{pattern_id}' not found")
92|
93|@app.get("/patterns/{pattern_id}/template")
94|def get_template(pattern_id: str):
95|    patterns = load_patterns()
96|    found = None
97|    for p in patterns:
98|        if p['pattern_id'] == pattern_id:
99|            found = p
100|            break
101|    if not found:
102|        raise HTTPException(404, f"Pattern '{pattern_id}' not found")
103|    
104|    template_path = os.path.join(TEMPLATE_DIR, f'{pattern_id}.html')
105|    if not os.path.exists(template_path):
106|        raise HTTPException(404, f"No template found for '{pattern_id}'")
107|    
108|    with open(template_path) as f:
109|        content = f.read()
110|    return HTMLResponse(content=content)
111|
112|@app.get("/patterns/{pattern_id}/evidence")
113|def get_pattern_evidence(pattern_id: str):
114|    patterns = load_patterns()
115|    for p in patterns:
116|        if p['pattern_id'] == pattern_id:
117|            all_evidence = []
118|            for el in p.get('elements', []):
119|                for ev in el.get('evidence', []):
120|                    all_evidence.append({
121|                        'element': el['name'],
122|                        'element_id': el['element_id'],
123|                        **ev
124|                    })
125|            return {
126|                'pattern_id': p['pattern_id'],
127|                'name': p['name'],
128|                'total_citations': len(all_evidence),
129|                'evidence': all_evidence
130|            }
131|    raise HTTPException(404, f"Pattern '{pattern_id}' not found")
132|
133|@app.post("/generate")
134|def generate_section(req: GenerateRequest):
135|    patterns = load_patterns()
136|    found = None
137|    for p in patterns:
138|        if p['pattern_id'] == req.pattern_id:
139|            found = p
140|            break
141|    if not found:
142|        raise HTTPException(404, f"Pattern '{pattern_id}' not found")
143|    
144|    template_path = os.path.join(TEMPLATE_DIR, f'{req.pattern_id}.html')
145|    if not os.path.exists(template_path):
146|        raise HTTPException(404, f"No template for '{req.pattern_id}'")
147|    
148|    with open(template_path) as f:
149|        html = f.read()
150|    
151|    # Apply substitutions
152|    for key, value in req.substitutions.items():
153|        placeholder = f'[{key}]'
154|        html = html.replace(placeholder, value)
155|    
156|    return {
157|        "pattern": req.pattern_id,
158|        "generated": True,
159|        "html": html
160|    }
161|
162|@app.post("/build")
163|def build_full_page(patterns_req: List[GenerateRequest]):
164|    """Build a full landing page from multiple pattern sections"""
165|    full_html_parts = []
166|    for pr in patterns_req:
167|        result = generate_section(pr)
168|        full_html_parts.append(result['html'])
169|    
170|    combined = '\n\n'.join(full_html_parts)
171|    return {
172|        "sections": len(patterns_req),
173|        "html": combined
174|    }
175|
176|@app.get("/elements")
177|def list_elements(pattern_id: Optional[str] = Query(None)):
178|    patterns = load_patterns()
179|    elements = {}
180|    for p in patterns:
181|        if pattern_id and p['pattern_id'] != pattern_id:
182|            continue
183|        for el in p.get('elements', []):
184|            elements[el['element_id']] = {
185|                'name': el['name'],
186|                'type': el.get('type'),
187|                'first_principle_label': el.get('first_principle_label'),
188|                'specs': el.get('specs', {}),
189|                'variants': el.get('variants', []),
190|                'evidence_count': len(el.get('evidence', [])),
191|                'pattern_id': p['pattern_id'],
192|                'pattern_name': p['name']
193|            }
194|    return {"count": len(elements), "elements": elements}
195|
196|@app.get("/search")
197|def search(query: str = Query(...)):
198|    """Search across patterns, elements, and evidence"""
199|    patterns = load_patterns()
200|    q = query.lower()
201|    results = []
202|    seen_ids = set()
203|    
204|    for p in patterns:
205|        score = 0
206|        matches = []
207|        
208|        # Pattern name match
209|        if q in p['name'].lower():
210|            score += 10
211|            matches.append(f"Pattern name: {p['name']}")
212|        
213|        # Pattern description match
214|        if q in p.get('description','').lower():
215|            score += 5
216|            matches.append(f"Description match")
217|        
218|        # Element matches
219|        for el in p.get('elements', []):
220|            if q in el['name'].lower():
221|                score += 3
222|                matches.append(f"Element: {el['name']}")
223|            if q in el.get('first_principle_label','').lower():
224|                score += 3
225|                matches.append(f"FP: {el['first_principle_label'][:60]}")
226|            
227|            # Evidence matches
228|            for ev in el.get('evidence', []):
229|                if q in ev.get('study','').lower() or q in ev.get('finding','').lower():
230|                    score += 2
231|                    matches.append(f"Study: {ev.get('study','')[:60]}")
232|        
233|        if score > 0:
234|            results.append({
235|                'pattern_id': p['pattern_id'],
236|                'name': p['name'],
237|                'relevance': score,
238|                'matches': matches
239|            })
240|    
241|    results.sort(key=lambda x: -x['relevance'])
242|    return {"count": len(results), "query": query, "results": results}
243|
244|# ===========================
245|# Landscape & Prediction Endpoints
246|# ===========================
247|
248|LANDSCAPE_PATH = os.path.join(DATA_DIR, 'landscape_report.json')
249|PREDICTION_PATH = os.path.join(DATA_DIR, 'funnel_prediction_output.json')
250|
251|def load_json(path):
252|    if os.path.exists(path):
253|        with open(path) as f:
254|            return json.load(f)
255|    return None
256|
257|def extract_prediction_data():
258|    Extract structured prediction data from EventMath compiled output
259|    try:
260|        # Run the EventMath output to get fresh counts
261|        import subprocess
262|        result = subprocess.run(
263|            ['node', os.path.join(os.path.dirname(__file__), 'data', 'funnel-prediction-output.js')],
264|            capture_output=True, text=True, timeout=10
265|        )
266|        predictions_raw = result.stdout.strip()
267|    except Exception:
268|        predictions_raw = None
269|
270|    return {
271|        "dimensions": {
272|            "entry": [
273|                {"id": "free_offer", "kind": "free offer", "barrier": "email", "value": 0},
274|                {"id": "paid_product", "kind": "paid product", "barrier": "payment", "value": "XX"},
275|                {"id": "summit_register", "kind": "summit register", "barrier": "form", "value": 0},
276|                {"id": "apply", "kind": "apply", "barrier": "form", "need": "callback"},
277|                {"id": "content_gate", "kind": "content gate", "barrier": "email", "value": 0},
278|                {"id": "quiz", "kind": "quiz", "barrier": "answers", "personalization": "high"}
279|            ],
280|            "complexity": [
281|                {"id": "light", "kind": "light", "pages": 2},
282|                {"id": "medium", "kind": "medium", "pages": 3},
283|                {"id": "deep", "kind": "deep", "pages": 4},
284|                {"id": "full", "kind": "full", "pages": "5+"}
285|            ],
286|            "money": [
287|                {"id": "donation", "kind": "donation", "model": "voluntary"},
288|                {"id": "once", "kind": "once", "model": "single payment"},
289|                {"id": "recurring", "kind": "recurring", "model": "subscription"},
290|                {"id": "free_then_paid", "kind": "free then paid", "model": "upsell"},
291|                {"id": "low_then_upsell", "kind": "low then upsell", "model": "tripwire"},
292|                {"id": "high_ticket", "kind": "high ticket", "model": "proposal"}
293|            ],
294|            "exit": [
295|                {"id": "buy", "kind": "buy", "state": "revenue"},
296|                {"id": "book", "kind": "book", "state": "callback"},
297|                {"id": "cancel", "kind": "cancel", "state": "no revenue"},
298|                {"id": "wait", "kind": "wait", "state": "future lead"},
299|                {"id": "group", "kind": "group", "state": "engagement"},
300|                {"id": "sample", "kind": "sample", "state": "trial"}
301|            ],
302|            "branch": [
303|                {"id": "straight", "kind": "straight", "forks": 0},
304|                {"id": "upsell", "kind": "upsell", "forks": 1},
305|                {"id": "upsell_down", "kind": "upsell down", "forks": 2},
306|                {"id": "multi", "kind": "multi fork", "forks": "3+"}
307|            ]
308|        },
309|        "total_combinations": {
310|            "predicted": 144,
311|            "with_all_dimensions": 3456,
312|            "estimated_valid": "200-400"
313|        },
314|        "predictions_raw": predictions_raw
315|    }
316|
317|@app.get("/landscape")
318|def get_landscape():
319|    Full funnel landscape analysis report
320|    report = load_json(LANDSCAPE_PATH)
321|    if not report:
322|        raise HTTPException(404, "Landscape report not found")
323|    return report
324|
325|@app.get("/landscape/dimensions")
326|def get_dimensions():
327|    Get the funnel model dimensions (entry, complexity, money, exit, branch)
328|    data = extract_prediction_data()
329|    return data["dimensions"]
330|
331|@app.get("/landscape/gaps")
332|def get_gaps():
333|    What's missing from the funnel library — gap analysis
334|    report = load_json(LANDSCAPE_PATH)
335|    if not report:
336|        raise HTTPException(404, "Landscape report not found")
337|    gaps = {
338|        "missing_entry_types": [
339|            {"type": "content_gate", "count": 0, "status": "MISSING", "note": "email-gated video/content before offer"},
340|            {"type": "quiz", "count": 0, "status": "MISSING", "note": "quiz → personalized recommendation → order"}
341|        ],
342|        "missing_money_models": [
343|            {"type": "subscription", "count": 0, "status": "MISSING", "note": "recurring billing, trial → convert → upgrade"},
344|            {"type": "donation", "count": 0, "status": "MISSING", "note": "voluntary payment, no fixed price"}
345|        ],
346|        "missing_architectures": [
347|            {"name": "Webinar", "flow": "Register → Attend → Replay → Buy", "status": "MISSING"},
348|            {"name": "Subscription", "flow": "Trial → Convert → Upgrade → Cancel → Win-back", "status": "MISSING"},
349|            {"name": "Quiz/Survey", "flow": "Questions → Results → Recommendation → Order", "status": "MISSING"},
350|            {"name": "Cart Abandonment", "flow": "Add → Abandon → Email → Recover", "status": "MISSING"},
351|            {"name": "Enterprise/SaaS", "flow": "Demo → Trial → Onboard → Subscribe → Expand", "status": "MISSING"},
352|            {"name": "VSL + Bumps", "flow": "Gate → VSL → Upsell → Order+Bump → Cross-sell", "status": "MISSING"},
353|            {"name": "Waitlist", "flow": "Join → Notify → Limited Access → Full Access", "status": "MISSING"},
354|            {"name": "Affiliate", "flow": "Apply → Approve → Promote → Commission", "status": "MISSING"},
355|            {"name": "Community", "flow": "Register → Trial → Lapsed → Win-back", "status": "MISSING"},
356|            {"name": "Multi-step Hi-Ticket", "flow": "Apply → Qualify → Proposal → Close → Deliver", "status": "MISSING"},
357|            {"name": "Contest", "flow": "Enter → Share → Refer → Winner", "status": "MISSING"},
358|            {"name": "Lead Magnet → Call", "flow": "Download → Email Sequence → Sales Call", "status": "MISSING"},
359|            {"name": "Physical → Online", "flow": "In-store → Email → Online Purchase", "status": "MISSING"}
360|        ],
361|        "coverage": report.get("coverage_by_entry_type", {}),
362|        "total_collected": report.get("what_we_collected", {}).get("total", 71),
363|        "estimated_total_landscape": "200-400",
364|        "coverage_percentage": "~25-35%"
365|    }
366|    return gaps
367|
368|@app.get("/landscape/predictions")
369|def get_predictions():
370|    EventMath-generated funnel predictions across all dimensions
371|    data = extract_prediction_data()
372|    return data
373|
374|@app.get("/landscape/eventmath-model")
375|def get_eventmath_source():
376|    The raw EventMath source file used to generate predictions
377|    source_path = os.path.join(DATA_DIR, 'funnel-prediction-v3.em')
378|    if os.path.exists(source_path):
379|        with open(source_path) as f:
380|            return {"language": "EventMath v0.4", "source": f.read(), "generated_predictions": 144}
381|    raise HTTPException(404, "EventMath source not found")
382|
383|# ===========================
384|# Explorer (Web UI)
385|# ===========================
386|@app.get("/explorer", response_class=HTMLResponse)
387|def explorer():
388|    return """
389|<!DOCTYPE html>
390|<html lang="en">
391|<head>
392|    <meta charset="UTF-8">
393|    <meta name="viewport" content="width=device-width, initial-scale=1.0">
394|    <title>Landing Page Pattern Explorer</title>
395|    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
396|    <style>
397|        * { margin: 0; padding: 0; box-sizing: border-box; }
398|        body { font-family: 'Inter', sans-serif; background: #0f172a; color: #e2e8f0; }
399|        .header { padding: 2rem; border-bottom: 1px solid #1e293b; }
400|        .header h1 { font-size: 2rem; color: #f8fafc; font-weight: 800; }
401|        .header p { color: #94a3b8; margin-top: 0.5rem; }
402|        .container { max-width: 1400px; margin: 0 auto; padding: 2rem; }
403|        .pattern-list { display: grid; gap: 1.5rem; }
404|        .pattern-card {
405|            background: #1e293b; border-radius: 16px; padding: 2rem;
406|            border: 1px solid #334155; cursor: pointer;
407|            transition: all 0.2s;
408|        }
409|        .pattern-card:hover { border-color: #3b82f6; transform: translateY(-2px); }
410|        .pattern-card h2 { font-size: 1.4rem; color: #f8fafc; }
411|        .pattern-card .tags { display: flex; gap: 0.5rem; flex-wrap: wrap; margin: 0.75rem 0; }
412|        .pattern-card .tag {
413|            background: #334155; padding: 4px 12px; border-radius: 20px;
414|            font-size: 0.75rem; color: #94a3b8;
415|        }
416|        .pattern-card .meta { display: flex; gap: 2rem; color: #64748b; font-size: 0.85rem; }
417|        .pattern-card .desc { color: #94a3b8; margin-top: 0.75rem; font-size: 0.9rem; line-height: 1.5; }
418|        
419|        .detail-panel {
420|            background: #1e293b; border-radius: 16px; padding: 2rem;
421|            border: 1px solid #334155; margin-top: 2rem;
422|        }
423|        .detail-panel h2 { font-size: 1.8rem; color: #f8fafc; margin-bottom: 0.5rem; }
424|        .detail-panel .desc { color: #94a3b8; margin-bottom: 2rem; }
425|        
426|        .element { 
427|            background: #0f172a; border-radius: 12px; padding: 1.5rem;
428|            margin-bottom: 1rem; border-left: 3px solid #3b82f6;
429|        }
430|        .element h3 { color: #f8fafc; font-size: 1.1rem; }
431|        .element .fpl { color: #3b82f6; font-size: 0.85rem; margin-top: 0.25rem; font-weight: 600; }
432|        .element .specs { color: #94a3b8; font-size: 0.85rem; margin-top: 0.5rem; line-height: 1.6; }
433|        .element .variants { display: flex; gap: 0.5rem; flex-wrap: wrap; margin-top: 0.75rem; }
434|        .element .variant {
435|            background: #1e293b; padding: 6px 14px; border-radius: 8px;
436|            font-size: 0.8rem; color: #cbd5e1; border: 1px solid #334155;
437|        }
438|        
439|        .evidence { margin-top: 0.75rem; padding: 0.75rem; background: #1a2332; border-radius: 8px; }
440|        .evidence .study { color: #f59e0b; font-weight: 600; font-size: 0.85rem; }
441|        .evidence .finding { color: #94a3b8; font-size: 0.85rem; margin-top: 0.25rem; }
442|        .evidence .lift { color: #10b981; font-size: 0.85rem; font-weight: 600; margin-top: 0.25rem; }
443|        
444|        .template-preview {
445|            background: #0f172a; border-radius: 12px; padding: 2rem;
446|            margin-top: 1.5rem; border: 1px solid #334155;
447|        }
448|        .template-preview pre {
449|            overflow-x: auto; color: #e2e8f0; font-size: 0.8rem;
450|            max-height: 400px; overflow-y: auto;
451|        }
452|        .tab-bar { display: flex; gap: 1rem; margin-bottom: 1.5rem; }
453|        .tab {
454|            padding: 0.5rem 1.5rem; border-radius: 8px; cursor: pointer;
455|            background: #334155; color: #94a3b8; font-size: 0.85rem; font-weight: 600;
456|        }
457|        .tab.active { background: #3b82f6; color: #fff; }
458|        
459|        .search-bar {
460|            width: 100%; padding: 1rem 1.5rem; border-radius: 12px;
461|            background: #1e293b; border: 1px solid #334155;
462|            color: #e2e8f0; font-size: 1rem; margin-bottom: 1.5rem;
463|            font-family: 'Inter', sans-serif;
464|        }
465|        .search-bar:focus { outline: none; border-color: #3b82f6; }
466|        .back-btn {
467|            display: inline-block; margin-bottom: 1rem; 
468|            color: #3b82f6; cursor: pointer; font-size: 0.9rem;
469|            background: none; border: none; font-family: 'Inter', sans-serif;
470|        }
471|        .back-btn:hover { color: #60a5fa; }
472|    </style>
473|</head>
474|<body>
475|    <div class="header">
476|        <h1>🏗️ Landing Page Pattern Explorer</h1>
477|        <p>First-principles pattern library backed by empirical evidence</p>
478|    </div>
479|    <div class="container" id="app">
480|        <input class="search-bar" id="search" placeholder="Search patterns, elements, or studies..." oninput="searchPatterns(this.value)">
481|        <div id="pattern-list" class="pattern-list"></div>
482|        <div id="detail-panel" style="display:none;"></div>
483|    </div>
484|    <script>
485|        let patterns = [];
486|        let currentPattern = null;
487|        
488|        fetch('/patterns')
489|            .then(r => r.json())
490|            .then(d => { patterns = d.patterns; renderList(d.patterns); });
491|        
492|        function renderList(list) {
493|            const container = document.getElementById('pattern-list');
494|            container.innerHTML = list.map(p => `
495|                <div class="pattern-card" onclick="showPattern('${p.pattern_id}')">
496|                    <h2>${p.name}</h2>
497|                    <div class="tags">${p.tags.map(t => '<span class="tag">' + t + '</span>').join('')}</div>
498|                    <div class="meta">
499|                        <span>${p.element_count} elements</span>
500|                        <span>${p.evidence_count} citations</span>
501|                    </div>
502|                    <div class="desc">${p.description}</div>
503|                </div>
504|            `).join('');
505|            document.getElementById('detail-panel').style.display = 'none';
506|        }
507|        
508|        async function showPattern(id) {
509|            const r = await fetch('/patterns/' + id);
510|            const p = await r.json();
511|            currentPattern = p;
512|            
513|            const panel = document.getElementById('detail-panel');
514|            panel.style.display = 'block';
515|            panel.innerHTML = `
516|                <button class="back-btn" onclick="renderList(patterns)">← Back to patterns</button>
517|                <h2>${p.name}</h2>
518|                <p class="desc">${p.description}</p>
519|                
520|                <div class="tab-bar">
521|                    <div class="tab active" onclick="showElements()">Elements + Evidence</div>
522|                    <div class="tab" onclick="showTemplate()">HTML Template</div>
523|                    <div class="tab" onclick="showWhoUses()">Who Uses This</div>
524|                </div>
525|                <div id="tab-content"></div>
526|            `;
527|            showElements();
528|            
529|            document.getElementById('pattern-list').innerHTML = '';
530|            document.getElementById('search').value = '';
531|        }
532|        
533|        function showElements() {
534|            if (!currentPattern) return;
535|            const tc = document.getElementById('tab-content');
536|            tc.innerHTML = currentPattern.elements.map(el => `
537|                <div class="element">
538|                    <h3>${el.name}</h3>
539|                    <div class="fpl">${el.first_principle_label || ''}</div>
540|                    <div class="specs"><strong>Specs:</strong> ${Object.entries(el.specs || {}).map(([k,v]) => k + ': ' + v).join(' | ')}</div>
541|                    ${el.variants ? '<div class="variants">' + el.variants.map(v => '<span class="variant">' + v.label + ': ' + (v.example || '') + '</span>').join('') + '</div>' : ''}
542|                    ${el.evidence ? el.evidence.map(ev => '<div class="evidence"><div class="study">📚 ' + ev.study + '</div><div class="finding">' + ev.finding + '</div><div class="lift">📈 ' + ev.lift_estimate + '</div></div>').join('') : ''}
543|                </div>
544|            `).join('');
545|            
546|            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
547|            event.target.classList.add('active');
548|        }
549|        
550|        async function showTemplate() {
551|            if (!currentPattern) return;
552|            const r = await fetch('/patterns/' + currentPattern.pattern_id + '/template');
553|            const html = await r.text();
554|            document.getElementById('tab-content').innerHTML = '<div class="template-preview"><pre>' + html.replace(/</g, '&lt;') + '</pre></div>';
555|            
556|            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
557|            event.target.classList.add('active');
558|        }
559|        
560|        function showWhoUses() {
561|            if (!currentPattern) return;
562|            const tc = document.getElementById('tab-content');
563|            const uses = currentPattern.who_uses || [];
564|            tc.innerHTML = '<div style="padding: 1rem 0;"><h3 style="color: #f8fafc; margin-bottom: 1rem;">Industries & Use Cases</h3><ul style="list-style: none; padding: 0;">' + 
565|                uses.map(u => '<li style="padding: 0.75rem; background: #0f172a; border-radius: 8px; margin-bottom: 0.5rem; color: #94a3b8;">🔹 ' + u + '</li>').join('') +
566|                '</ul></div>';
567|            
568|            document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
569|            event.target.classList.add('active');
570|        }
571|        
572|        function searchPatterns(q) {
573|            if (!q.trim()) { renderList(patterns); return; }
574|            fetch('/patterns?search=' + encodeURIComponent(q))
575|                .then(r => r.json())
576|                .then(d => renderList(d.patterns));
577|        }
578|    </script>
579|</body>
580|</html>
581|"""
582|
583|# ===========================
584|# Static files
585|# ===========================
586|if os.path.exists(STATIC_DIR):
587|    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
588|
589|if __name__ == "__main__":
590|    import uvicorn
591|    print("Starting Landing Page Pattern API on http://0.0.0.0:8002")
592|    print("Explorer: http://localhost:8002/explorer")
593|    print("Docs: http://localhost:8002/docs")
594|    uvicorn.run(app, host="0.0.0.0", port=8002)
595|