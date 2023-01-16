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
# Submission Information
1) Special Issue - Journal of Computer Languages Issue on Foundations and Practice of Visual Modeling

Call for Papers: Journal of Computer Languages Issue on Foundations and Practice of Visual Modeling
https://www.sciencedirect.com/journal/journal-of-computer-languages/about/forthcoming-special-issues#foundations-and-practice-of-visual-modeling-fpvm

### Scope
The sheer complexity of software systems nowadays makes modeling artifacts pervasive throughout the development process, be it use requirements, analysis, design, or development. Whether models are used for communication or prescriptive purposes, their syntax and pragmatics affect usability and represent contributory factors concerning the accidental complexity. The diversity of modeling notations and approaches permits classifying them according to different taxonomies. General-purpose and domain-specific modeling languages can be created with different intended scopes, although all of them can make use of graphical, textual, maps, matrices, tables, and combinations regarding its concrete syntax. These representations have the undoubted advantage of capturing and increasing understanding of complex software systems and better grasping the rationale behind them. In essence, a visual modeling language creates a joint base for the modeler by improving their communication and lays a solid foundation for the implementation.

The special issue aims at providing a window for researchers and practitioners from academia and industry in which novel and innovative solutions to current and future challenges of the visualization of modeling languages can be presented and discussed. Topics of interest are but are not limited to:
- Visualization techniques and methodologies for modeling languages
- Visualizing models for different stakeholders/readers
- Visualizing errors in models (incompleteness, inconsistency, incorrectness)
- Guidance in modeling languages
- Visualizing version data of models
- Visualizing different views
- Complex or large-scale model visualization
- Usability for visual modeling languages
- Meta-editors novel approaches
- Development of collaborative (human-in-the-loop) visual modeling languages
- Visual Modeling platforms for cloud applications
- LowCode/NoCode techniques and methodologies

### Submission Guidelines
Submissions should describe original research and must not have been previously published or be under review at a different venue. Authors are requested to follow instructions for manuscript submission to the Journal of Computer Languages https://www.elsevier.com/journals/journal-of-computer-languages/2590-1184/guide-for-authors. To ensure that your manuscript is correctly identified for inclusion into the special issue, please select article type "VSI:FPVM" upon upload. The submission website is located at: https://www.editorialmanager.com/cola.

### Important Dates
Date of expected first submission: 1st January, 2023
Date first review round completed: 1st March, 2023
Date revised manuscripts due: 1st May, 2023
Date completion of the review and revision process: 1st June, 2023

### Guest Editors
Amleto Di Salle, European University of Rome, Rome, Italy
Ludovico Iovino, Gran Sasso Science Institute, L'Aquila, Italy
Alfonso Pierantonio, University of L'Aquila, L'Aquila, Italy
Juha-Pekka Tolvanen, MetaCase, Finland


2) (Possible backup to consider)
************************************************************
Call for Papers: 28th International Conference on Conceptual Structures (ICCS 2023)
September 11th-13rd, 2023, Berlin, Germany

Website: https://iccs-conference.org
Twitter: @iccs_confs
Contact us:  contact@iccs-conference.org
************************************************************

***************
About ICCS:
***************
The International Conferences on Conceptual Structures (ICCS) focus on the formal analysis and representation of conceptual knowledge at the crossroads of artificial intelligence, human cognition, computational linguistics, and related areas of computer science and cognitive science. The ICCS conferences evolved from seven annual workshops on conceptual graphs, starting with an informal gathering hosted by John F. Sowa in 1986. Recently, graph-based knowledge representation and reasoning (KRR) paradigms have been getting more and more attention. With the rise of quasi-autonomous AI, graph-based representations provide a vehicle for making machine cognition explicit to human users. ICCS 2023 will take place in Berlin, Germany, in September 2023. Scholars, students and industry participants from different disciplines will meet for several weeks of conferences, workshops, summer schools, and public events to engage with the broad topics, issues and challenges related to knowledge in the 21st century.

Submissions are invited on significant, original, and previously unpublished research on the formal analysis and representation of conceptual knowledge in artificial intelligence (AI). All papers will receive mindful and rigorous reviews that will provide authors with useful critical feedback. The aim of the ICCS 2023 conference is to build upon its long-standing expertise in graph-based KRR and focus on providing modelling, formal and application results of graph-based systems. In particular, the conference welcomes contributions that address graph-based representation and reasoning paradigms (e.g. Bayesian Networks (BNs), Semantic Networks (SNs), RDF(S), Conceptual Graphs (CGs), Formal Concept Analysis (FCA), CP-Nets, GAI-Nets, Graph Databases, Diagrams, Knowledge Graphs, Semantic Web, etc.) from a modelling, theoretical and application viewpoint.

**********
Topics:
**********

Topics include but are not limited to:
Existential and Conceptual Graphs
Graph-based models for human reasoning
Social network analysis
Formal Concept Analysis
Conceptual knowledge acquisition
Data and Text mining
Human and machine reasoning under inconsistency
Human and machine knowledge representation and uncertainty
Automated decision-making
Argumentation
Constraint satisfaction
Preferences
Contextual logic
Ontologies
Knowledge architecture and management
Semantic Web, Web of Data, Web 2.0, Linked (Open) Data
Conceptual structures in natural language processing and linguistics
Metaphoric, cultural or semiotic considerations
Resource allocation and agreement technologies
Philosophical, neural, and didactic investigations of conceptual, graphical representations


********************
Important Dates:
********************

- Abstract registration deadline: March 19th, 2023
- Submission deadline: March 26th, 2023
- Paper Reviews Sent to Authors: May 14th, 2023
- Rebuttals Due: May 21th, 2023
- Notification to authors: May 31th, 2023
- Camera-ready papers due: June 14th, 2023

********************
Submission Details:
********************

We invite scientific papers of up to fourteen pages, short contributions of up to eight pages, and extended poster abstracts of up to three pages. Papers and poster abstracts must be formatted according to Springer’s LNCS style guidelines and not exceed the page limit. Papers will be subject to double-blind peer review, in which the reviewers do not know the author's identity. We recommend using services like https://anonymous.4open.science/ to anonymously share code or data. Anonymized works that are available as preprints (e.g., on arXiv or SSRN) may be submitted without citing them. Submission should be made via EasyChair: https://easychair.org/conferences/?conf=iccs2023. All paper submissions will be refereed, and authors will have the opportunity to respond to reviewers’ comments during the rebuttal phase. Accepted papers will be included in the conference proceedings, published by Springer in the LNCS/LNAI series. Poster submissions will also be refereed  and selected poster abstracts might be included in the conference proceedings. At least one author of each accepted paper or poster must register for the conference and present the paper or poster there. Proceedings will be indexed by DBLP.

***************
Organizers:
***************

General Chair:
Robert Jäschke, Information Processing and Analytics, Humboldt University of Berlin, Germany

Program Chairs:
Manuel Ojeda Aciego, Dept. Applied Mathematics, University of Málaga, Spain
Kai Sauerwald, Artificial Intelligence Group, FernUniversität in Hagen, Germany

*****************************************
