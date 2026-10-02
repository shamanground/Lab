# EXP-0002 hypothesis

HYPOTHESIS
Exact object inequality cannot tell a same-pole paraphrase from an opposite pole. It marks shut/closed, 120/120 m, Open/open, and whitespace variants as contradictions. A deterministic normalizer (casefold, whitespace fold, strip a fixed unit suffix, apply a fixed synonym map) agrees on those same-pole pairs and still contradicts 120/140 and open/closed.

EXPECTED OBSERVATION
Exact detector false-flags the same-pole pairs. Normalized detector matches expected agree/contradict on those pairs and on the two opposite pairs. not open/closed remains a false contradiction, because no negation rule is in the map.

FAILURE CONDITION
Normalizer collapses 120 and 140, or fails to agree shut with closed, or exact already agrees on the unit and case pairs.

WHAT WOULD CHANGE MY MIND
A fixture where shut is not a synonym of closed, or where stripping " m" deletes a meaningful distinction.

LABEL CORRECTION
The first local pass labeled closed/shut as contradict. That treats a synonym as an opposite pole. Corrected expected label is agree. The wrong pass is not evidence.
