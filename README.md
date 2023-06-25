# Overview

LTL2TL is a tool which generates timeline visualizations for Linear temporal logic (LTL) formulas. It provides two utilities:
- `ltl2timeline`, for translating LTL formulas to timeline graphic images; and
- `ltl2regex`, for translating LTL formulas to regular expressions representing the solution set of the formula.

The tool works by transforming LTL formulae to Büchi automata (provided by [SPOT](https://spot.lre.epita.fr/)) and subsequently to $\omega$-regular expressions and timeline graphics. It is intended for validating software system specification formulas written in LTL.

Installation, usage and examples are provided below.

# Usage
## Option 1: Docker Image
 (Recommended for trials and artifact evaluation)

 - Make sure you have [Docker](https://docs.docker.com/get-docker/) installed
 - Pull the docker image from Docker Hub
 ```
    $ docker pull runmingl/ltl
 ```
- Run the docker image
 ```
    $ docker run -it runmingl/ltl
 ```
- Run the tool
 ```
    $ cd opt/ltl-explainability/src
    $ python3 main.py ltl2timeline 'G(p xor X p)' --filename 'example' --output_format 'png'
 ```
 This will generate a timeline image `example.gv.png` in the current directory.

 - You can copy the generated images to your local machine via
 ```
    $ docker cp <containerId>:/opt/ltl-explainability/src/example.gv.png .
 ```
 where `<containerId>` is the id of the docker container you just ran.

## Option 2: Local Installation
(Recommended for development)

Download the following dependencies:
### Dependencies
- SPOT (Download [here](https://spot.lre.epita.fr/install.html) and use the following command in the root directory of your installation)
```
$ ./configure --prefix ~/.local && make && sudo make install
```
- Graphviz
```
$ brew install graphviz
```
- Python 3.10+
- Other packages
```
$ pip install -r requirements.txt
```

After installing dependencies, update git submodule via
```bash
$ git submodule init
$ git submodule update
```

# Usage
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

## Examples
LTL Formulas are inputted following the same syntax as [SPOT](https://spot.lre.epita.fr/app/). For example,

```
python3 main.py ltl2timeline 'G(p xor X p)'
```
generates the following timeline

![timeline](paper/examples/ex2/ex2.png)
