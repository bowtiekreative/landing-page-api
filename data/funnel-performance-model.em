note FUNNEL PERFORMANCE MODEL v2 — EventMath v2.3
note Uses: chain, assume, satisfy for revenue modeling

note ── Benchmarks ──
assume optin rate is 30
assume upsell rate is 15
assume traffic is 10000
assume order value is 67
assume upsell value is 47

note ── Funnel chains ──

chain tripwire
  visitor leads to optin at value traffic
  optin leads to email at value optin rate
  email leads to upsell view at value 100
  upsell view leads to upsell buy at value upsell rate
  no upsell leads to order at value 85
  order leads to complete at value 80
  complete leads to revenue at value order value
end

chain simple
  visitor leads to optin at value traffic
  optin leads to email at value optin rate
  email leads to order at value 10
  order leads to revenue at value order value
end

chain webinar
  visitor leads to register at value traffic
  register leads to attend at value 25
  attend leads to offer at value 20
  offer leads to buy at value 10
  buy leads to revenue at value upsell value
end

chain subscription
  visitor leads to signup at value traffic
  signup leads to trial at value 5
  trial leads to paid at value 25
  paid leads to revenue at value order value
end

show tripwire
show simple

note Evaluate: which funnel makes more money?
satisfy tripwire against tripwire into tripwire result
satisfy simple against simple into simple result
satisfy webinar against webinar into webinar result
satisfy subscription against subscription into subscription result

show tripwire result
show simple result
show webinar result
show subscription result