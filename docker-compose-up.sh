#!/bin/bash

# docker build -f src/Dockerfile -t src_api:test .
# docker run --rm --name src_api_1 -it -v $PWD/src:/root -p 5000:5000 src_api:latest

# urls
# s3: http://localhost:4572/
# localstack dashboard: http://localhost:8080/#!/infra
# localstack edge service: http://localhost:4566/

docker-compose --file src/docker-compose.yml up