# Docker 101

Hello, welcome to the most awesome docker tutorial in the interweb!

🐋 🐳

## Installation

In order to install this repository, make sure you have [git](https://git-scm.com) and [docker](https://www.docker.com/) installed in your system. Then:

```
git clone https://github.com/jaymeanchante/docker101-tutorial && cd docker101-tutorial
```

In order to run the architecture:
```
sh docker-compose-up.sh
```

After the system is up and running, make sure you create a Bucket called `iris` in Localstack's S3 using either: i) the `/create_bucket` route explained below; ii) aws-cli inside the docker container `docker exec -it src_api_1 bash -c "aws s3 mb s3://iris --endpoint-url http://localstack:4572"`; iii) [aws-cli](https://github.com/aws/aws-cli) in your local system `aws s3 mb s3://iris --endpoint-url http://localhost:4572`

## Tutorial

It is divided in 4 steps:

1. [Local application](01_local_application/README.md)
2. [Dockerizing the application](dockerizing_application/README.md)
3. [Adding another service](03_adding_another_service/README.md)
4. [Multi container application](./README.md)

## Architecture

This system consist of two services called api and localstack. Both services are running in docker containers and can communicate with each other.

### Localstack

[Localstack](https://github.com/localstack/localstack) is a fully functional local AWS cloud stack. They provide a nice [docker-compose](https://github.com/localstack/localstack/blob/master/docker-compose.yml) starting point.

Useful links:

* [Overview of deployed resources](http://localhost:8080)
* [S3 file system](http://localhost:4572)
* [Edge route](http://localhost:4566)


### Api

An API written in [Python](https://www.python.org/) using the [Flask](https://flask.palletsprojects.com/) framework.

* Protocol: http
* Endpoint: 0.0.0.0
* Port: 5000
* Header: Content-Type: application/json

#### Routes

**/create_bucket/_bucket_**

Creates a S3 Bucket named _bucket_.

Testing the route:

```
curl -X POST http://0.0.0.0:5000/create_bucket/iris
```

obs: an additional step in order to make the bucket public read is:
```
aws s3api put-bucket-acl --bucket iris --acl public-read --endpoint-url=http://localhost:4572
```

**/upload_file/_researcher_**

Uploads a JSON file to a _researcher_ namespace.

Testing the route:

```
curl -X POST -d '{"iris": "setosa"}' -H 'Content-Type: application/json' 0.0.0.0:5000/upload_file/anderson
```

**/list_files/_researcher_**

Lists files of a given _researcher_.

Testing the route:

```
curl -X GET 0.0.0.0:5000/list_files/anderson
```

**/download_file/_researcher_/_fileid_**

Downloads file of a given _researcher_ given the _filename_.

Testing the route:

```
curl -X GET 0.0.0.0:5000/download_file/anderson/a1b2-c3d4.json
```