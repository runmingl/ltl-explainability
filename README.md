# ltl-explainability

# What's in a Name? Linear Temporal Logic Literally Represents Time Lines
(because Shakespeare...)

Algorithm Outline:
LTL -> minimized GBA (using SPOT) -> regular expression (new algorithm) -> minimized RegEx  (via TBD tool) -> timeline (new algorithm)

Alternatives (for now or to mention as "future work")
- See if translating directly from LTL to RegEx provides a different minimized RegEx or a better time complexity

Stuff We Think Is True:
- Propose that a minimal RegEx always makes the best (most explainable) timeline
- Propose that average-case complexity is much much better than worst-case (because we can likely find pathological LTL formulas but these would not make sense as real-life requirements and an analysis of real-life LTL requirements will produce certain characteristics amenable to our algorithm)
