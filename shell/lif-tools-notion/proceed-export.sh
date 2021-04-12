#!/usr/bin/env bash

# Remove MD5 suffix in all directories and files.
# 1. Find all paths in current path.
# 2. Sort the paths in reverse order so the renaming will performs correctly.
# 3. And rename all the paths to new ones in a `while` loop.
find . -iname "*" | sort -r | while read -r FILE; do
    NEW_FILE="$(echo "$FILE" | sed -E -e "s/(.*) \w{32}\.(.*)/\1.\2/g")"
    mv "$FILE" "$NEW_FILE"
done

# Remove title of all files.
find . -iname "*" -type f | while read -r FILE; do
    # Read next line, and replace line which starts with "#".
    sed -Ei_ "N; /^#.*\n/d" "$FILE"
    # Append new line to end of file.
    echo "" >> "$FILE"
done
