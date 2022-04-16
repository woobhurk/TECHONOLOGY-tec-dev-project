#!/usr/bin/env bash

function main() {
    MODE="${1:- -e}"
    BASE_DIR="${2:-"$(pwd)"}"
    [[ "$MODE" != "-e" && "$MODE" != "-d" ]] \
        && echo "Invalid mode (-d or -e): $MODE" \
        && exit -1

    echo "================================"
    echo "Mode: $MODE"
    echo "Base dir: $BASE_DIR"
    processFilename "$MODE" "$BASE_DIR"

    echo ALL DONE!
}

function processFilename() {
    MODE="$1"
    BASE_DIR="$2"
    find "$BASE_DIR/" -type f | while read -r FILE_PATH; do
        DIR="$(dirname "$FILE_PATH")"
        FILE="$(basename "$FILE_PATH")"
        if [[ "$MODE" == "-e" ]]; then
            NEW_FILE="$(basenc --base64url -w 0 <<< "$FILE")"
        else
            NEW_FILE="$(basenc --base64url -d -w 0 <<< "$FILE")"
        fi
        NEW_FILE_PATH="$DIR/$NEW_FILE"
        #echo "$FILE_PATH -> $NEW_FILE_PATH"
        mv "$FILE_PATH" "$NEW_FILE_PATH"
    done
}

main "$1" "$2"
