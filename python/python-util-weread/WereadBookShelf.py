#!/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import os
import re
import sys
import time
from typing import *

"""
- 使用方式：
    - 登录网页端微信读书，打开控制台，执行代码：
        - `fetch('https://i.weread.qq.com/shelf/friendCommon?userVid=15962203', {method: 'GET', credentials: "include"}).then(o => o.text()).then(o => console.warn(o))`
    - 复制输出的文本为 book-info.json 文件（里面包含书籍的信息）
    - 点击“我的书架”，在控制台将 `/web/shelf` 请求返回的数据保存为 html
    - 打开 html 文件，搜索 `__INITIAL_STATE__`，复制这个变量值，保存为 book-group.json 文件（里面包含书籍所在分组）
    - 运行本脚本，依次将 book-group.json book-info.json 路径作为参数传入

- 更新日志：
    - 2024-02-06
        - 由于微信更新， `/web/shelf` 返回的信息中不再包含书籍信息，仅包含分组，因此需要配合 `/shelf/friendCommon` 接口返回的书籍信息来匹配
        - 参考：https://www.cnblogs.com/cloudbird/p/12683546.html
"""
class WereadBookShelf():
    OUTPUT_FILE_PATH: str = "%s/微信读书书架-%s.md"
    BOOK_GROUP_INFO: str = "- **%s**\n"
    BOOK_INFO: str = "    - **《{title}》**\n" \
        + "        - 作者：{author}\n" \
        + "        - 封面：![{title}]({cover})\n" \
        + "        - 分类：{category}\n" \
        + "        - 出版日期：{publishTime}\n"

    def __init__(self) -> None:
        super().__init__()

    def main(self, argv: List[str]) -> None:
        logging.basicConfig(level=logging.INFO)
        try:
            bookGroupFilePath: str = self.__getFilePath(argv[1] if len(argv) > 1 else "", \
                "Book group json file path: ")
            self.__checkFilePath(bookGroupFilePath)
            bookInfoFilePath: str = self.__getFilePath(argv[2] if len(argv) > 2 else "", \
                "Book info json file path: ")
            self.__checkFilePath(bookInfoFilePath)
            outputFilePath: str = self.__buildOutputFilePath(bookGroupFilePath)
            bookGroupJsonObj: Dict[str, Any] = self.readJsonFile(bookGroupFilePath)
            bookGroups: List[Dict[str, Any]] = self.buildBookGroups(bookGroupJsonObj)
            bookInfoJsonObj: Dict[str, Any] = self.readJsonFile(bookInfoFilePath)
            bookInfoMap: Dict[str, Any] = self.buildBookInfoMap(bookInfoJsonObj)
            self.writeBookAndShelfInfo(outputFilePath, bookGroups, bookInfoMap)
        except Exception as e:
            logging.exception("!!!! ERROR", e)
        pass

    def readJsonFile(self, inputFilePath: str="") -> Dict[str, Any]:
        """读取 JSON 文件并转换成字典
        """
        with open(inputFilePath, "rt", encoding="utf-8") as f:
            jsonObj: Dict[str, Any] = json.load(f)
            return jsonObj

    def buildBookGroups(self, bookGroupJsonObj: Dict[str, Any]) -> List[Dict[str, Any]]:
        """构建书籍分组信息
        - 返回：[{name="分组名", bookIds=[书籍 id, ...]}, ...]
        """
        bookGroupInfoList: List[Dict[str, Any]] = bookGroupJsonObj["shelf"]["booksAndArchives"]
        # 没有 archiveId 属性的对象不是分组，要过滤掉
        return [{"name": i["name"], "bookIds": i["bookIds"]} \
                for i in bookGroupInfoList if "archiveId" in i]

    def buildBookInfoMap(self, bookInfoJsonObj: Dict[str, Any]) -> Dict[str, Any]:
        """构建书籍信息
        - 返回：{书籍 id: {书籍信息}}
        """
        bookInfoList: List[Dict[str, Any]] = bookInfoJsonObj["recentBooks"]
        # 没有 bookId 属性的对象不是书籍，要过滤掉
        return {i["bookId"]: i for i in bookInfoList if "bookId" in i}

    def writeBookAndShelfInfo(self, outputFilePath: str, bookGroups: List[Dict[str, Any]], \
            bookInfoMap: Dict[str, Any]) -> None:
        """将解析的书籍信息写入文件中
        """
        with open(outputFilePath, "wt+", encoding="utf-8") as f:
            self.__writeFileTitle(outputFilePath, f)
            for bookGroup in bookGroups:
                self.__writeBookGroupInfo(f, bookGroup)
                self.__writeBookInfo(f, bookGroup["bookIds"], bookInfoMap)

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

    def __buildOutputFilePath(self, inputFilePath: str) -> str:
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

    def __writeBookGroupInfo(self, outputFile: IO[Any], bookGroup: Dict[str, Any]) -> None:
        """写入书籍分组信息
        """
        groupName: str = bookGroup["name"]
        content: str = self.BOOK_GROUP_INFO % groupName
        outputFile.write(content)

    def __writeBookInfo(self, outputFile: IO[Any], bookIds: List[str], bookInfoMap: Dict[str, Any]) \
            -> None:
        """写入书籍信息
        """
        for bookId in bookIds:
            bookInfo: Dict[str, Any] = bookInfoMap[bookId]
            contentMap: Dict[str, str] = {
                "title": bookInfo["title"],
                "author": bookInfo["author"],
                "cover": bookInfo["cover"],
                "category": bookInfo["categories"][0]["title"] \
                    if "categories" in bookInfo and len(bookInfo["categories"]) > 0 \
                    else "",
                "publishTime": re.sub(" .*", "", bookInfo["publishTime"]),
            }
            content: str = self.BOOK_INFO.format(**contentMap)
            outputFile.write(content)

if __name__ == "__main__":
    WereadBookShelf().main(sys.argv)
