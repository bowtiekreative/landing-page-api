#!/usr/bin/env python3
"""
Build 56 funnel patterns from V2-V7 funnel template bundles.
Each has 3-4 pages with page URLs for reference.
"""
import json, os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(DATA_DIR, exist_ok=True)

patterns = []

def make(pid, name, desc, pages, tags, fp_principle=None):
    entry = {
        "pattern_id": pid,
        "name": name,
        "description": desc[:200],
        "version_group": "v2-v7",
        "first_principles": fp_principle or {"core": "High-converting HTML funnel template with ready-made pages"},
        "pages": pages,
        "elements": [{"element_id": f"{pid[:4]}_{i:02d}", "name": pname.title(), "type": "page", "specs": {"url": purl}} for i, (pname, purl) in enumerate(pages.items())],
        "tags": ["funnel", "html-template", "v2-v7"] + tags[:3]
    }
    entry["element_count"] = len(entry["elements"])
    entry["evidence_count"] = 0
    return entry

###############################################################################
# V2 — 10 funnels
###############################################################################
v2_demos = [
    ("v2_make_money_online", "Make Money Online Summit", ["Optin","Upsell","Order","Thank You"], "demo/money-online/.md"),
    ("v2_vacation", "Vacation Application Funnel", ["Optin","Upsell","Order","Thank You"], "demo/vacation/"),
    ("v2_green_tea", "Green Tea Summit Funnel", ["Optin","Upsell","Upsell 2","Thank You"], "demo/green-tea-v2/"),
    ("v2_dog_food", "Dog Food Summit Funnel", ["Optin","Upsell","Upsell 2","Thank You"], "demo/dog-food/"),
    ("v2_beauty_product", "Self-Love Beauty Product Summit", ["Optin","OTO","Downsell","Thank You"], "demo/selflove-beauty-product/"),
    ("v2_entrepreneurs", "Entrepreneurs Webinar Application", ["Optin","Upsell","Order","Thank You"], "demo/entrepreneurs/"),
    ("v2_business_consultant", "Business Consultant Application", ["Optin","OTO","Order","Thank You"], "demo/business-consultant-application/"),
    ("v2_juice", "Juice Application Funnel", ["Optin","Upsell","Order","Thank You"], "demo/juice/"),
    ("v2_nutritionist", "Professional Nutritionist Application", ["Optin","Upsell","Order","Thank You"], "demo/nutritionist/"),
    ("v2_ebook_course", "Ebook Course Application", ["Optin","Upsell","Order","Thank You"], "demo/ebook-course/"),
]

v2_url_map = {
    "v2_make_money_online": {"optin":"https://demonavigator.com/demo/money-online/index.html","upsell":"https://demonavigator.com/demo/money-online/upsell.html","order":"https://demonavigator.com/demo/money-online/order.html","thank_you":"https://demonavigator.com/demo/money-online/thank-you.html"},
    "v2_vacation": {"optin":"https://demonavigator.com/demo/vacation/","upsell":"https://demonavigator.com/demo/vacation/upsell.html","order":"https://demonavigator.com/demo/vacation/orderpage.html","thank_you":"https://demonavigator.com/demo/vacation/thankyou.html"},
    "v2_green_tea": {"optin":"https://demonavigator.com/demo/green-tea-v2/","upsell":"https://demonavigator.com/demo/green-tea-v2/upsell.html","upsell2":"https://demonavigator.com/demo/green-tea-v2/upsell1.html","thank_you":"https://demonavigator.com/demo/green-tea-v2/thank-you.html"},
    "v2_dog_food": {"optin":"https://demonavigator.com/demo/dog-food/","upsell":"https://demonavigator.com/demo/dog-food/upsell1.html","upsell2":"https://demonavigator.com/demo/dog-food/upsell2.html","thank_you":"https://demonavigator.com/demo/dog-food/orderconfirmation.html"},
    "v2_beauty_product": {"optin":"https://demonavigator.com/demo/selflove-beauty-product/","oto":"https://demonavigator.com/demo/selflove-beauty-product/oto.html","downsell":"https://demonavigator.com/demo/selflove-beauty-product/downsell.html","thank_you":"https://demonavigator.com/demo/selflove-beauty-product/thankyou.html"},
    "v2_entrepreneurs": {"optin":"https://demonavigator.com/demo/entrepreneurs/index.html","upsell":"https://demonavigator.com/demo/entrepreneurs/upsell.html","order":"https://demonavigator.com/demo/entrepreneurs/order.html","thank_you":"https://demonavigator.com/demo/entrepreneurs/thank-you.html"},
    "v2_business_consultant": {"optin":"https://demonavigator.com/demo/business-consultant-application/index.html","oto":"https://demonavigator.com/demo/business-consultant-application/oto.html","order":"https://demonavigator.com/demo/business-consultant-application/order.html","thank_you":"https://demonavigator.com/demo/business-consultant-application/thank-you.html"},
    "v2_juice": {"optin":"https://demonavigator.com/demo/juice/","upsell":"https://demonavigator.com/demo/juice/upsell1.html","order":"https://demonavigator.com/demo/juice/order.html","thank_you":"https://demonavigator.com/demo/juice/thank-you.html"},
    "v2_nutritionist": {"optin":"https://demonavigator.com/demo/nutritionist/","upsell":"https://demonavigator.com/demo/nutritionist/upsell.html","order":"https://demonavigator.com/demo/nutritionist/order.html","thank_you":"https://demonavigator.com/demo/nutritionist/thank-you.html"},
    "v2_ebook_course": {"optin":"https://demonavigator.com/demo/ebook-course/","upsell":"https://demonavigator.com/demo/ebook-course/upsell.html","order":"https://demonavigator.com/demo/ebook-course/order.html","thank_you":"https://demonavigator.com/demo/ebook-course/thank-you.html"},
}

v2_names = {
    "v2_make_money_online": "Make Money Online Summit Funnel",
    "v2_vacation": "Vacation Booking Application Funnel",
    "v2_green_tea": "Green Tea Supplement Summit Funnel",
    "v2_dog_food": "Dog Food Summit Funnel",
    "v2_beauty_product": "Self-Love Beauty Product Summit Funnel",
    "v2_entrepreneurs": "Entrepreneurs Webinar Application Funnel",
    "v2_business_consultant": "Business Consultant Application Funnel",
    "v2_juice": "Juice Product Application Funnel",
    "v2_nutritionist": "Professional Nutritionist Application Funnel",
    "v2_ebook_course": "Ebook Course Application Funnel",
}

for pid, name, pages, base in v2_demos:
    patterns.append(make(pid, v2_names.get(pid, name), f"10 demo from Funnel Templates V2 — {v2_names.get(pid, name)}. {len(pages)}-page funnel.",
                        v2_url_map.get(pid, {}), ["v2", pid.replace("v2_","")]))

###############################################################################
# V3 — 10 funnels
###############################################################################
v3_url_map = {
    "v3_business_coaching": {"optin":"https://demonavigator.com/demo/business-coaching-consulting/index.html","upsell":"https://demonavigator.com/demo/business-coaching-consulting/upsell.html","order":"https://demonavigator.com/demo/business-coaching-consulting/order.html","thank_you":"https://demonavigator.com/demo/business-coaching-consulting/order-confirmation.html"},
    "v3_hotel_guest": {"optin":"https://demonavigator.com/demo/get-hotel-guest/","upsell":"https://demonavigator.com/demo/get-hotel-guest/oto.html","order":"https://demonavigator.com/demo/get-hotel-guest/order.html","thank_you":"https://demonavigator.com/demo/get-hotel-guest/thankyou.html"},
    "v3_music_concert": {"optin":"https://demonavigator.com/demo/musicevent/","upsell":"https://demonavigator.com/demo/musicevent/oto.html","order":"https://demonavigator.com/demo/musicevent/order.html","thank_you":"https://demonavigator.com/demo/musicevent/thankyou.html"},
    "v3_design_agency": {"optin":"https://demonavigator.com/demo/design-agency/","upsell":"https://demonavigator.com/demo/design-agency/upsell.html","order":"https://demonavigator.com/demo/design-agency/order.html","thank_you":"https://demonavigator.com/demo/design-agency/thank-you.html"},
    "v3_online_courses": {"optin":"https://demonavigator.com/demo/onlinecourses/index.html","upsell":"https://demonavigator.com/demo/onlinecourses/upsell.html","order":"https://demonavigator.com/demo/onlinecourses/order.html","thank_you":"https://demonavigator.com/demo/onlinecourses/thankyou.html"},
    "v3_get_loan": {"optin":"https://demonavigator.com/demo/get-loan/","order":"https://demonavigator.com/demo/get-loan/order.html","thank_you":"https://demonavigator.com/demo/get-loan/thank-you.html","cancel":"https://demonavigator.com/demo/get-loan/order-cancelled.html"},
    "v3_startup": {"optin":"https://demonavigator.com/demo/startup/","upsell":"https://demonavigator.com/demo/startup/leadership.html","order":"https://demonavigator.com/demo/startup/order.html","thank_you":"https://demonavigator.com/demo/startup/thank-you.html"},
    "v3_tax_advisor": {"optin":"https://demonavigator.com/demo/tax-advisor-consultant/","upsell":"https://demonavigator.com/demo/tax-advisor-consultant/oto.html","order":"https://demonavigator.com/demo/tax-advisor-consultant/order.html","thank_you":"https://demonavigator.com/demo/tax-advisor-consultant/thank-you.html"},
    "v3_software_launch": {"optin":"https://demonavigator.com/demo/software-product-launch/","upsell":"https://demonavigator.com/demo/software-product-launch/video_1.html","order":"https://demonavigator.com/demo/software-product-launch/video_4.html","thank_you":"https://demonavigator.com/demo/software-product-launch/thankyou.html"},
    "v3_keto": {"optin":"https://demonavigator.com/demo/ketto/","upsell":"https://demonavigator.com/demo/ketto/oto.html","downsell":"https://demonavigator.com/demo/ketto/downsell.html","thank_you":"https://demonavigator.com/demo/ketto/thankyou.html"},
}

v3_names = {
    "v3_business_coaching": "Business Coaching & Consulting Summit Funnel",
    "v3_hotel_guest": "Hotel Guest / Tenant for Rental Homes Application Funnel",
    "v3_music_concert": "Music Concert Summit Funnel",
    "v3_design_agency": "Design Agency Summit Funnel",
    "v3_online_courses": "Online Courses Summit Funnel",
    "v3_get_loan": "Get Loan 10X Faster Application Funnel",
    "v3_startup": "Service-Based Startup Application Funnel",
    "v3_tax_advisor": "Tax Advisor Consultant Application Funnel",
    "v3_software_launch": "Software Product Launch Application Funnel",
    "v3_keto": "Keto Weight Loss Application Funnel",
}

for pid, name in v3_names.items():
    patterns.append(make(pid, name, f"10 demo from Funnel Templates V3 — {name}.", v3_url_map.get(pid, {}), ["v3", pid.replace("v3_","")]))

###############################################################################
# V4 — 10 funnels
###############################################################################
v4_url_map = {
    "v4_book_funnel": {"optin":"https://demonavigator.com/demo/book-funnel/","about":"https://demonavigator.com/demo/book-funnel/about.html","order":"https://demonavigator.com/demo/book-funnel/order.html","thank_you":"https://demonavigator.com/demo/book-funnel/thank-you.html"},
    "v4_download_ebook": {"optin":"https://demonavigator.com/demo/download-the-ebook/","upsell":"https://demonavigator.com/demo/download-the-ebook/upsell.html","downsell":"https://demonavigator.com/demo/download-the-ebook/downsell.html","order":"https://demonavigator.com/demo/download-the-ebook/order.html"},
    "v4_n95_mask": {"optin":"https://demonavigator.com/demo/n-95-mask/","upsell":"https://demonavigator.com/demo/n-95-mask/upsell.html","downsell":"https://demonavigator.com/demo/n-95-mask/downsell.html","order":"https://demonavigator.com/demo/n-95-mask/order.html"},
    "v4_music_era": {"optin":"https://demonavigator.com/demo/new-music-era/","upsell":"https://demonavigator.com/demo/new-music-era/upsell.html","downsell":"https://demonavigator.com/demo/new-music-era/downsell.html","order":"https://demonavigator.com/demo/new-music-era/order.html"},
    "v4_online_course": {"optin":"https://demonavigator.com/demo/online-course/","upsell":"https://demonavigator.com/demo/online-course/upsell.html","downsell":"https://demonavigator.com/demo/online-course/downsell.html","order":"https://demonavigator.com/demo/online-course/order.html"},
    "v4_organic_store": {"optin":"https://demonavigator.com/demo/organic-store/","sales":"https://demonavigator.com/demo/organic-store/sales-page.html","order":"https://demonavigator.com/demo/organic-store/order.html","thank_you":"https://demonavigator.com/demo/organic-store/thank-you.html"},
    "v4_roofing_agency": {"optin":"https://demonavigator.com/demo/roofing-agency/","terms":"https://demonavigator.com/demo/roofing-agency/terms-and-conditions.html","thank_you":"https://demonavigator.com/demo/roofing-agency/thank-you.html","error":"https://demonavigator.com/demo/roofing-agency/error.html"},
    "v4_web_form": {"optin":"https://demonavigator.com/demo/web-form/","terms":"https://demonavigator.com/demo/web-form/terms-and-conditions.html","thank_you":"https://demonavigator.com/demo/web-form/thank-you.html","error":"https://demonavigator.com/demo/web-form/error.html"},
    "v4_working_space": {"optin":"https://demonavigator.com/demo/working-space/","upsell":"https://demonavigator.com/demo/working-space/upsell.html","downsell":"https://demonavigator.com/demo/working-space/downsell.html","thank_you":"https://demonavigator.com/demo/working-space/thank-you.html"},
    "v4_yoga": {"optin":"https://demonavigator.com/demo/yoga/","upsell":"https://demonavigator.com/demo/yoga/upsell.html","downsell":"https://demonavigator.com/demo/yoga/downsell.html","order":"https://demonavigator.com/demo/yoga/order.html"},
}

v4_names = {
    "v4_book_funnel": "Book Funnel — Author Landing & Order Pages",
    "v4_download_ebook": "Download the eBook Funnel",
    "v4_n95_mask": "N-95 Mask Product Summit Funnel",
    "v4_music_era": "New Music Era Summit Funnel",
    "v4_online_course": "Online Courses Summit Funnel",
    "v4_organic_store": "Organic Store Sales Funnel",
    "v4_roofing_agency": "Roofing Agency Application Funnel",
    "v4_web_form": "Web Form Application Funnel",
    "v4_working_space": "Working Space Summit Funnel",
    "v4_yoga": "Yoga Summit Funnel",
}

for pid, name in v4_names.items():
    patterns.append(make(pid, name, f"10 demo from Funnel Templates V4 — {name}.", v4_url_map.get(pid, {}), ["v4", pid.replace("v4_","")]))

###############################################################################
# V5 — 10 funnels
###############################################################################
v5_url_map = {
    "v5_saas_success": {"optin":"https://demonavigator.com/demo/saas-success/","thank_you":"https://demonavigator.com/demo/saas-success/thank-you.html","terms":"https://demonavigator.com/demo/saas-success/terms-and-conditions.html","privacy":"https://demonavigator.com/demo/saas-success/privacy-policy.html"},
    "v5_herbal_shampoo": {"optin":"https://demonavigator.com/demo/herbal-shampoo/","upsell":"https://demonavigator.com/demo/herbal-shampoo/upsell.html","downsell":"https://demonavigator.com/demo/herbal-shampoo/downsell.html","order":"https://demonavigator.com/demo/herbal-shampoo/order.html"},
    "v5_freelance_copywriter": {"optin":"https://demonavigator.com/demo/freelance-copywriter/","thank_you":"https://demonavigator.com/demo/freelance-copywriter/thank-you.html","privacy":"https://demonavigator.com/demo/freelance-copywriter/privacy-policy.html","terms":"https://demonavigator.com/demo/freelance-copywriter/terms-and-conditions.html"},
    "v5_beer_launch": {"optin":"https://demonavigator.com/demo/beer-launch/","upsell":"https://demonavigator.com/demo/beer-launch/upsell.html","downsell":"https://demonavigator.com/demo/beer-launch/downsell.html","order":"https://demonavigator.com/demo/beer-launch/order.html"},
    "v5_healthy_green_tea": {"optin":"https://demonavigator.com/demo/healthy-green-tea/","upsell":"https://demonavigator.com/demo/healthy-green-tea/upsell1.html","downsell":"https://demonavigator.com/demo/healthy-green-tea/upsell2.html","order":"https://demonavigator.com/demo/healthy-green-tea/order.html"},
    "v5_health_planer": {"optin":"https://demonavigator.com/demo/health-planer/","order":"https://demonavigator.com/demo/health-planer/order.html","sales":"https://demonavigator.com/demo/health-planer/sales-page.html","thank_you":"https://demonavigator.com/demo/health-planer/thank-you.html"},
    "v5_mental_health": {"optin":"https://demonavigator.com/demo/mental-health-counselling/","upsell":"https://demonavigator.com/demo/mental-health-counselling/upsell.html","downsell":"https://demonavigator.com/demo/mental-health-counselling/downsell.html","order":"https://demonavigator.com/demo/mental-health-counselling/order.html"},
    "v5_law_firm": {"optin":"https://demonavigator.com/demo/law-firm/","thank_you":"https://demonavigator.com/demo/law-firm/thank-you.html","privacy":"https://demonavigator.com/demo/law-firm/privacy-policy.html","terms":"https://demonavigator.com/demo/law-firm/terms-and-conditions.html"},
    "v5_interior_designer": {"optin":"https://demonavigator.com/demo/interior-designer/","thank_you":"https://demonavigator.com/demo/interior-designer/thank-you.html","privacy":"https://demonavigator.com/demo/interior-designer/privacy-policy.html","terms":"https://demonavigator.com/demo/interior-designer/terms-and-conditions.html"},
    "v5_business_coach": {"optin":"https://demonavigator.com/demo/business-coach/","order":"https://demonavigator.com/demo/business-coach/order.html","thank_you":"https://demonavigator.com/demo/business-coach/thank-you.html","cancel":"https://demonavigator.com/demo/business-coach/order-cancelled.html"},
}

v5_names = {
    "v5_saas_success": "SaaS Success Application Funnel",
    "v5_herbal_shampoo": "Herbal Shampoo Product Summit Funnel",
    "v5_freelance_copywriter": "Freelance Copywriter Application Funnel",
    "v5_beer_launch": "Beer Launch Summit Funnel",
    "v5_healthy_green_tea": "Healthy Green Tea Summit Funnel",
    "v5_health_planer": "Health Planer Application Funnel",
    "v5_mental_health": "Mental Health Counselling Summit Funnel",
    "v5_law_firm": "Law Firm Application Funnel",
    "v5_interior_designer": "Interior Designer Application Funnel",
    "v5_business_coach": "Business Coach Application Funnel",
}

for pid, name in v5_names.items():
    patterns.append(make(pid, name, f"10 demo from Funnel Templates V5 — {name}.", v5_url_map.get(pid, {}), ["v5", pid.replace("v5_","")]))

###############################################################################
# V6 — 7 funnels
###############################################################################
v6_url_map = {
    "v6_wet_wipes": {"optin":"https://demonavigator.com/demo/wet-wipes/index.html","sales":"https://demonavigator.com/demo/wet-wipes/sales.html","order":"https://demonavigator.com/demo/wet-wipes/order.html","thank_you":"https://demonavigator.com/demo/wet-wipes/thank-you.html"},
    "v6_crypto": {"optin":"https://demonavigator.com/demo/cryptocurrency/index.html","upsell":"https://demonavigator.com/demo/cryptocurrency/upsell1.html","downsell":"https://demonavigator.com/demo/cryptocurrency/upsell2.html","thank_you":"https://demonavigator.com/demo/cryptocurrency/thank-you.html"},
    "v6_youtube_sales": {"optin":"https://demonavigator.com/demo/dream-client/index.html","order":"https://demonavigator.com/demo/dream-client/order.html","thank_you":"https://demonavigator.com/demo/dream-client/thank-you.html","cancel":"https://demonavigator.com/demo/dream-client/cancelled.html"},
    "v6_trip_reservation": {"optin":"https://demonavigator.com/demo/trip-reservation/index.html","upsell":"https://demonavigator.com/demo/trip-reservation/upsell.html","downsell":"https://demonavigator.com/demo/trip-reservation/downsell.html","order":"https://demonavigator.com/demo/trip-reservation/order.html"},
    "v6_spa_marketing": {"optin":"https://demonavigator.com/demo/spa/index.html","upsell":"https://demonavigator.com/demo/spa/upsell.html","downsell":"https://demonavigator.com/demo/spa/downsell.html","order":"https://demonavigator.com/demo/spa/order.html"},
    "v6_child_care": {"optin":"https://demonavigator.com/demo/childcare-master/index.html","upsell":"https://demonavigator.com/demo/childcare-master/upsell.html","downsell":"https://demonavigator.com/demo/childcare-master/downsell.html","order":"https://demonavigator.com/demo/childcare-master/order.html"},
    "v6_cafe_bar": {"optin":"https://demonavigator.com/demo/cafe-and-bar/index.html","upsell":"https://demonavigator.com/demo/cafe-and-bar/upsell.html","downsell":"https://demonavigator.com/demo/cafe-and-bar/downsell.html","order":"https://demonavigator.com/demo/cafe-and-bar/order.html"},
}

v6_names = {
    "v6_wet_wipes": "Wet Wipes Beauty Product Funnel",
    "v6_crypto": "Crypto Business Summit Funnel",
    "v6_youtube_sales": "YouTube Dream Client Sales Funnel",
    "v6_trip_reservation": "Trip Reservation Summit Funnel",
    "v6_spa_marketing": "Spa Marketing Summit Funnel",
    "v6_child_care": "Child Care Services Summit Funnel",
    "v6_cafe_bar": "Cafe & Bar Launch Summit Funnel",
}

for pid, name in v6_names.items():
    patterns.append(make(pid, name, f"7 demo from Funnel Templates V6 — {name}.", v6_url_map.get(pid, {}), ["v6", pid.replace("v6_","")]))

###############################################################################
# V7 — 9 funnels
###############################################################################
v7_url_map = {
    "v7_travel_tycoons": {"optin":"https://demonavigator.com/demo/travel-tycoons/","upsell":"https://demonavigator.com/demo/travel-tycoons/upsell.html","downsell":"https://demonavigator.com/demo/travel-tycoons/downsell.html","order":"https://demonavigator.com/demo/travel-tycoons/order.html"},
    "v7_ice_cream": {"optin":"https://demonavigator.com/demo/ice-cream/","upsell":"https://demonavigator.com/demo/ice-cream/upsell.html","downsell":"https://demonavigator.com/demo/ice-cream/downsell.html","thank_you":"https://demonavigator.com/demo/ice-cream/thank-you.html"},
    "v7_product_pro": {"optin":"https://demonavigator.com/demo/product-pro/","privacy":"https://demonavigator.com/demo/product-pro/privacy-policy.html","terms":"https://demonavigator.com/demo/product-pro/terms-and-conditions.html","thank_you":"https://demonavigator.com/demo/product-pro/thank-you.html"},
    "v7_portfolio_pro": {"optin":"https://demonavigator.com/demo/portfolio-pro/","order":"https://demonavigator.com/demo/portfolio-pro/order.html","upsell":"https://demonavigator.com/demo/portfolio-pro/upsell.html","downsell":"https://demonavigator.com/demo/portfolio-pro/downsell.html"},
    "v7_music_magic": {"optin":"https://demonavigator.com/demo/music-magic/","order":"https://demonavigator.com/demo/music-magic/order.html","upsell":"https://demonavigator.com/demo/music-magic/upsell.html","downsell":"https://demonavigator.com/demo/music-magic/downsell.html"},
    "v7_management_marvel": {"optin":"https://demonavigator.com/demo/management-marvel/","order":"https://demonavigator.com/demo/management-marvel/order.html","upsell":"https://demonavigator.com/demo/management-marvel/upsell.html","downsell":"https://demonavigator.com/demo/management-marvel/downsell.html"},
    "v7_theatre_titan": {"optin":"https://demonavigator.com/demo/theatre-titan/","order":"https://demonavigator.com/demo/theatre-titan/order.html","upsell":"https://demonavigator.com/demo/theatre-titan/upsell.html","downsell":"https://demonavigator.com/demo/theatre-titan/downsell.html"},
    "v7_virtual_connect": {"optin":"https://demonavigator.com/demo/virtual-connect/","privacy":"https://demonavigator.com/demo/virtual-connect/privacy-policy.html","terms":"https://demonavigator.com/demo/virtual-connect/terms-and-conditions.html","thank_you":"https://demonavigator.com/demo/virtual-connect/thank-you.html"},
    "v7_digital_programmer": {"optin":"https://demonavigator.com/demo/digital-programmers/","privacy":"https://demonavigator.com/demo/digital-programmers/privacy-policy.html","terms":"https://demonavigator.com/demo/digital-programmers/terms-and-conditions.html","thank_you":"https://demonavigator.com/demo/digital-programmers/thank-you.html"},
}

v7_names = {
    "v7_travel_tycoons": "Travel Tycoons Tripwire Funnel",
    "v7_ice_cream": "Ice Cream Service-Based Sales Funnel",
    "v7_product_pro": "Product Pro Sales Funnel",
    "v7_portfolio_pro": "Portfolio Pro Summit Funnel",
    "v7_music_magic": "Music Magic Webinar Funnel",
    "v7_management_marvel": "Management Marvel Application Funnel",
    "v7_theatre_titan": "Theatre Titan Application Funnel",
    "v7_virtual_connect": "Virtual Connect Application Funnel",
    "v7_digital_programmer": "Digital Programmer Application Funnel",
}

for pid, name in v7_names.items():
    patterns.append(make(pid, name, f"9 demo from Funnel Templates V7 — {name}.", v7_url_map.get(pid, {}), ["v7", pid.replace("v7_","")]))

###############################################################################
# Merge with existing and write
###############################################################################
patterns_path = os.path.join(DATA_DIR, "patterns.json")

existing = []
if os.path.exists(patterns_path):
    with open(patterns_path) as f:
        existing = json.load(f)

existing_ids = {p['pattern_id'] for p in existing}
new_count = 0
replace_count = 0

for np in patterns:
    if np['pattern_id'] in existing_ids:
        existing = [p for p in existing if p['pattern_id'] != np['pattern_id']]
        replace_count += 1
    else:
        new_count += 1

all_patterns = existing + patterns
with open(patterns_path, 'w') as f:
    json.dump(all_patterns, f, indent=2, ensure_ascii=False)

print(f"Written {len(all_patterns)} total patterns")
print(f"Added {new_count} new + {replace_count} replaced")
print(f"V2 added: {len(v2_names)}, V3: {len(v3_names)}, V4: {len(v4_names)}, V5: {len(v5_names)}, V6: {len(v6_names)}, V7: {len(v7_names)}")
print(f"Total in this batch: {len(patterns)}")

# Also save the batch URLs for screenshotting
import os
screenshot_dir = os.path.join(os.path.dirname(__file__), 'screenshots')
os.makedirs(screenshot_dir, exist_ok=True)

with open(os.path.join(screenshot_dir, 'batch_urls_v2_v7.txt'), 'w') as f:
    for p in patterns:
        pid = p['pattern_id']
        for pname, purl in p.get('pages', {}).items():
            # Determine folder: v2/money-online, v3/business-coaching, etc.
            # Use first part of pattern_id after v?_
            parts = pid.split('_', 1)
            folder = parts[1] if len(parts) > 1 else pid
            f.write(f"{folder}|{pname}|{purl}\n")

print(f"Saved {sum(len(p.get('pages',{})) for p in patterns)} URLs for batch screenshotting")