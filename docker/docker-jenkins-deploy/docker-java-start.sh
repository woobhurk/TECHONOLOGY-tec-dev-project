#!/usr/bin/env bash

# #####
# USAGE
#   docker-java-start.sh PROJECT_NAME PROJECT_PORT HOST_PORTS PROJECT_FILE
# EXAMPLE
#   docker-java-start.sh demo-app 8080 8081 /data/project/demo-app.jar
#       Build and run a docker project. Naming the image to `demo-app`, app exposes a port `8080`,
#       and map it to port `8081` of the host. The path of app is `/data/project/demo-app.jar`.
#   docker-java-start.sh demo-app 8080 "8081 8082" /data/project/demo-app.jar
#       Build and run a project in multiple ports.

# -e: Exit when error occurred
set -e

# Directory of this script
BASE_DIR="$(dirname "$0")"
# Project name, or image name
PROJECT_NAME="${1:-app}"
# Exposed port of image
PROJECT_PORT="${2:-8080}"
# Mapped ports of host
HOST_PORTS="${3:-18080}"
# Path of project file
PROJECT_FILE="${4:-app.jar}"
# Directory of project file
PROJECT_DIR="$(dirname "$PROJECT_FILE")"

# Path of Dockerfile
DOCKERFILE="$BASE_DIR/docker-java-image.dockerfile"
# Path of project entrypoint script
PROJECT_ENTRYPONT="$BASE_DIR/docker-java-entrypoint.sh"

echo ================================
echo Debug information:
echo "Script directory: $BASE_DIR/"
echo "Project name: $PROJECT_NAME"
echo "Project port: $PROJECT_PORT"
echo "Host ports: $HOST_PORTS"
echo "Project file: $PROJECT_FILE"
echo "Project directory: $PROJECT_DIR/"
echo
echo "Dockerfile: $DOCKERFILE"
echo "Project entrypoint script: $PROJECT_ENTRYPONT"
echo

echo ================================
echo Initializing...
cp -f "$PROJECT_ENTRYPONT" "$PROJECT_DIR/"
echo

echo ================================
echo "Building docker image with name $PROJECT_NAME..."
# -f: Dockerfile path
# -t: Image name
# --build-arg: Arguments to be used in Dockerfile
DOCKER_PROJECT_FILE="$(basename "$PROJECT_FILE")"
docker build -f "$DOCKERFILE" \
    -t "$PROJECT_NAME" \
    --build-arg PROJECT_FILE="$DOCKER_PROJECT_FILE" \
    "$PROJECT_DIR/"
echo

echo ================================
for PORT in $HOST_PORTS; do
    CONTAINER_NAME="$PROJECT_NAME-$PORT"
    #CONTAINER_ID="$(docker ps -a | grep "$CONTAINER_NAME" | awk '{print \$1}')"
    # Delete exists container
    echo --------------------------------
    echo "Deleting container $CONTAINER_NAME..."
    docker container rm -f "$CONTAINER_NAME"
    # Run container
    echo "Running container $CONTAINER_NAME..."
    docker run -d --name "$CONTAINER_NAME" -p $PORT:$PROJECT_PORT \
        "$PROJECT_NAME"
    # Log command
    echo "docker logs -f $CONTAINER_NAME"
done
echo

echo ALL DONE!
