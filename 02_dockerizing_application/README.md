# Dockerizing the application

## Setup

Make sure you have [docker](https://www.docker.com/) installed in your system and then run the following:

```
cd ../02_dockerizing_application && sh docker-run.sh
```

The `docker-run.sh` file contains two instructions:

1. It checks whether your system has the appropriate docker image, if it doesn't, it builds it using the instruction contained in the `Dockerfile`

2. It runs the image as a container using the appropriate flags and entry point.

This is the same minimal application from [section 01](../01_local_application/README.md). However, there is a big difference now: the application is running inside a container instead of your host OS!

Head over to http://localhost:5000/ in your browser and check if the "Hello world!" message still appears or use [curl](https://curl.haxx.se/) `curl http://localhost:5000/`

## Description

The _docker-run.sh_  file contains the two main docker instructions to run the application: `build` and `run`. Let's explain them a little bit:

* **build**: it takes the instructions contained in a _Dockerfile_ in order to compile a new image containing new system dependencies not contained in the base image, system management and most importantly your code. The mandatory flag in this command is `-t` or `--tag` where you can name your image using the convention `$image:$tag`

* **run**: it takes a pre-compiled image in your system (or tries to pull one from [ducker hub](https://hub.docker.com/)) and run it as a container. You can think of images as the ISO file of an operating system, you can't interact with that, however, when plug in a USB containing an ISO and boots from that, you have a operating system that you can use, this is the equivalent of a container, it is the "living" thing. The only mandatory argument in the `run` command is the name of the image you are running. However, a few other flags were used:

    - --rm: completely removes the container after you stop it
    - --name: give it a name of using the default name generator from docker
    - -it: give the container a shell session
    - -v: pair volumes between your local host and the guest container
    - -p: pair ports between your local host and the guest container
    - $image:$tag: the name and tag of the we want to run
    - bash -c: a bash command we want to run as soon as the image begin

Let's dive a bit into the _Dockerfile_. It has a few commands inside:

    - FROM: the base image we are going to use to build our own image
    - WORKDIR: defined a working directory, something like `cd` in shell
    - RUN: shell commands
    - COPY: copy file from your host to your guest/container

Docker ensures operating system level reproducibility. You still have to define your Python-level dependencies (aka _requirements.txt_) or any other library dependencies in other languages (_package.json_ in [Node.js](https://nodejs.org) for example). However, you don't have to point out each and every system dependency the application needs because everything is going to be specified in the _Dockerfile_!

## Next steps

Please head over to the next section [03 - Adding another service](../03_adding_another_service/README.md)