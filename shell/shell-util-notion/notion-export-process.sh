#!/usr/bin/env bash

set -e

function main() {
    DIR="$1"
    if [[ -z "$DIR" ]]; then
        read -r -p "Input dir: " DIR
    fi
    echo "DIR = $DIR"
    echo

    renameDirAndFile "$DIR"
    processAllLines "$DIR"
    addFilename "$DIR"
    echo ALL DONE!
}

function renameDirAndFile() {
    echo --------------------------------
    echo Removing MD5 suffix in all dir and files...
    DIR="$1"
    # Remove MD5 suffix in all directories and files.
    # 1. Find all paths in current path.
    # 2. Sort the paths in reverse order so the renaming will performs correctly.
    # 3. And rename all the paths to new ones in a `while` loop.
    while read -r FILE_PATH; do
        DIR_PATH="$(dirname "$FILE_PATH")"
        # Remove MD5 suffix in filenames.
        NEW_FILENAME="$(basename "$FILE_PATH" | sed -E -e "s/(.*) \w{32}(\..*)?/\1\2/")"
        NEW_FILE_PATH="$DIR_PATH/$NEW_FILENAME"
        # Do not rename base dir
        if [[ "$FILE_PATH" != "$DIR" && "$FILE_PATH" != "$NEW_FILE_PATH" ]]; then
            echo "Renaming: $FILE_PATH -> $NEW_FILE_PATH"
            mv "$FILE_PATH" "$NEW_FILE_PATH"
        fi
    done < <(find "$DIR/" -mindepth 1 -iname "*" | sort -r)
    echo
}

function processAllLines() {
    echo --------------------------------
    echo Proceeding lines of all files...
    DIR="$1"
    while read -r FILE; do
        echo "Processing: $FILE"
        # 1. Remove title of all files.
        #   1.1 Read next line,
        #   1.2 Remove line which starts with "#".
        sed -Ei -e "{N; /^#.*\n/ d}" "$FILE"
        # 1. Remove extra tailing spaces.
        sed -Ei -e "s/[ \t]+$//g" "$FILE"
        # Append new line to end of file.
        echo "" >> "$FILE"
    done < <(findAllTextFile "$DIR")
    echo
}

function addFilename() {
    echo --------------------------------
    echo Adding filename as title...
    DIR="$1"
    while read -r FILE; do
        FILENAME="- $(basename "$FILE")"
        TITLE_LINE="${FILENAME%.*}"
        FIRST_LINE="$(sed -n "1 p" "$FILE")"
        if [[ "$FIRST_LINE" != "$TITLE_LINE" ]]; then
            echo "Adding line: $FILE"
            sed -Ei -e "1 i $TITLE_LINE" "$FILE"
        fi
    done < <(findAllTextFile "$DIR")
    echo
}

function findAllTextFile() {
    DIR="$1"
    PATTERN=".*\.\(md\|txt\)"
    find "$DIR/" -iregex "$PATTERN" -type f
}

main "$1"
