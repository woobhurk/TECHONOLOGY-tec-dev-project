#!/bin/env bash

function main() {
    FILE="$1"

    convert "$FILE" "$FILE.csv"
}

function convert() {
    FILE="$1"
    OUT_FILE="$2"

    # 1 2. 替换掉 | 和空格
    # 3. 替换掉 NULL 字符串
    # 4. 删除表头和数据之间的分割行
    sed -E -e "s/ +\| +/\",\"/g" \
        -e "s/(\| +| +\|)/\"/g" \
        -e "s/\"\bNULL\b\"/null/g" \
        -e "/^\+-+.*-+\+\$/d" \
        "$FILE" > "$OUT_FILE"
}

main "$@"
