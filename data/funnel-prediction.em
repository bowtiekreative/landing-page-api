note ============================================
note FUNNEL LANDSCAPE PREDICTION MODEL
note Uses EventMath prediction engine to enumerate
note every valid funnel architecture
note ============================================

note ##########
note DIMENSION 1: ENTRY METHODS — how users enter
note ##########

event free offer entry
category entry
matter
  name is free offer
  barrier is email
  value is $0
end
end

event paid product entry
category entry
matter
  name is paid product
  barrier is payment
  value is $XX
end
end

event summit entry
category entry
matter
  name is summit register
  barrier is form
  value is $0
end
end

event application entry
category entry
matter
  name is apply
  barrier is form
  callback is required
end
end

event content gate entry
category entry
matter
  name is content gate
  barrier is email
  value is $0
end
end

event quiz entry
category entry
matter
  name is quiz
  barrier is answers
  personalization is high
end
end

layer entry methods
  free offer entry
  paid product entry
  summit entry
  application entry
  content gate entry
  quiz entry
end

note ##########
note DIMENSION 2: FUNNEL COMPLEXITY — layers/depth
note ##########

event minimal funnel
category complexity
matter
  name is minimal
  page count is 2
  description is capture then confirm
end
end

event standard funnel
category complexity
matter
  name is standard
  page count is 3
  description is capture then offer then confirm
end
end

event expanded funnel
category complexity
matter
  name is expanded
  page count is 4
  description is capture then upsell then order then confirm
end
end

event complex funnel
category complexity
matter
  name is complex
  page count is 5 to 7
  description is multiple upsells bumps and cross-sells
end
end

layer complexities
  minimal funnel
  standard funnel
  expanded funnel
  complex funnel
end

note ##########
note DIMENSION 3: MONETIZATION MODEL
note ##########

event donation model
category monetization
matter
  name is donation
  type is voluntary
end
end

event one time model
category monetization
matter
  name is one time
  type is single payment
end
end

event subscription model
category monetization
matter
  name is subscription
  type is recurring
end
end

event free plus upsell model
category monetization
matter
  name is free plus upsell
  type is entry free then paid
end
end

event tripwire model
category monetization
matter
  name is tripwire
  type is low entry then upsell
end
end

event high ticket model
category monetization
matter
  name is high ticket
  type is application then proposal
end
end

layer monetizations
  donation model
  one time model
  subscription model
  free plus upsell model
  tripwire model
  high ticket model
end

note ##########
note DIMENSION 4: EXIT STATE — how the funnel ends
note ##########

event purchase exit
category exit
matter
  name is purchase
  outcome is revenue
end
end

event appointment exit
category exit
matter
  name is appointment
  outcome is callback
end
end

event cancel exit
category exit
matter
  name is cancel
  outcome is no revenue
end
end

event waitlist exit
category exit
matter
  name is waitlist
  outcome is future potential
end
end

event community exit
category exit
matter
  name is community
  outcome is engagement
end
end

event trial exit
category exit
matter
  name is trial
  outcome is conversion potential
end
end

layer exits
  purchase exit
  appointment exit
  cancel exit
  waitlist exit
  community exit
  trial exit
end

note ##########
note DIMENSION 5: BRANCH TYPE — how decisions split
note ##########

event no branch
category branch
matter
  name is none
  split count is 0
end
end

event upsell only
category branch
matter
  name is upsell only
  split count is 1
end
end

event upsell downsell
category branch
matter
  name is upsell and downsell
  split count is 2
end
end

event multi branch
category branch
matter
  name is multi
  split count is 3 or more
end
end

layer branches
  no branch
  upsell only
  upsell downsell
  multi branch
end

note ##########
note GENERATE ALL PREDICTIONS
note 6 entries × 4 complexities × 6 monetizations × 6 exits × 4 branches
note = 3,456 theoretical combinations
note = ~200-400 valid after constraints applied
note ##########

predict funnel architecture
across entries
and complexities
and monetizations
and exits
and branches
into all funnel predictions

note ##########
note APPLY VALIDITY CONSTRAINTS
note Filter out invalid combinations (e.g., donation + tripwire)
note ##########

note Rule 1: Minimal complexity + upsell branch = invalid (no room)
mark invalid mini upsell as count in all funnel predictions
  where complexity is minimal and branch is upsell only

note Rule 2: Donation + high ticket = invalid
mark invalid donation high as count in all funnel predictions
  where monetization is donation and exit is appointment

note Rule 3: Quiz entry + no branch = miss opportunity
mark quiz no branch as count in all funnel predictions
  where entry is quiz and branch is none

note ##########
note CLASSIFY BY ARCHETYPE
note ##########

note Tripwire family
mark tripwire predictions as count in all funnel predictions
  where entry is free offer
  and complexity is expanded
  and monetization is tripwire

note Summit family
mark summit predictions as count in all funnel predictions
  where entry is summit register
  and complexity is expanded
  and monetization is free plus upsell

note Application family
mark application predictions as count in all funnel predictions
  where entry is apply
  and complexity is expanded
  and monetization is high ticket

note Webinar family (MISSING from our library)
mark webinar predictions as count in all funnel predictions
  where entry is content gate
  and complexity is complex
  and branch is multi

note Subscription family (MISSING from our library)
mark subscription predictions as count in all funnel predictions
  where monetization is subscription
  and exit is trial

note Quiz family (MISSING from our library)
mark quiz predictions as count in all funnel predictions
  where entry is quiz
  and branch is upsell and downsell

note ##########
note OUTPUT RESULTS
note ##########

run all funnel predictions
