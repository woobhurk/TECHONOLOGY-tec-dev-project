#!/usr/bin/env bash

function renameDirAndFile() {
    echo "--------------------------------"
    echo "Removing MD5 suffix in all dir and files..."
    DIR="$1"
    # Remove MD5 suffix in all directories and files.
    # 1. Find all paths in current path.
    # 2. Sort the paths in reverse order so the renaming will performs correctly.
    # 3. And rename all the paths to new ones in a `while` loop.
    find "$DIR" -iname "*" | sort -r | while read -r NAME; do
        NEW_NAME="$(echo "$NAME" | sed -E -e "s/(.*) \w{32}(\..*)?/\1\2/")"
        if [[ "$NAME" != "$NEW_NAME" ]]; then
            echo "RENAME: $NAME -> $NEW_NAME"
            mv "$NAME" "$NEW_NAME"
        fi
    done
    echo
}

function removeTitle() {
    echo "--------------------------------"
    echo "Removing title of all files..."
    DIR="$1"
    # Remove title of all files.
    find "$DIR" -iname "*" -type f | while read -r FILE; do
        echo "PROCEED: $FILE"
        # Read next line, and replace line which starts with "#".
        sed -Ei "N; /^#.*\n/d" "$FILE"
        # Append new line to end of file.
        echo "" >> "$FILE"
    done
    echo
}

function main() {
    DIR="$1"
    if [[ -z "$DIR" ]]; then
        read -r -p "Input dir: " DIR
    fi
    renameDirAndFile "$DIR"
    removeTitle "$DIR"
    echo ALL DONE!
}

main "$1"
