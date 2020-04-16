# Local application

## Setup

Make sure you have [Python](https://www.python.org/) installed in your system and then run the following:

```
cd 01_local_application && python3 -m venv venv && source venv/bin/activate && pip3 install -U pip && pip3 install -r requirements.txt
```

## Architecture

The central unit is the minimal application from [flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/) and [flask-restful](https://flask-restful.readthedocs.io/en/latest/quickstart.html)

Head over to http://localhost:5000/ in your browser and check if the "Hello world!" message appears or use [curl](https://curl.haxx.se/) `curl http://localhost:5000/`

## Description

This is an application running locally using the configuration of your host system. However, it has no description of how to configure your entire system, only that it depends on Python (version?) and the stated libraries in `requirements.txt` (what if a can't install a dependency?)

It is very common that people write a piece of code without any other actual context (programming language, dependencies, setup, installation etc.). Reproducibility is one of the core principles of (data) science, if one cannot reproduce a machine learning benchmark or cannot use a pre-trained model, it turns your work almost useless

## Next steps

Please head over to the next section [02 - Dockerizing the application](../02_dockerizing_application/README.md)