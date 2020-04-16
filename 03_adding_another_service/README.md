# Adding another service

Let's take a step back, and run our application again using our local Python installation. However, we will run another service using docker.

## Setup

Make sure you have [docker](https://www.docker.com/) installed in your system and then run the following:

```
cd ../03_adding_another_service && sh docker-run.sh
```

Open another tab in your terminal and then run the API using the following:

```
python3 -m venv venv && source venv/bin/activate && pip3 install -U pip && pip3 install -r requirements.txt && python3 app.py
```

## Architecture

### Localstack

The _docker-run.sh_ file will launch a [localstack](https://github.com/localstack/localstack) image which offer a wide array of [AWS](https://aws.amazon.com/) services that run inside the container. In this case, we are going to use the [S3 (Simple Storage Service)](https://aws.amazon.com/s3/) service to store our [JSON](https://www.json.org/json-en.html) files

### Api

The Api service is still running in our local installation of Python. In the next section we are going to launch both services using docker with the [docker-compose tool](https://docs.docker.com/compose/)

If you want to check out all the routes available, please refer to the main [README.md](../README.md)

## Next steps

Please head over to the next section [04 - Multi container application](../README.md) in the main _README_ file