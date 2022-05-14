#!/usr/bin/env bash

function renameDirAndFile() {
    echo --------------------------------
    echo Removing MD5 suffix in all dir and files...
    DIR="$1"
    # Remove MD5 suffix in all directories and files.
    # 1. Find all paths in current path.
    # 2. Sort the paths in reverse order so the renaming will performs correctly.
    # 3. And rename all the paths to new ones in a `while` loop.
    find "$DIR" -iname "*" | sort -r | while read -r NAME; do
        PARENT_DIR="${NAME%/*}"
        # Remove MD5 suffix in filenames.
        FILE_NAME="$(echo "${NAME##*/}" | sed -E -e "s/(.*) \w{32}(\..*)?/\1\2/")"
        NEW_NAME="$PARENT_DIR/$FILE_NAME"
        #NEW_NAME="$(echo "$NAME" | sed -E -e "s/(.*) \w{32}(\..*)?/\1\2/")"
        # Do not rename base dir
        if [[ "$NAME" != "$DIR" && "$NAME" != "$NEW_NAME" ]]; then
            echo "RENAME: $NAME -> $NEW_NAME"
            mv "$NAME" "$NEW_NAME"
        fi
    done
    echo
}

function proceedAllLines() {
    echo --------------------------------
    echo Proceeding lines of all files...
    DIR="$1"
    #find "$DIR" -iname "*" -type f | while read -r FILE; do
    findAllTextFile "$DIR" | while read -r FILE; do
        echo "PROCEED: $FILE"
        # 1. Remove title of all files.
        #   1.1 Read next line,
        #   1.2 Replace line which starts with "#".
        # 2. Remove extra top blank lines.
        # 3. Remove extra tailing spaces.
        sed -Ei -e "N; /^#.*\n/d" \
            -e "/./,\$!d" \
            -e "s/[ \t]+$//" "$FILE"
        # Append new line to end of file.
        echo "" >> "$FILE"
    done
    echo
}

function addFilename() {
    echo --------------------------------
    echo Adding filename as title...
    DIR="$1"
    #find "$DIR" -iname "*" -type f | while read -r FILE; do
    findAllTextFile "$DIR" | while read -r FILE; do
        TITLE_LINE="${FILE##*/}"
        TITLE_LINE="- ${TITLE_LINE%.*}"
        FIRST_LINE="$(sed -n "1 p" "$FILE")"
        if [[ "$FIRST_LINE" != "$TITLE_LINE" ]]; then
            echo "ADD: $FILE"
            sed -Ei "1 i $TITLE_LINE" "$FILE"
        fi
    done
    echo
}

function findAllTextFile() {
    DIR="$1"
    FILE_PATTERN=".*\.\(md\|txt\)"
    find "$DIR" -iregex "$FILE_PATTERN" -type f
}

function main() {
    DIR="$1"
    if [[ -z "$DIR" ]]; then
        read -r -p "Input dir: " DIR
    fi
    echo "DIR = $DIR"
    echo

    renameDirAndFile "$DIR"
    proceedAllLines "$DIR"
    addFilename "$DIR"
    echo ALL DONE!
}

main "$1"
