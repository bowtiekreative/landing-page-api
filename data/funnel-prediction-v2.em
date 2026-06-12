note ============================================
note FUNNEL LANDSCAPE PREDICTION MODEL v2.0
note Enumerates every valid funnel architecture
note Uses EventMath prediction engine
note ============================================

note ##########
note DIMENSION 1: ENTRY
note ##########

event free offer
category entry
matter
  name is free offer
  barrier is email
  value is $0
end
end

event paid product
category entry
matter
  name is paid product
  barrier is payment
  value is $XX
end
end

event summit register
category entry
matter
  name is summit register
  barrier is form
  value is $0
end
end

event apply
category entry
matter
  name is apply
  barrier is form
  callback is required
end
end

event content gate
category entry
matter
  name is content gate
  barrier is email
  value is $0
end
end

event quiz
category entry
matter
  name is quiz
  barrier is answers
  personalization is high
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

note ##########
note DIMENSION 2: COMPLEXITY
note ##########

event minimal
category complexity
matter
  name is minimal
  pages is 2
end
end

event standard
category complexity
matter
  name is standard
  pages is 3
end
end

event expanded
category complexity
matter
  name is expanded
  pages is 4
end
end

event complex
category complexity
matter
  name is complex
  pages is 5 plus
end
end

layer complexities
  minimal
  standard
  expanded
  complex
end

note ##########
note DIMENSION 3: MONEY
note ##########

event donation
category money
matter
  name is donation
  model is voluntary
end
end

event one time
category money
matter
  name is one time
  model is single payment
end
end

event subscription
category money
matter
  name is subscription
  model is recurring
end
end

event free plus upsell
category money
matter
  name is free plus upsell
  model is entry free then paid
end
end

event tripwire
category money
matter
  name is tripwire
  model is low entry then upsell
end
end

event high ticket
category money
matter
  name is high ticket
  model is application then proposal
end
end

layer moneys
  donation
  one time
  subscription
  free plus upsell
  tripwire
  high ticket
end

note ##########
note DIMENSION 4: EXIT
note ##########

event purchase
category exit
matter
  name is purchase
  outcome is revenue
end
end

event appointment
category exit
matter
  name is appointment
  outcome is callback
end
end

event cancel
category exit
matter
  name is cancel
  outcome is no revenue
end
end

event waitlist
category exit
matter
  name is waitlist
  outcome is future potential
end
end

event community
category exit
matter
  name is community
  outcome is engagement
end
end

event trial
category exit
matter
  name is trial
  outcome is conversion potential
end
end

layer exits
  purchase
  appointment
  cancel
  waitlist
  community
  trial
end

note ##########
note DIMENSION 5: BRANCH
note ##########

event none
category branch
matter
  name is none
  splits is 0
end
end

event upsell only
category branch
matter
  name is upsell only
  splits is 1
end
end

event upsell downsell
category branch
matter
  name is upsell and downsell
  splits is 2
end
end

event multi
category branch
matter
  name is multi
  splits is 3 plus
end
end

layer branches
  none
  upsell only
  upsell downsell
  multi
end

note ##########
note GENERATE ALL PREDICTIONS
note 6 entries x 4 complexities x 6 moneys x 6 exits x 4 branches
note = 3,456 predictions
note ##########

predict funnel architecture
across entries
and complexities
and moneys
and exits
and branches
into all funnel predictions

note ##########
note COUNT BY ENTRY TYPE
note ##########

count in all funnel predictions where entry is free offer into free offer count
count in all funnel predictions where entry is paid product into paid count
count in all funnel predictions where entry is summit register into summit count
count in all funnel predictions where entry is apply into apply count
count in all funnel predictions where entry is content gate into content gate count
count in all funnel predictions where entry is quiz into quiz count

note ##########
note FAMILY CLASSIFICATION
note ##########

count in all funnel predictions where entry is free offer into tripwire family
count in all funnel predictions where complexity is expanded into expanded family
count in all funnel predictions where money is tripwire into tripwire money

count in all funnel predictions where money is free plus upsell into summit money
count in all funnel predictions where money is high ticket into high ticket money
count in all funnel predictions where entry is content gate into content gate family
count in all funnel predictions where branch is multi into multi branch family
count in all funnel predictions where money is subscription into subscription money
count in all funnel predictions where exit is trial into trial exits
count in all funnel predictions where exit is waitlist into waitlist family

note ##########
note OUTPUT
note ##########

run all funnel predictions