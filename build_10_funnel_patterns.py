#!/usr/bin/env python3
"""
Build 10 funnel patterns from the Diee Mas HTML Templates bundle.
Each funnel has 3-4 pages (optin, upsell/order, thank you, etc.)
"""
import json, os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(TEMPLATE_DIR, exist_ok=True)

patterns = []
templates = {}

###############################################################################
# FUNNEL 1: Diet & Weight Loss (Two Step Tripwire)
###############################################################################
patterns.append({
    "pattern_id": "diet_weight_loss_tripwire",
    "name": "Diet & Weight Loss Tripwire Funnel",
    "description": "A complete 4-page sales funnel for a diet/weight loss supplement product. Page 1: Long-form VSL optin page with scarcity countdown, product hero, pain-point targeting, scientific proof, before/after testimonials, review grid, FAQ accordion. Page 2: One-time upsell (hash-triggered popup variant). Page 3: Order confirmation/thank you with product receipt and next steps. Page 4: Order cancelled confirmation.",
    "first_principles": {
        "scarcity_trigger": "Countdown timer + limited stock warning creates urgency to act immediately",
        "risk_reversal": "Pay shipping only ($6.98) eliminates financial risk barrier",
        "social_proof_layers": "Before/after photos + review grid with star ratings + '75,654 samples shipped' builds multi-layer trust",
        "pain_point_mirroring": "'If you've tried and failed' language mirrors the user's exact frustration",
        "scientific_authority": "'100% scientifically proven' badge with lab imagery adds credibility"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/diet-weight-loss/",
        "upsell": "https://demonavigator.com/demo/diet-weight-loss/#otopopup",
        "thank_you": "https://demonavigator.com/demo/diet-weight-loss/thank-you.html",
        "cancel": "https://demonavigator.com/demo/diet-weight-loss/order-cancelled.html"
    },
    "tags": ["funnel", "diet", "weight-loss", "tripwire", "vsl", "health", "supplement", "optin", "thank-you"]
})

###############################################################################
# FUNNEL 2: Chiropractic Care (Application)
###############################################################################
patterns.append({
    "pattern_id": "chiropractic_demo_funnel",
    "name": "Chiropractic Care Application Funnel",
    "description": "A 4-page healthcare funnel: Long-form optin landing page with hero, benefits, pain-motivation, beliefs, therapies, testimonials, FAQ → Order form page → Appointment confirmation page with phone CTA → Thank you page with product receipt.",
    "first_principles": {
        "trust_building": "Blue medical palette + doctor credentials + before/after proof establishes authority",
        "pain_to_action": "'Why are you suffering?' reframes pain as solvable with one call",
        "multi_touch_cta": "CTA repeated 5+ times across the page — the user never has to search for how to convert",
        "appointment_to_upsell": "Confirmation page drives phone calls (highest converting channel) + upsell to order"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/chiropractic-care/",
        "order": "https://demonavigator.com/demo/chiropractic-care/order.html",
        "appointment_confirmation": "https://demonavigator.com/demo/chiropractic-care/appointment-confirmation.html",
        "thank_you": "https://demonavigator.com/demo/chiropractic-care/thank-you.html"
    },
    "tags": ["funnel", "chiropractic", "healthcare", "optin", "order-form", "appointment", "thank-you"]
})

###############################################################################
# FUNNEL 3: MLM Network (Summit)
###############################################################################
patterns.append({
    "pattern_id": "mlm_network_summit",
    "name": "MLM Network Summit Funnel",
    "description": "A summit/event registration funnel for MLM Network professionals. Page 1: Event landing with speaker lineup, schedule, testimonials, FAQ, free ticket CTA. Page 2: One-time offer upsell for lifetime access ($67). Page 3: Order/checkout form. Page 4: Thank you with access details, Facebook group, and event highlights video.",
    "first_principles": {
        "event_scarcity": "Limited seats + free ticket CTA drives registration volume",
        "upsell_after_free": "Free ticket → paid upgrade ($67) captures value after commitment",
        "social_proof": "12 speakers + 20 sessions + 16 hours consulting builds event credibility",
        "community_access": "Facebook group CTA on thank-you page builds post-event engagement"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/mlm-network/",
        "oto": "https://demonavigator.com/demo/mlm-network/oto.html",
        "order": "https://demonavigator.com/demo/mlm-network/order.html",
        "thank_you": "https://demonavigator.com/demo/mlm-network/thank-you.html"
    },
    "tags": ["funnel", "mlm", "network", "summit", "event", "registration", "optin", "upsell"]
})

###############################################################################
# FUNNEL 4: Cyber Security Summit
###############################################################################
patterns.append({
    "pattern_id": "cyber_security_summit",
    "name": "Cyber Security Summit Funnel",
    "description": "A 4-page summit registration funnel: Event landing (STEVE MARTIN host, 70+ hours, 11 speakers, schedule, testimonials, FAQ) → One-time offer upsell to lifetime access ($247) → Order/checkout form → Thank you with purchase receipt and schedule link.",
    "first_principles": {
        "authority_host": "Named host (Steve Martin) + 11 expert speakers builds event authority",
        "high_value_upsell": "$485 value → $247 creates massive perceived discount (49% off)",
        "time_urgency": "Countdown timer + '800 seats, few left' drives registration action",
        "schedule_transparency": "Full 3-day schedule listed builds attendee confidence"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/cyber-security-summit/index.html",
        "oto": "https://demonavigator.com/demo/cyber-security-summit/oto.html",
        "order": "https://demonavigator.com/demo/cyber-security-summit/order.html",
        "thank_you": "https://demonavigator.com/demo/cyber-security-summit/thank-you.html"
    },
    "tags": ["funnel", "cyber-security", "summit", "event", "tech", "registration", "upsell"]
})

###############################################################################
# FUNNEL 5: Professional Therapist
###############################################################################
patterns.append({
    "pattern_id": "therapist_application",
    "name": "Professional Therapist Application Funnel",
    "description": "A 4-page therapy services funnel: Service landing (clinical psychologist, therapy types for men/women/couples/children, testimonials, FAQ) → One-time offer upsell ($67 Life Changing Kit) → Order form → Thank you with Facebook group and product receipt.",
    "first_principles": {
        "empathy_first": "'I Could Help You Too' + 'Make A Positive Change' — emotional framing before clinical detail",
        "service_menu": "3 therapy types (child, teen, parent) gives clear options for different visitors",
        "kit_upsell": "Physical product upsell after free consultation captures additional revenue",
        "low_friction_cta": "'Get a Free Consultation' with no-obligation language reduces barrier"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/therapist/index.html",
        "oto": "https://demonavigator.com/demo/therapist/oto.html",
        "order": "https://demonavigator.com/demo/therapist/order.html",
        "thank_you": "https://demonavigator.com/demo/therapist/thank-you.html"
    },
    "tags": ["funnel", "therapy", "psychology", "healthcare", "optin", "upsell", "mental-health"]
})

###############################################################################
# FUNNEL 6: Software Launch
###############################################################################
patterns.append({
    "pattern_id": "software_launch_funnel",
    "name": "Software Launch Application Funnel",
    "description": "A 4-page SaaS/product funnel: Feature landing page with 6 core features, testimonials, FAQ, lifetime access CTA ($97) → Video page (3 product videos) → Order/checkout form → Thank you with purchase receipt and testimonials.",
    "first_principles": {
        "feature_showcase": "6 feature icons with descriptions show breadth before depth",
        "video_confirmation": "Separate video page lets users see the product in action before buying",
        "lifetime_value": "'Lifetime access for $97' eliminates subscription fear",
        "expert_endorsement": "Industry expert titles on testimonials add B2B credibility"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/the-software-launch/",
        "video": "https://demonavigator.com/demo/the-software-launch/video-01.html",
        "order": "https://demonavigator.com/demo/the-software-launch/order.html",
        "thank_you": "https://demonavigator.com/demo/the-software-launch/thank-you.html"
    },
    "tags": ["funnel", "software", "saas", "tech", "launch", "optin", "video", "lifetime-access"]
})

###############################################################################
# FUNNEL 7: 10X Revenue
###############################################################################
patterns.append({
    "pattern_id": "ten_x_revenue_funnel",
    "name": "10X Revenue Application Funnel",
    "description": "A 4-page business coaching funnel: High-scarcity landing page (only 100 spots, 'Never Lower The Target' motivation, 3 benefits, 3 secrets, testimonials, FAQ) → Short application form → Thank you with congratulations → Privacy policy page.",
    "first_principles": {
        "extreme_scarcity": "Only 100 spots, most renew year after year — highest tier of artificial scarcity",
        "challenge_framing": "'Simply work hard and BE BETTER' positions the program as demanding — attracting only serious applicants",
        "no_quit_guarantee": "'We don't stop until you get it done' eliminates the fear of wasting money",
        "application_gate": "Short application form filters leads before full commitment"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/10x-there-revenue/index.html",
        "apply": "https://demonavigator.com/demo/10x-there-revenue/apply.html",
        "thank_you": "https://demonavigator.com/demo/10x-there-revenue/thank-you.html",
        "privacy": "https://demonavigator.com/demo/10x-there-revenue/privacy-policy.html"
    },
    "tags": ["funnel", "business", "coaching", "revenue", "scarcity", "application", "optin"]
})

###############################################################################
# FUNNEL 8: Lifestyle & Health Coach
###############################################################################
patterns.append({
    "pattern_id": "health_coach_funnel",
    "name": "Lifestyle & Health Coach Application Funnel",
    "description": "A 4-page health coaching funnel: Service landing page (Jane Doe coach, 90-Day Total Body Transformation, 3 focus areas: nutrition, lifestyle, mind/body) → Order/checkout form ($30) → Thank you with next steps and video → Privacy policy.",
    "first_principles": {
        "coach_personality": "Named coach (Jane Doe) with photo humanizes the program and builds personal trust",
        "holistic_framing": "3 focus areas (nutrition, lifestyle, mind/body) positions the program as comprehensive",
        "fast_action_urgency": "'FAST Action Takers Only' creates superior commitment framing",
        "transformation_timeline": "'90-Day' gives a concrete, achievable timeframe"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/health-coach/",
        "order": "https://demonavigator.com/demo/health-coach/order.html",
        "thank_you": "https://demonavigator.com/demo/health-coach/thank-you.html",
        "privacy": "https://demonavigator.com/demo/health-coach/privacy-policy.html"
    },
    "tags": ["funnel", "health", "coach", "lifestyle", "transformation", "optin", "nutrition"]
})

###############################################################################
# FUNNEL 9: Pet Care
###############################################################################
patterns.append({
    "pattern_id": "pet_care_funnel",
    "name": "Pet Care Application Funnel",
    "description": "A 4-page pet care services funnel: Service landing ('We Pampering Pets', sitting/minding/training/grooming services, spot-your-pet app feature, testimonials, FAQ, trial CTA) → Upsell page (50% off original $99 → $79) → Order/checkout form with subscription → Thank you with support links.",
    "first_principles": {
        "service_menu": "4 pet services (sitting, minding, training, grooming) gives pet owners clear options",
        "app_integration": "'Spot your pet anytime, anywhere' — tech-enabled trust for anxious pet owners",
        "subscription_model": "Monthly pricing creates recurring revenue from pet care needs",
        "trial_offer": "'Wish to Require a Trial?' — low-barrier entry before full commitment"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/pet-care/",
        "upsell": "https://demonavigator.com/demo/pet-care/upsell.html",
        "order": "https://demonavigator.com/demo/pet-care/order.html",
        "thank_you": "https://demonavigator.com/demo/pet-care/thank-you.html"
    },
    "tags": ["funnel", "pet-care", "pets", "dogs", "service", "subscription", "optin", "app"]
})

###############################################################################
# FUNNEL 10: Beauty Salon & Spa
###############################################################################
patterns.append({
    "pattern_id": "salon_spa_funnel",
    "name": "Beauty Salon & Spa Application Funnel",
    "description": "A 4-page beauty/salon funnel: Service landing (8 beauty services: makeup, haircut, color, setting, photography, skin, fashion, bridal, testimonials, portfolio) → Upsell page (50% off offer → $150) → Order/checkout form → Thank you with steps and social links.",
    "first_principles": {
        "visual_portfolio": "8 service images + 8 portfolio images show the quality before asking for commitment",
        "service_breadth": "8 distinct beauty services positions salon as one-stop-shop",
        "bridal_premium": "Bridal makeup listed as separate service — high-ticket premium offering",
        "portfolio_as_proof": "'See Our Work!' gallery acts as visual social proof before the upsell"
    },
    "pages": {
        "optin": "https://demonavigator.com/demo/salon-spa/",
        "upsell": "https://demonavigator.com/demo/salon-spa/upsell.html",
        "order": "https://demonavigator.com/demo/salon-spa/order.html",
        "thank_you": "https://demonavigator.com/demo/salon-spa/thank-you.html"
    },
    "tags": ["funnel", "beauty", "salon", "spa", "makeup", "hair", "services", "optin", "bridal"]
})


###############################################################################
# Write all patterns to JSON
###############################################################################
patterns_path = os.path.join(DATA_DIR, "patterns.json")

existing = []
if os.path.exists(patterns_path):
    with open(patterns_path) as f:
        existing = json.load(f)

existing_ids = {p['pattern_id'] for p in existing}
for np in patterns:
    if np['pattern_id'] in existing_ids:
        print(f"  Replacing existing: {np['pattern_id']}")
        existing = [p for p in existing if p['pattern_id'] != np['pattern_id']]

all_patterns = existing + patterns
with open(patterns_path, 'w') as f:
    json.dump(all_patterns, f, indent=2, ensure_ascii=False)

print(f"Written {len(all_patterns)} total patterns to {patterns_path}")
print(f"Added {len(patterns)} new funnel patterns:")

# Create a text-index file for the screenshots
import textwrap
index_html = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<title>Funnel Screenshots Index</title>
<style>
body{font-family:monospace;background:#0f172a;color:#e2e8f0;padding:20px;max-width:1400px;margin:0 auto;}
h1{color:#f8fafc;border-bottom:2px solid #334155;padding-bottom:10px;}
.funnel{margin:30px 0;padding:20px;background:#1e293b;border-radius:12px;border:1px solid #334155;}
.funnel h2{color:#3b82f6;margin-bottom:10px;}
.pages{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:15px;margin-top:15px;}
.page{background:#0f172a;border-radius:8px;overflow:hidden;border:1px solid #334155;}
.page img{width:100%;display:block;}
.page .label{padding:8px 12px;font-size:12px;color:#94a3b8;background:#1e293b;}
</style></head><body>
<h1>📸 Funnel Screenshots Index</h1>
<p>10 funnels × 4 pages each = 40 screenshots</p>
"""

for p in patterns:
    pid = p['pattern_id']
    name = p['name']
    pages = p.get('pages', {})
    folder = pid.replace('_funnel','').replace('_','-')
    
    index_html += f'<div class="funnel">\n<h2>{name}</h2>\n<p><code>{pid}</code></p>\n<div class="pages">\n'
    for pkey, purl in pages.items():
        img_path = f'screenshots/{folder}/{pkey}.png'
        index_html += f'<div class="page"><img src="../{img_path}" alt="{pkey}" loading="lazy"><div class="label">{pkey} — {purl}</div></div>\n'
    index_html += '</div></div>\n'

index_html += '</body></html>'

with open(os.path.join(os.path.dirname(__file__), 'screenshots_index.html'), 'w') as f:
    f.write(index_html)
print("Written screenshots_index.html")

print("\nFunnel patterns added:")
for p in patterns:
    pages = list(p.get('pages', {}).keys())
    print(f"  • {p['pattern_id']:40s} | {len(pages)} pages: {', '.join(pages)}")