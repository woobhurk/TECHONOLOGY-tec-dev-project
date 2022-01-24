#!/usr/bin/env bash

function processFilename() {
    BASE_DIR="$1"
    MODE="$2"
    find "$BASE_DIR" -type f | while read -r FILE_PATH; do
        DIR="$(dirname "$FILE_PATH")"
        FILE="$(basename "$FILE_PATH")"
        if [[ "$MODE" == "d" ]]; then
            NEW_FILE="$(base64 -d -w 0 <<< "$FILE")"
        else
            NEW_FILE="$(base64 -w 0 <<< "$FILE")"
        fi
        NEW_FILE_PATH="$DIR/$NEW_FILE"
        echo "$FILE_PATH -> $NEW_FILE_PATH"
        mv "$FILE_PATH" "$NEW_FILE_PATH"
    done
}

function main() {
    BASE_DIR="${1:-"$(pwd)"}"
    MODE="${2:-e}"
    echo "Base dir: $BASE_DIR"
    echo "Mode: $MODE"
    processFilename "$BASE_DIR" "$MODE"
}

main "$1" "$2"
