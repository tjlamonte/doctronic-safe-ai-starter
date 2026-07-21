# The Doctronic Incident (January 2026)

In January 2026, an AI system called Doctronic accepted a fabricated regulatory
bulletin and generated a dangerously incorrect prescription dosage recommendation.
The system had no input validation, no audit trail, and no safety checks in place
to catch the fake bulletin before it was acted on.

## Meet Maria

*Maria is a fictitious patient, created for this course to help ground today's
technical work in human terms. She does not represent a real person, but her
situation reflects the kind of harm the real Doctronic failure could plausibly
have caused.*

Maria is a chronic pain patient who has relied on a stable prescription for
years. Her care depends on small, carefully judged adjustments - the kind a
doctor makes cautiously, based on real evidence and real oversight.

Now imagine Maria's care sits behind a system like Doctronic. A bulletin
arrives claiming new dosage guidance. The system has no way to check whether
that bulletin is genuine. It has no rule that says "a change this large
needs a second opinion." It has no record of what it did or why. It simply
acts - and Maria's prescription changes, based on nothing more than an
unverified message that looked official enough.

This is not a hypothetical flaw. It is the exact gap the real Doctronic
incident exposed. Maria's story exists to keep that gap visible and personal
as you work through today's modules - every fix you build is, in effect,
something that stands between a system like this and someone like her.

## What you're building today

This repo recreates the core of that failure as a hands-on exercise. Module
by module, you'll harden the system - adding the validation, logic, audit
trail, and tests that should have existed in the first place. By the end of
the day, the system you're left with is one that could have caught this
before it ever reached a patient.

We'll return to Maria's story at the end of the day, once the system you've
built would actually have protected her.
