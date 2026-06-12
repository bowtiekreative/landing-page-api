note FUNNEL PREDICTION MODEL v3 — 3 dimensions for predict

note ENTRY
event free offer
category entry
matter
  kind is free offer
  barrier is email
  start value is 0
end
end

event paid product
category entry
matter
  kind is paid product
  barrier is payment
  start value is XX
end
end

event summit register
category entry
matter
  kind is summit register
  barrier is form
  start value is 0
end
end

event apply
category entry
matter
  kind is apply
  barrier is form
  needs callback is yes
end
end

event content gate
category entry
matter
  kind is content gate
  barrier is email
  start value is 0
end
end

event quiz
category entry
matter
  kind is quiz
  barrier is answers
  personal touch is high
end
end

layer entries
  free offer
  paid product
  summit register
  apply
  content gate
  quiz
end

note COMPLEXITY
event light
category complexity
matter
  kind is light
  page total is 2
end
end

event medium
category complexity
matter
  kind is medium
  page total is 3
end
end

event deep
category complexity
matter
  kind is deep
  page total is 4
end
end

event full
category complexity
matter
  kind is full
  page total is 5 plus
end
end

layer complexities
  light
  medium
  deep
  full
end

note MONEY
event donation
category money
matter
  kind is donation
  pay model is voluntary
end
end

event once
category money
matter
  kind is once
  pay model is single
end
end

event recurring
category money
matter
  kind is recurring
  pay model is subscription
end
end

event free then paid
category money
matter
  kind is free then paid
  pay model is upsell
end
end

event low then upsell
category money
matter
  kind is low then upsell
  pay model is tripwire
end
end

event high ticket
category money
matter
  kind is high ticket
  pay model is proposal
end
end

layer moneys
  donation
  once
  recurring
  free then paid
  low then upsell
  high ticket
end

note GENERATE 6 x 4 x 6 = 144 predictions
predict funnel plan
across entries
and complexities
and moneys
into all predictions

note COUNT RESULTS
count in all predictions where kind is free offer into free offers
count in all predictions where kind is paid product into paid products
count in all predictions where kind is summit register into summit registers
count in all predictions where kind is apply into apply entries
count in all predictions where kind is content gate into content gates
count in all predictions where kind is quiz into quiz entries
count in all predictions where kind is light into light funnels
count in all predictions where kind is medium into medium funnels
count in all predictions where kind is deep into deep funnels
count in all predictions where kind is full into full funnels
count in all predictions where pay model is subscription into subscription plans
count in all predictions where pay model is tripwire into tripwire plans
count in all predictions where pay model is proposal into high ticket plans
count in all predictions where pay model is upsell into upsell plans
count in all predictions where pay model is single into single pay plans
count in all predictions where pay model is voluntary into donation plans

run all predictions