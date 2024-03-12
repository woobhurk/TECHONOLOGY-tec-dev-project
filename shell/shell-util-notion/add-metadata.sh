#!/bin/env bash

set -e

function main() {
    local DIR="$1"

    addMetadata "$DIR"

    echo ALL DONE!
}

function addMetadata() {
    local DIR="$1"
    declare -A DOMAIN_MAP=(
        ["com"]="computer"
        ["edu"]="education"
        ["lif"]="life"
        ["tec"]="technology"
        ["wor"]="work"
    )

    while read -r FILE; do
        echo "Processing file: $FILE"
        local FILENAME="$(basename "$FILE")"
        # 形如 com-os-linux
        local DIRNAME="$(basename "$(dirname "$FILE")")"
        # 标题，不含后缀名
        local TITLE="${FILENAME%.*}"
        # 截取 com
        local DOMAIN="$(echo "$DIRNAME" | awk '{split($0, arr, "-"); print arr[1]}')"
        # 截取 os
        local CATEGORY="$(echo "$DIRNAME" | awk '{split($0, arr, "-"); print arr[2]}')"
        # 截取 linux
        local TAG="${DIRNAME#*-*-}"
        local METADATA="---\ntitle: $TITLE\ntype: note\ndomain: ${DOMAIN_MAP[$DOMAIN]}\ncategory: $CATEGORY\ntags:\n    - $TAG\ncreate-time:\n---"

        # 1、插入元数据到文件开头
        echo "Adding metadata..."
        echo -e "METADATA=$METADATA"
        sed -Ei_ -e "1 i $METADATA" \
            "$FILE"
        # 2、删除标题行
        echo "Removing title line..."
        sed -Ei -e "/^- (# +)?$TITLE\$/ d" \
            "$FILE"
    done < <(find "$DIR/" -iregex ".*\.\(md\|txt\)" -type f)
}

main "$@"



#while read -r FILE; do
#    FILENAME="$(basename "$FILE")"
#    TITLE="${FILENAME%.*}"
#    CATEGORY1="$(echo "$TITLE" | awk '{split($0, arr, "-"); print arr[1]}')"
#    CATEGORY2="$(echo "$TITLE" | awk '{split($0, arr, "-"); print arr[2]}')"
#    echo "$TITLE: $CATEGORY1  $CATEGORY2"
#    sed -Ei_ -e "s/(- book)/\1\n    - $CATEGORY1\n    - $CATEGORY2/" "$FILE"
#done < <(find ./ -iname "*-*-*.md" -type f)



#while read -r FILE; do
#    FILENAME="$(basename "$FILE")"
#    TITLE="${FILENAME%.*}"
#    CATEGORY="$(echo "$TITLE" | awk '{split($0, arr, "-"); print arr[1]}')"
#    NEW_TITLE="$(echo "$TITLE" | awk '{split($0, arr, "-"); print arr[2]}')"
#    echo "$TITLE: $CATEGORY $NEW_TITLE"
#    sed -Ei_ -e "s/(- video)/\1\n    - $CATEGORY/" "$FILE"
#    mv "$FILE" "$(dirname "$FILE")/$NEW_TITLE.md"
#done < <(find ./ -iname "*-*.md" -type f)



#while read -r FILE; do
#    FILENAME="$(basename "$FILE")"
#    TITLE="${FILENAME%.*}"
#    echo "$FILENAME: $TITLE"
#    sed -Ei_ -e "s/title: .*/title: $TITLE/g" "$FILE"
#done < <(find ./ -iname "*.md" -type f)
