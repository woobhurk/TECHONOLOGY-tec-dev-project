#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import logging
from typing import *
from FileUtils import FileUtils

class JpgExtractHelper(object):
    def __init__(self) -> None:
        super().__init__()

    def main(self, argv: List[str]) -> None:
        logging.basicConfig(level=logging.INFO)
        try:
            argvBasePath: str = argv[1] if len(argv) >= 2 else ""
            basePath: str = self.readBasePath(argvBasePath)
            rvfFileList: List[str] = self.buildRvfFileList(basePath)
            self.extractAll(rvfFileList)
        except Exception as e:
            logging.exception("!!!! ERROR", e)

    def readBasePath(self, argvBasePath: str) -> str:
        """- 获取存储路径（文件或文件夹）。

        - param
            - `argvBasePath` 命令行传入的存储路径
        - return 获取到的存储路径（文件或文件夹）
        """
        return FileUtils.inputPath("Input rvf file or dir: ", argvBasePath)

    def buildRvfFileList(self, basePath: str) -> List[str]:
        """- 生成路径下所有 rvf 文件的列表。

        - param
            - `basePath` 存储路径
        - return 该路径下所有的 rvf 文件
        """
        rvfFileList: List[str] = FileUtils.listAllPaths(basePath, type=FileUtils.FILE, \
            extList=["rvf"])
        logging.info("Building rvf file list finished.")
        return rvfFileList

    def extractAll(self, rvfFileList: List[str]) -> None:
        """- 提取 rvf 文件中所有的 jpg 文件。

        - param
            - `rvfFileList` rvf 文件列表
        """
        for rvfFile in rvfFileList:
            jpgDataList: List[bytes] = []
            if self.isRvfTextFile(rvfFile):
                jpgDataList = self.__readJpgTextData(rvfFile)
            else:
                jpgDataList = self.__readJpgBinaryData(rvfFile)
            self.__saveAllJpgFiles(rvfFile, jpgDataList)
        logging.info("DONE!")

    def isRvfTextFile(self, rvfFile: str) -> bool:
        """- 判断 rvf 文件是文本类型还是二进制类型。

        - param
            - `rvfFile` rvf 文件
        - return 是否是文本类型
        """
        return FileUtils.isFileTypeText(rvfFile)

    def __readJpgTextData(self, rvfFile: str) -> List[bytes]:
        """- 从文本型 rvf 文件中提取 jpg 文件。

        - param
            - `rvfFile` rvf 文件
        - return 提取到的 jpg 二进制数据列表
        """
        logging.info("Extracting jpg text from %s..." % rvfFile)
        jpgDataList: List[bytes] = []
        with open(rvfFile, "rt", encoding="utf-8") as f:
            lineList: List[str] = f.readlines()
            index: int = 1
            while index < len(lineList):
                prevLine: str = lineList[index - 1].strip()
                currentLine: str = lineList[index].strip()
                if prevLine == "TJPEGImage":
                    jpgDataList.append(bytes.fromhex(currentLine))
                index += 1
        return jpgDataList

    def __readJpgBinaryData(self, rvfFile: str) -> List[bytes]:
        logging.info("Extracting jpg binary from %s..." % rvfFile)
        jpgHeader: bytes = b"\xff\xd8\xff\xe0"
        jpgTail: bytes = b"\xff\xd9"
        jpgDataList: List[bytes] = []
        rvfFileSize: int = os.path.getsize(rvfFile)
        with open(rvfFile, "rb") as f:
            index: int = 0
            while index < rvfFileSize:
                f.seek(index)
                data = f.read(4)
                if data == jpgHeader:
                    jpgData: bytes = data
                    index += 4
                    data = f.read(2)
                    while data != jpgTail and index < rvfFileSize:
                        jpgData += bytes([data[0]])
                        index += 1
                        f.seek(index)
                        data = f.read(2)
                    jpgData += jpgTail
                    index += 2
                    jpgDataList.append(jpgData)
                else:
                    index += 1
        return jpgDataList

    def __saveAllJpgFiles(self, rvfFile: str, jpgDataList: List[bytes]) -> None:
        """- 保存所有 jpg 文件数据。

        - param
            - `rvfFile` rvf 文件
            - `jpgDataList` jpg 二进制数据列表
        """
        index: int = 0
        while index < len(jpgDataList):
            jpgFile: str = "%s_%s.jpg" % (os.path.splitext(rvfFile)[0], index + 1)
            jpgData: bytes = jpgDataList[index]
            self.__saveJpgFile(jpgFile, jpgData)
            index += 1

    def __saveJpgFile(self, jpgFile: str, jpgData: bytes) -> None:
        """- 保存 jpg 文件。

        - param
            - `jpgFile` jpg 文件名
            - `jpgData` 文件内容
        """
        with open(jpgFile, "wb") as f:
            f.write(jpgData)

if __name__ == "__main__":
    JpgExtractHelper().main(sys.argv)
