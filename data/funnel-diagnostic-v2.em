note FUNNEL DIAGNOSTIC ENGINE v2 — EventMath v2.3
note Every condition passes through directions x lenses x quantities

note ── DIRECTIONS (how to approach) ──
event direct direction
category compass
matter name is direct description is same cause same effect polarity is positive
end
end

event indirect opposite
category compass
matter name is indirect opposite description is inversion polarity is negative
end
end

event indirect other
category compass
matter name is indirect other description is different path polarity is lateral
end
end

event keep same
category compass
matter name is keep same description is no change polarity is neutral
end
end

event more same
category compass
matter name is more same description is amplify polarity is amplified
end
end

event less same
category compass
matter name is less same description is diminish polarity is diminished
end
end

layer directions
  direct direction
  indirect opposite
  indirect other
  keep same
  more same
  less same
end

note ── LENSES (which dimension) ──
event who lens
category lens
matter name is who description is people dimension focus is agent
end
end

event what lens
category lens
matter name is what description is object dimension focus is thing
end
end

event place lens
category lens
matter name is where description is location dimension focus is place
end
end

event time lens
category lens
matter name is when description is timing dimension focus is sequence
end
end

event why lens
category lens
matter name is why description is cause dimension focus is motivation
end
end

event how lens
category lens
matter name is how description is method dimension focus is mechanism
end
end

layer lenses
  who lens
  what lens
  place lens
  time lens
  why lens
  how lens
end

note ── QUANTITIES (how much) ──
event small quantity
category quantity
matter name is small description is low amount range is 1 to 10
end
end

event medium quantity
category quantity
matter name is medium description is medium amount range is 10 to 100
end
end

event large quantity
category quantity
matter name is large description is high amount range is 100 to 1000
end
end

event very large quantity
category quantity
matter name is very large description is very high amount range is 1000 plus
end
end

layer quantities
  small quantity
  medium quantity
  large quantity
  very large quantity
end

note ── INDUSTRIES ──
event healthcare
category industry
matter kind is healthcare need is trust price range is 200 to 5000
end
end

event ecommerce
category industry
matter kind is ecommerce need is convenience price range is 20 to 200
end
end

event saas
category industry
matter kind is saas need is efficiency price range is 10 to 200
end
end

event coaching
category industry
matter kind is coaching need is transformation price range is 500 to 5000
end
end

event education
category industry
matter kind is education need is knowledge price range is 50 to 1000
end
end

layer industries
  healthcare
  ecommerce
  saas
  coaching
  education
end

note ── PRICE TIERS ──
event free tier
category price
matter kind is free barrier is none commitment is very low
end
end

event low tier
category price
matter kind is low range is 1 to 50 barrier is low commitment is low
end
end

event medium tier
category price
matter kind is medium range is 51 to 200 barrier is medium commitment is medium
end
end

event high tier
category price
matter kind is high range is 201 to 1000 barrier is high commitment is high
end
end

event premium tier
category price
matter kind is premium range is 1001 to 5000 barrier is very high commitment is very high
end
end

layer prices
  free tier
  low tier
  medium tier
  high tier
  premium tier
end

note ── AWARENESS LEVELS ──
event unaware
category awareness
matter kind is unaware knows problem is no headline type is curiosity
end
end

event problem aware
category awareness
matter kind is problem aware knows problem is yes knows solution is no headline type is pain
end
end

event solution aware
category awareness
matter kind is solution aware knows problem is yes knows solution is yes headline type is benefit
end
end

event product aware
category awareness
matter kind is product aware knows product is yes headline type is social proof
end
end

layer awareness levels
  unaware
  problem aware
  solution aware
  product aware
end

note ── FUNNEL TYPES (output) ──
event tripwire
category funnel type
matter kind is tripwire pages is 4 entry is free offer money is free then upsell
end
end

event application
category funnel type
matter kind is application pages is 4 entry is apply money is high ticket
end
end

event summit
category funnel type
matter kind is summit pages is 4 entry is register money is free then paid
end
end

event webinar
category funnel type
matter kind is webinar pages is 6 entry is content gate money is free then upsell
end
end

event subscription
category funnel type
matter kind is subscription pages is 5 entry is free trial money is recurring
end
end

event quiz
category funnel type
matter kind is quiz pages is 5 entry is quiz money is free then upsell
end
end

layer funnel types
  tripwire
  application
  summit
  webinar
  subscription
  quiz
end

note ── CHAIN ANALYSIS ──
note Each industry passes through 3-axis filter to generate funnel recommendations

chain healthcare funnel
  healthcare leads to application funnel at value 90
  healthcare leads to quiz funnel at value 10
end

chain ecommerce funnel
  ecommerce leads to tripwire funnel at value 70
  ecommerce leads to quiz funnel at value 30
end

chain saas funnel
  saas leads to subscription funnel at value 60
  saas leads to webinar funnel at value 40
end

chain coaching funnel
  coaching leads to application funnel at value 40
  coaching leads to webinar funnel at value 30
  coaching leads to subscription funnel at value 20
  coaching leads to quiz funnel at value 10
end

chain education funnel
  education leads to summit funnel at value 50
  education leads to webinar funnel at value 30
  education leads to subscription funnel at value 20
end

note ── ELEMENT SELECTION BY AWARENESS ──
note Pass awareness through 3-axis filter to select headline type

chain headline selector
  problem aware leads to pain headline at value 85
  problem aware leads to question headline at value 15
  solution aware leads to benefit headline at value 70
  solution aware leads to comparison headline at value 30
  product aware leads to social proof headline at value 60
  product aware leads to feature headline at value 40
  unaware leads to curiosity headline at value 70
  unaware leads to pain headline at value 30
end

note ── PAGE SELECTION BY PRICE ──
note Pass price through 3-axis filter to select page count and complexity

chain page selector
  free tier leads to minimal at value 80
  free tier leads to standard at value 20
  low tier leads to standard at value 60
  low tier leads to expanded at value 40
  medium tier leads to expanded at value 50
  medium tier leads to standard at value 30
  medium tier leads to full at value 20
  high tier leads to expanded at value 40
  high tier leads to full at value 40
  high tier leads to standard at value 20
  premium tier leads to full at value 60
  premium tier leads to expanded at value 40
end

note ── GENERATE ALL COMBOS ──
note Each dimension passes through the 3-axis filter
note 5 industries x 5 prices x 4 awareness = 100 predictions

predict recommended funnel
across industries
and prices
and awareness levels
into all recommendations

run all recommendations

note ── SHOW ANALYSIS ──
show healthcare funnel
show ecommerce funnel
show saas funnel
show coaching funnel
show education funnel
show headline selector
show page selector