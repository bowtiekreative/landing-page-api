# Funnel Landscape — Modeled in EventMath
#
# Every funnel IS a timeline.
# Pages are events.
# Page sequences are layers.
# Branches (upsell/downsell/skip) are split/path.
# Customer data is matter flowing through doors.
# Past = what the user saw. Present = where they are. Future = where they go.

# ==========================================
# DIMENSION 1: ENTRY EVENTS (How the user enters)
# ==========================================

# Type A: Free Offer Entry
event free optin
category entry
matter
  offer type is lead magnet       # ebook, checklist, video, webinar, trial
  value at entry is $0
  commitment is low
end

# Type B: Direct Purchase Entry
event direct purchase
category entry
matter
  offer type is product           # physical, digital, course, subscription
  value at entry is $XX
  commitment is high
end

# Type C: Event / Summit Entry
event summit registration
category entry
matter
  offer type is free ticket
  value at entry is $0
  barrier is registration form
end

# Type D: Service Application Entry
event service apply
category entry
matter
  offer type is consultation      # healthcare, coaching, legal
  value at entry is $0
  barrier is application form
  callback required is true
end

# Type E: Content Gate Entry
event content gate
category entry
matter
  offer type is video/article
  gate type is email required
  value at entry is $0
end

# ==========================================
# DIMENSION 2: COMMITMENT LADDER EVENTS (Progressive commitment)
# ==========================================

event bridge page
category commitment
matter
  purpose is warm up              # builds value before offer
  content type is story/video
  timing is after optin
end

event video sales letter
category commitment
matter
  purpose is demonstrate value
  duration is 5-60 minutes
  triggers is emotional/pain/desire
end

event upsell
category commitment
matter
  offer value is $XX
  discount is 50%                 # universal pattern
  timing is before order
  decline path is downsell or order
end

event downsell
category commitment
matter
  offer value is lower than upsell
  discount is deeper than upsell
  timing is after upsell decline
  decline path is order or thank you
end

event order bump
category commitment
matter
  offer value is $X-$XX
  placement is inside checkout
  decline path is complete order
end

event cross sell
category commitment
matter
  offer value is $XX
  placement is after order
  decline path is thank you
end

event order page
category commitment
matter
  fields required is billing info
  payment methods is paypal or card
  action is submit payment
end

event appointment confirm
category commitment
matter
  fields required is contact info
  callback window is 24 hours
  upsell offer is separate
end

event thank you
category commitment
matter
  confirmation type is purchase or booking
  upsell path is cross sell or none
  community cta is facebook link
end

event cancel page
category commitment
matter
  message type is confirmation
  charge reversal is confirmed
end

event privacy terms
category commitment
matter
  content type is legal
  requirement is compliance
end

# ==========================================
# DIMENSION 3: BRANCH TYPES (Split paths)
# ==========================================

# Every upsell/downsell creates a SPLIT:
# Path A: Accept → next stage
# Path B: Decline → alternative path

split upsell decision into
  path accepted
    # user goes to order or next upsell
  end
  path declined
    # user goes to downsell or order
  end
end

split downsell decision into
  path accepted
    # user goes to order
  end
  path declined
    # user goes to order or thank you
  end
end

split order outcome into
  path completed
    # user goes to thank you
  end
  path cancelled
    # user goes to cancel page or upsell recover
  end
end

# ==========================================
# DIMENSION 4: FUNNEL ARCHITECTURES (Timeline combinations)
# ==========================================

# Each funnel is a timeline defined by its page sequence.
# We can systematically enumerate every valid sequence.

# ---------- 2-PAGE FUNNELS ----------

timeline mini funnel
  # Simplest possible: capture → confirm
  # Used for: email signups, simple downloads
  past
  end
  present
    layer active
      event free optin
    end
  end
  future
    layer planned
      event thank you
    end
  end
end

timeline direct purchase
  # Product sold directly, no lead capture
  # Used for: e-commerce, direct sales
  past
  end
  present
    layer active
      event order page
    end
  end
  future
    layer planned
      event thank you
    end
  end
end

# ---------- 3-PAGE FUNNELS ----------

timeline classic optin funnel
  # Free offer → order → confirm
  # Used for: info products, low-ticket
  past
  end
  present
    layer active
      event free optin
      event order page
    end
  end
  future
    layer planned
      event thank you
    end
  end
end

timeline application funnel
  # Apply → qualify → confirm
  # Used for: services, high-ticket
  past
  end
  present
    layer active
      event service apply
      event appointment confirm
    end
  end
  future
    layer planned
      event thank you
    end
  end
end

timeline summit funnel
  # Register → order (optional) → confirm
  # Used for: events, webinars
  past
  end
  present
    layer active
      event summit registration
      event order page         # optional: paid upgrade
    end
  end
  future
    layer planned
      event thank you
    end
  end
end

timeline content gate
  # Gate → content → order
  # Used for: VSL funnels, educational
  past
  end
  present
    layer active
      event content gate
      event bridge page          # or video sales letter
      event order page
    end
  end
  future
    layer planned
      event thank you
    end
  end
end

# ---------- 4-PAGE FUNNELS (Standard, most common) ----------

timeline tripwire funnel
  # Optin → upsell → order → thank you
  # Used for: physical products, supplements
  # Has tripwire order bump built into order page
  past
  end
  present
    layer capture
      event free optin
    end
    layer tripwire
      event upsell
      event order page
    end
  end
  future
    layer confirm
      event thank you
    end
  end
end

timeline application with upsell
  # Apply → upsell → appointment → thank you
  # Used for: healthcare, coaching (phase 2 funnel)
  past
  end
  present
    layer capture
      event service apply
    end
    layer upsell path
      event upsell
      event appointment confirm
    end
  end
  future
    layer confirm
      event thank you
    end
  end
end

timeline summit with upsell
  # Register → OTO → order → thank you
  # Used for: events, courses (most profitable pattern)
  past
  end
  present
    layer capture
      event summit registration
    end
    layer monetize
      event upsell             # lifetime access offer
      event order page
    end
  end
  future
    layer confirm
      event thank you
    end
  end
end

timeline double upsell funnel
  # Optin → upsell → downsell → order → thank you
  # Used for: high-ticket funnels, aggressive monetization
  past
  end
  present
    layer capture
      event free optin
    end
    layer upsell path
      split upsell decision into
        path accepted
          event order page
        end
        path declined
          event downsell
          split downsell decision into
            path accepted
              event order page
            end
            path declined
              event order page          # goes to base offer
            end
          end
        end
      end
    end
  end
  future
    layer confirm
      event thank you
    end
  end
end

# ---------- 5+ PAGE FUNNELS (Complex) ----------

timeline vsl funnel with bumps
  # Gate → VSL → upsell → order + bumps → thank you + cross-sell
  # Used for: high-ticket info products, launch funnels
  past
  end
  present
    layer gate
      event content gate        # email required for video
    end
    layer educate
      event video sales letter  # 30-60 min presentation
      event bridge page          # recap + urgency
    end
    layer offer
      event upsell              # main product + bonus stack
      event order page          # with order bumps inside
      split order outcome into
        path completed
          # goes to thank you
        end
        path cancelled
          event cancel page     # recovery offer here
        end
      end
    end
  end
  future
    layer confirm
      event thank you
    end
    layer post purchase
      event cross sell           # one more offer
    end
  end
end

timeline multi step application
  # Apply → qualify → upsell → book → confirm → thank you
  # Used for: high-ticket services ($1000+)
  past
  end
  present
    layer entry
      event service apply       # application form
    end
    layer qualify
      event appointment confirm  # discovery call booked
    end
    layer upsell
      event upsell              # upgrade package offer
      split upsell decision into
        path accepted
          event order page
        end
        path declined
          event order page      # base package
        end
      end
    end
  end
  future
    layer confirm
      event thank you
    end
  end
end

timeline webinar funnel
  # Register → remind → attend → replay → buy → thank you
  # Used for: live launches, evergreen webinars
  past
  end
  present
    layer register
      event summit registration  # webinar signup
    end
    layer attend
      event bridge page          # reminder sequence
      event video sales letter   # the actual webinar
    end
    layer offer
      split upsell decision into
        path accepted
          event upsell           # during-webinar offer
          event order page
        end
        path declined
          event downsell         # replay/recording offer
          event order page
        end
      end
    end
  end
  future
    layer confirm
      event thank you
    end
    layer post purchase
      event cross sell
    end
  end
end

# ==========================================
# DIMENSION 5: WHAT'S MISSING
# ==========================================
# 
# From our 71 collected funnels, we have these architectures:
# ✓ Tripwire (optin → upsell → order → thank you)        — 20+ examples
# ✓ Application (apply → upsell → appointment → thank you) — 15+ examples
# ✓ Summit (register → OTO → order → thank you)           — 12+ examples
# ✓ Simple (optin → order → thank you)                    — 10+ examples
#
# MISSING architectures we DON'T have:
#
# ❌ Webinar funnel (register → attend → replay → buy)
# ❌ Multi-step application (apply → qualify → upsell → book → confirm)
# ❌ VSL with bumps (gate → VSL → upsell → order+bump → thank you+cross-sell)
# ❌ Subscription funnel (trial → convert → upgrade → cancel → win-back)
# ❌ Lead magnet → email sequence → sales call funnel
# ❌ Physical product with shipping + tracking + delivery confirmation
# ❌ Membership/community funnel (register → trial → upgrade → renew → lapsed)
# ❌ Survey/quiz funnel (quiz → results → recommendation → order)
# ❌ Cart abandon recovery funnel (add to cart → abandon → email → recover)
# ❌ Contests/sweepstakes funnel (enter → share → refer → winner)
# ❌ Partner/affiliate funnel (apply → approve → promote → commission)
# ❌ Waitlist funnel (join → notify → limited access → full access)
# ❌ Enterprise/SaaS funnel (demo → trial → onboard → subscribe → expand)
# ❌ Physical retail → online funnel (in-store → email → online purchase)
# ❌ Consultation → proposal → close → deliver funnel

# ==========================================
# DIMENSION 6: TOTAL THEORETICAL LANDSCAPE
# ==========================================
#
# Page Types:              15
# Entry Methods:            6
# Branch Points:            5
# Exit States:              4
#
# All possible combinations = 15 × 6 × 5 × 4 = 1800 theoretical funnels
# But most are invalid (wrong order, logical impossibilities)
# Estimated valid funnels: ~200-300
# We have collected:          71
# Coverage:                ~25-35%
# Still missing:          ~130-230
#
# Priority gaps to fill next:
# 1. Webinar / evergreen funnel
# 2. Subscription / membership funnel
# 3. Multi-step high-ticket application
# 4. Survey / quiz → recommendation funnel
# 5. Cart abandonment recovery
# 6. Waitlist → access funnel
# 7. Enterprise demo → trial → onboard
