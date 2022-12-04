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

# Dependencies
- SPOT (https://spot.lre.epita.fr/install.html)
- Graphviz
```
brew install graphviz
```
- Python 3.10+
- Other packages
```
pip install -r requirements.txt
```

# Usage
- ltl2regex
```
NAME
    main.py ltl2regex

SYNOPSIS
    main.py ltl2regex FORMULA

POSITIONAL ARGUMENTS
    FORMULA
        Type: str
```
- ltl2timeline
```
NAME
    main.py ltl2timeline

SYNOPSIS
    main.py ltl2timeline FORMULA <flags>

POSITIONAL ARGUMENTS
    FORMULA
        Type: str

FLAGS
    --filename=FILENAME
        Type: str
        Default: 'ltl'
    --output_format=OUTPUT_FORMAT
        Type: str
        Default: 'pdf'
```