#!/bin/sh
LOCAL_MOUNT='/Users/rarora17/Documents/GitHub/'
IMAGE_MOUNT='/home/jovyan/work/'
DOCKER_COMMAND="docker run --rm -p 8888:8888 -v $LOCAL_MOUNT:$IMAGE_MOUNT --name JUPYTER -t cvbi/datascience-environment"
echo $DOCKER_COMMAND
