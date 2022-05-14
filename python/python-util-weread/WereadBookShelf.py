#!/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os
import sys
import time
from typing import *


class WereadBookShelf():
    OUTPUT_FILE_PATH: str = "%s/微信读书书架-%s.md"
    BOOK_SHELF_INFO: str = "- **%s**\n"
#    BOOK_INFO: str = \
#"""    - 书名：%s
#        - 作者：%s
#        - 封面：%s
#        - 进度：%s
#"""
    BOOK_INFO: str = "    - 书名：%s\n" \
        + "        - 作者：%s\n" \
        + "        - 封面：![%s](%s)\n" \
        + "        - 进度：%s%%\n"

    def __init__(self) -> None:
        super().__init__()

    def main(self, argv: List[str]) -> None:
        logging.basicConfig(level=logging.INFO)
        try:
            inputFilePath: str = self.__getFilePath(argv[1] if len(argv) > 1 else "", \
                "JSON file path: ")
            self.__checkFilePath(inputFilePath)
            outputFilePath: str = self.__generateOutputFilePath(inputFilePath)
            jsonObj: Dict[str, Any] = self.readJsonFile(inputFilePath)
            bookAndShelfList: List[Dict[str, Any]] = self.getBookAndShelfList(jsonObj)
            self.writeBookAndShelfInfo(outputFilePath, bookAndShelfList)
        except Exception as e:
            logging.exception("!!!! ERROR", e)
        pass

    def readJsonFile(self, inputFilePath: str="") -> Dict[str, Any]:
        """读取 JSON 文件并转换成字典
        """
        with open(inputFilePath, "rt", encoding="utf-8") as f:
            jsonObj: Dict[str, Any] = json.load(f)
            return jsonObj

    def getBookAndShelfList(self, jsonObj: Dict[str, Any]) -> List[Dict[str, Any]]:
        """获取字典对象中的书籍分组信息
        """
        bookShelfList: List[Dict[str, Any]] = jsonObj["shelf"]["booksAndArchives"]
        # 没有 archiveId 属性的对象不是分组，要过滤掉
        return [i for i in bookShelfList if "archiveId" in i]

    def writeBookAndShelfInfo(self, outputFilePath: str, bookShelfList: List[Dict[str, Any]]) \
            -> None:
        """将解析的书籍信息写入文件中
        """
        with open(outputFilePath, "wt+", encoding="utf-8") as f:
            self.__writeFileTitle(outputFilePath, f)
            for bookShelf in bookShelfList:
                self.__writeBookShelfInfo(f, bookShelf)
                self.__writeBookInfo(f, bookShelf)

    def __getFilePath(self, path: str, prompt: str) -> str:
        """获取有效的文件路径
        """
        filePath: str = path if os.path.isfile(path) else input(prompt)
        return filePath

    def __checkFilePath(self, filePath: str) -> None:
        """校验文件路径是否有效
        """
        if not os.path.isfile(filePath):
            raise FileNotFoundError("File not found: %s" % (filePath))

    def __generateOutputFilePath(self, inputFilePath: str) -> str:
        """生成输出文件路径
        """
        (inputDirPath, _) = os.path.split(inputFilePath)
        outputFilePath: str = self.OUTPUT_FILE_PATH % (inputDirPath, time.strftime("%Y%m%d"))
        return outputFilePath

    def __writeFileTitle(self, outputFilePath: str, outputFile: IO[Any]) -> None:
        """写入文件标题
        """
        (_, outputFilename) = os.path.split(outputFilePath)
        (fileTitle, _) = os.path.splitext(outputFilename)
        content: str = "- %s\n" % (fileTitle)
        outputFile.write(content)

    def __writeBookShelfInfo(self, outputFile: IO[Any], bookShelf: Dict[str, Any]) -> None:
        """写入书籍分组信息
        """
        shelfName: str = bookShelf["name"]
        content: str = self.BOOK_SHELF_INFO % (shelfName)
        outputFile.write(content)

    def __writeBookInfo(self, outputFile: IO[Any], bookShelf: Dict[str, Any]) -> None:
        """写入书籍信息
        """
        bookInfoList: List[Dict] = bookShelf["bookInfos"]
        for  bookInfo in bookInfoList:
            title: str = bookInfo["title"]
            author: str = bookInfo["author"]
            cover: str = bookInfo["cover"]
            progress: str = bookInfo["progress"]
            content: str = self.BOOK_INFO % (title, author, title, cover, progress)
            outputFile.write(content)

if __name__ == "__main__":
    WereadBookShelf().main(sys.argv)
