#!/usr/bin/env bash

# #####
# USAGE
#   sgl-project-run.sh APP_NAME APP_PORT HOST_PORT APP_FILE
# EXAMPLE
#   sgl-project-run.sh demo-app 8080 8081 /data/project/demo-app.jar
#       Build and run a docker project. Naming the image to `demo-app`, app exposes a port `8080`,
#       and map it to port `8081` of the host. The path of app is `/data/project/demo-app.jar`.
#   sgl-project-run.sh demo-app 8080 "8081 8082" /data/project/demo-app.jar
#       Build and run a project in multiple ports.

# -e: Exit when error occurred
set -e

# Directory of this script
BASE_DIR="$(dirname "$0")"
# App name, or image name
APP_NAME="${1:-app}"
# Exposed port of image
APP_PORT="${2:-8080}"
# Mapped ports of host
HOST_PORTS="${3:-8080}"
# Path of app file
APP_FILE="${4:-app.jar}"
# Directory of app file
APP_DIR="$(dirname "$APP_FILE")"
# Path of generated Singularity defination file
SGL_DEF_FILE="$BASE_DIR/singularity-$APP_NAME-$RANDOM.def"
# Path of Singularity SIF file
SGL_SIF_FILE="$APP_DATA/singularity/$APP_NAME.sif"

echo ================================
echo Debug information:
echo "Script directory: $BASE_DIR/"
echo "App name: $APP_NAME"
echo "App port: $APP_PORT"
echo "Host ports: $HOST_PORTS"
echo "App file path: $APP_FILE"
echo "App file directory: $APP_DIR/"
echo "Singularity defination file path: $SGL_DEF_FILE"
echo "Singularity SIF file path: $SGL_SIF_FILE"
echo

echo ================================
echo Copying needed files...
cp -f "$BASE_DIR/sgl-project-entrypoint.sh" "$APP_DIR/"
echo

echo ================================
echo Generating Singularity defination file...
SGL_APP_FILE="$(basename "$APP_FILE")"
# Make a copy of origional denfination file
cp -f "$BASE_DIR/singularity.def" "$SGL_DEF_FILE"
# Replace variables in defination file
sed -i -E -e "s|\{\{APP_FILE\}\}|$SGL_APP_FILE|g" \
    -e "s|\{\{CONTEXT_DIR\}\}|$APP_DIR|g" \
    "$SGL_DEF_FILE"
echo

echo ================================
echo Building container...
singularity build --force "$SGL_SIF_FILE" "$SGL_DEF_FILE"
echo

echo ================================
for PORT in $HOST_PORTS; do
    CONTAINER_NAME="$APP_NAME-$PORT"
    echo --------------------------------
    echo "Running container $CONTAINER_NAME..."
    singularity instance start \
        --net --network-args "portmap=$PORT:$APP_PORT/tcp" \
        --bind "/data:/host-data" \
        "$SGL_SIF_FILE" "$CONTAINER_NAME"
    #SGL_SIF_LOG_FILE="$SGL_SIF_FILE-$(date +%Y%m%d).out"
    #singularity run --bind "/data:/host/data" "$SGL_SIF_FILE" \
    #    /data/project/sgl-project-entrypoint.sh >> "$SGL_SIF_LOG_FILE" 2>&1 &
done
echo

echo ================================
echo Deleting temporary files...
rm -f "$SGL_DEF_FILE"
echo

echo ALL DONE!
