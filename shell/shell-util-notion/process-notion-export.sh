#!/usr/bin/env bash

set -e

function main() {
    local DIR="$1"

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
    local DIR="$1"

    echo --------------------------------
    echo Removing MD5 suffix in all dir and files...
    # 删除文件和目录中的 md5 字符
    # 1、查找当前目录下所有的文件和目录（不包括当前目录）
    # 2、根据路径来方向排序，这样文件能先于目录被重命名，就能保证文件和目录重命名的正确
    # 3、在 while 循环中重命名
    while read -r FILE_PATH; do
        DIR_PATH="$(dirname "$FILE_PATH")"
        # 删除文件名中的 md5 字符，但保留文件名和后缀
        NEW_FILENAME="$(basename "$FILE_PATH" | sed -E -e "s/(.*) \w{32}(\..*)?/\1\2/")"
        NEW_FILE_PATH="$DIR_PATH/$NEW_FILENAME"
        # 不重命名当前目录，以及名字不变的文件
        if [[ "$FILE_PATH" != "$DIR" && "$FILE_PATH" != "$NEW_FILE_PATH" ]]; then
            echo "Renaming: $FILE_PATH -> $NEW_FILE_PATH"
            mv "$FILE_PATH" "$NEW_FILE_PATH"
        fi
    done < <(find "$DIR/" -mindepth 1 -iname "*" | sort -r)
    echo
}

function processAllLines() {
    local DIR="$1"

    echo --------------------------------
    echo Proceeding lines of all files...
    while read -r FILE; do
        echo "Processing: $FILE"
        # 1、删除所有的标题行
        #   1.1、读取下一行到缓冲区
        #   1.2、删除 # 开头的行以及后面的空行
        sed -Ei -e "{N; /^#.*\n/ d}" "$FILE"
        # 删除行尾的空白符
        sed -Ei -e "s/[ \t]+$//g" "$FILE"
        # 添加新行到文件末尾
        echo "" >> "$FILE"
    done < <(findAllTextFile "$DIR")
    echo
}

function addFilename() {
    local DIR="$1"

    echo --------------------------------
    echo Adding filename as title...
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
    local DIR="$1"

    find "$DIR/" -iregex ".*\.\(md\|txt\)" -type f
}

main "$1"
