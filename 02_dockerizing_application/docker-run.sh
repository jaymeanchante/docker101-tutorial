#!/bin/bash

# variables
image="demo_api"
tag="latest"
command="gunicorn -b 0.0.0.0:5000 --reload app:app"

# test if $image already exists, if not, build it
if test ! -z "$(docker images -q $image:$tag)"; then
	echo "\nImage already exists\n\n"
else
	echo "\nCompiling the image, should take a few minutes\n\n"
	docker build -t $image:$tag . --no-cache
	echo "\n\nCompiled the image successfully\n\n"
fi

# running the $image as a container
docker run --rm --name $image -it -v $PWD:/root/ -p 5000:5000 $image:$tag bash -c "$command"