#!/bin/bash

# variables
image="localstack/localstack"
tag="latest"
name="localstack"

# running the $image as a container
docker run --rm --name $name -it -v /tmp/localstack:/tmp/localstack -p "4566-4599:4566-4599" -p 8080:8080 -e SERVICES=s3 $image:$tag