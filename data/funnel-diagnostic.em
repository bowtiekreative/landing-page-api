note FUNNEL DIAGNOSTIC ENGINE — EventMath v2.3
note Maps business conditions to exact funnel architectures
note Compiles and runs as EventMath

note ── CONDITION DIMENSIONS ──
note Each condition is an event with possible values

note INDUSTRY
event healthcare industry
category condition
matter
  kind is healthcare
  needs trust is high
  needs authority is high
  typical price is 200 to 5000
end
end

event ecommerce industry
category condition
matter
  kind is ecommerce
  needs trust is medium
  needs authority is low
  typical price is 20 to 200
end
end

event saas industry
category condition
matter
  kind is saas
  needs trust is high
  needs authority is medium
  typical price is 10 to 200 per month
end
end

event coaching industry
category condition
matter
  kind is coaching
  needs trust is very high
  needs authority is high
  typical price is 500 to 5000
end
end

event education industry
category condition
matter
  kind is education
  needs trust is medium
  needs authority is high
  typical price is 50 to 1000
end
end

layer industries
  healthcare industry
  ecommerce industry
  saas industry
  coaching industry
  education industry
end

note PRICE TIER
event free tier
category price
matter
  kind is free
  range is 0
  commitment is very low
end
end

event low tier
category price
matter
  kind is low
  range is 1 to 50
  commitment is low
end
end

event medium tier
category price
matter
  kind is medium
  range is 50 to 200
  commitment is medium
end
end

event high tier
category price
matter
  kind is high
  range is 200 to 1000
  commitment is high
end
end

event premium tier
category price
matter
  kind is premium
  range is 1000 to 5000
  commitment is very high
end
end

layer prices
  free tier
  low tier
  medium tier
  high tier
  premium tier
end

note AWARENESS
event unaware visitor
category awareness
matter
  kind is unaware
  knows problem is no
  knows solution is no
  needs education is yes
end
end

event problem aware
category awareness
matter
  kind is problem aware
  knows problem is yes
  knows solution is no
  needs education is yes
end
end

event solution aware
category awareness
matter
  kind is solution aware
  knows problem is yes
  knows solution is yes
  needs best option is yes
end
end

event product aware
category awareness
matter
  kind is product aware
  knows product is yes
  needs confidence is yes
end
end

layer awareness
  unaware visitor
  problem aware
  solution aware
  product aware
end

note ── FUNNEL ARCHITECTURES ──
note Each funnel type is an event with its page sequence

event tripwire architecture
category funnel
matter
  kind is tripwire
  page count is 4
  entry is free offer
  complexity is 4 pages
  money model is free then upsell
  exit type is purchase
  branch type is upsell only
  best for is ecommerce and health products
end
end

event application architecture
category funnel
matter
  kind is application
  page count is 4
  entry is apply
  complexity is 4 pages
  money model is high ticket
  exit type is appointment
  branch type is upsell only
  best for is healthcare and coaching and services
end
end

event summit architecture
category funnel
matter
  kind is summit
  page count is 4
  entry is summit register
  complexity is 4 pages
  money model is free then paid
  exit type is purchase
  branch type is upsell and downsell
  best for is events and courses
end
end

event webinar architecture
category funnel
matter
  kind is webinar
  page count is 6
  entry is content gate
  complexity is full
  money model is free then upsell
  exit type is purchase
  branch type is multi
  best for is coaching and courses and saas
end
end

event subscription architecture
category funnel
matter
  kind is subscription
  page count is 5
  entry is free trial
  complexity is full
  money model is recurring
  exit type is trial conversion
  branch type is upsell only
  best for is saas and membership and coaching
end
end

event quiz architecture
category funnel
matter
  kind is quiz
  page count is 5
  entry is quiz
  complexity is full
  money model is free then upsell
  exit type is purchase
  branch type is upsell and downsell
  best for is ecommerce and coaching and health
end
end

layer funnels
  tripwire architecture
  application architecture
  summit architecture
  webinar architecture
  subscription architecture
  quiz architecture
end

note ── DECISION CHAIN ──
note Maps condition combinations to funnel choices

chain funnel selector
  healthcare industry leads to application architecture at value 90
  healthcare industry leads to quiz architecture at value 10
  ecommerce industry leads to tripwire architecture at value 70
  ecommerce industry leads to quiz architecture at value 30
  saas industry leads to subscription architecture at value 60
  saas industry leads to webinar architecture at value 40
  coaching industry leads to application architecture at value 40
  coaching industry leads to webinar architecture at value 30
  coaching industry leads to subscription architecture at value 20
  coaching industry leads to quiz architecture at value 10
  education industry leads to summit architecture at value 50
  education industry leads to webinar architecture at value 30
  education industry leads to subscription architecture at value 20
end

show funnel selector

note ── DETAILED MAPPING ──
note For each condition, show the recommended funnel with page breakdown

note Healthcare + High Price + Problem Aware → Application Funnel
chain healthcare application
  healthcare industry leads to application architecture at value 90
  high tier leads to full page count at value 100
  problem aware leads to pain hero at value 85
  application architecture leads to landing page at value 100
  landing page leads to hero with pain headline at value 100
  landing page leads to benefit grid at value 90
  landing page leads to doctor credentials at value 85
  landing page leads to testimonial section at value 80
  landing page leads to faq section at value 75
  landing page leads to free consult cta at value 95
  application page leads to contact form at value 100
  application page leads to service selection at value 90
  application page leads to submit button at value 100
  appointment confirmed leads to phone cta at value 95
  appointment confirmed leads to one more offer at value 70
end

chain ecommerce tripwire
  ecommerce industry leads to tripwire architecture at value 70
  medium tier leads to low risk offer at value 85
  solution aware leads to benefit bullets at value 90
  tripwire architecture leads to optin page at value 100
  optin page leads to hero with product at value 100
  optin page leads to countdown timer at value 80
  optin page leads to testimonial grid at value 75
  optin page leads to review cards at value 70
  upsell page leads to value stack at value 90
  upsell page leads to strikethrough price at value 95
  upsell page leads to decline link at value 100
  order page leads to billing form at value 100
  order page leads to payment selection at value 100
  order page leads to order bump at value 60
  thank you leads to facebook group at value 80
end

chain saas subscription
  saas industry leads to subscription architecture at value 60
  low tier leads to trial offer at value 85
  solution aware leads to feature showcase at value 90
  subscription architecture leads to landing page at value 100
  landing page leads to feature grid at value 95
  landing page leads to pricing table at value 90
  landing page leads to testimonials at value 80
  landing page leads to trial cta at value 95
  onboarding leads to welcome email at value 100
  onboarding leads to first action prompt at value 85
  retention leads to value reminder at value 75
  retention leads to upgrade offer at value 40
end

show healthcare application
show ecommerce tripwire
show saas subscription

note ── PREDICT ALL COMBINATIONS ──
note 5 industries x 5 prices x 4 awareness = 100 combinations
predict funnel match
across industries
and prices
and awareness
into all matches

run all matches