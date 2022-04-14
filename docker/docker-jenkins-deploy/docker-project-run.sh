#!/usr/bin/env bash

# #####
# USAGE
#   docker-project-run.sh APP_NAME APP_PORT HOST_PORT APP_FILE
# EXAMPLE
#   docker-project-run.sh demo-app 8080 8081 /data/project/demo-app.jar
#       Build and run a docker project. Naming the image to `demo-app`, app exposes a port `8080`,
#       and map it to port `8081` of the host. The path of app is `/data/project/demo-app.jar`.
#   docker-project-run.sh demo-app 8080 "8081 8082" /data/project/demo-app.jar
#       Build and run a project in multiple ports.

# -e: Exit when error occurred
set -e

# Directory of this script
BASE_DIR="$(dirname "$0")"
# App name, or image name
APP_NAME="${1:-app}"
# Port of app image
APP_PORT="${2:-8080}"
# Port of app ocntainer
CONTAINER_PORT="${3:-8080}"
# Path of app file
APP_FILE="${4:-app.jar}"
# Directory of app file
APP_DIR="$(dirname "$APP_FILE")"

echo ================================
echo Debug information:
echo "Script directory: $BASE_DIR/"
echo "App name: $APP_NAME"
echo "App port: $APP_PORT"
echo "Container port: $CONTAINER_PORT"
echo "App file path: $APP_FILE"
echo "App file directory: $APP_DIR/"
echo

echo ================================
echo Copying needed files...
cp -f "$BASE_DIR/docker-project-entrypoint.sh" "$APP_DIR/"
echo

echo ================================
echo "Building docker image with name $APP_NAME..."
# -f: Dockerfile path
# -t: Image name
# --build-arg: Arguments to be used in Dockerfile
DOCKER_APP_FILE="$(basename "$APP_FILE")"
docker build -f "$BASE_DIR/Dockerfile" -t "$APP_NAME" \
    --build-arg APP_FILE="$DOCKER_APP_FILE" \
    "$APP_DIR/"
echo

echo ================================
for PORT in $CONTAINER_PORT; do
    CONTAINER_NAME="$APP_NAME-$PORT"
    #CONTAINER_ID="$(docker ps -a | grep "$CONTAINER_NAME" | awk '{print \$1}')"
    # Delete exists container
    echo --------------------------------
    echo "Deleting container $CONTAINER_NAME..."
    docker container rm -f "$CONTAINER_NAME"
    # Run container
    echo "Running container $CONTAINER_NAME..."
    docker run -d --name "$CONTAINER_NAME" -p $PORT:$APP_PORT \
        "$APP_NAME"
    # Log command
    echo "docker logs -f $CONTAINER_NAME"
done
echo

echo ALL DONE!
