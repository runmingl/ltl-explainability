# ltl-explainability

# What's in a Name? Linear Temporal Logic Literally Represents Time Lines
(because Shakespeare...)

Linear Temporal Logic (LTL) is widely used to specify requirements in safety- critical systems. However, like many formal verification techniques, it is known to be unintuitive and error-prone for human practitioners to specify and validate. In this paper, we provide a new timeline tool for visualizing LTL-based specifications, which is effective at intuitively representing a wide range of formulas. Our tool generates timeline visualizations by translating LTL formulae to intermediate representations as Buchi automata and then ω-regular expressions, and finally simplifying and visualizing the expressions. We provide an algorithm for this visualization, a theoretical soundness analysis, and an implementation.

# Dependencies
- SPOT (https://spot.lre.epita.fr/install.html)
```
./configure --prefix ~/.local && make && sudo make install
```
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
Before running the tool, make sure that all dependencies are properly installed. Then update git submodule via
```bash
$ git submodule init
$ git submodule update
```

We provide 2 command-line tools:
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
        Supported values: ['pdf', 'png', 'svg', 'latex']
```
