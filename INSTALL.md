# Install
## Option 1: Docker Image
 (Recommended for trials and artifact evaluation: this method can be used on any systems with Docker installed)

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
(Recommended for development: this method requires a Unix-like system with Python 3.10+ installed)
This method will likely take more than 30 minutes to set up.

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