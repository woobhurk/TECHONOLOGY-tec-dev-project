#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import sqlite3
import zlib
import re
import logging
from datetime import datetime
from sqlite3.dbapi2 import Connection, Cursor
from typing import *
from FileUtils import FileUtils

class RvfExtractHelper(object):
    def __init__(self) -> None:
        super().__init__()

    def main(self, argv: List[str]):
        logging.basicConfig(level=logging.INFO)
        try:
            argvDbName: str = argv[1] if len(argv) >= 2 else ""
            dbName: str = self.readDbName(argvDbName)
            outputDir: str = self.initOutputDir(dbName)
            dbConnection, dbCursor = self.connectDb(dbName)
            self.queryRecords(dbCursor)
            self.saveAllRecords(outputDir, dbCursor)
            self.closeDb(dbConnection, dbCursor)
        except Exception as e:
            logging.exception("!!!! ERROR:", e)

    def main2(self, argv: List[str]) -> None:
        logging.basicConfig(level=logging.INFO)
        try:
            argvBasePath: str = argv[1] if len(argv) >= 2 else ""
            basePath: str = self.readBasePath(argvBasePath)
            dbFileList: List[str] = self.buildDbFileList(basePath)
        except Exception as e:
            logging.exception("!!!! ERROR:", e)

    def readBasePath(self, argvBasePath: str) -> str:
        """- 获取存储路径（文件或文件夹）。

        - param
            - `argvBasePath` 命令行传入的存储路径
        - return 获取到的存储路径（文件或文件夹）
        """
        return FileUtils.inputPath("Input SQLite DB file or dir: ", argvBasePath)

    def buildDbFileList(self, basePath: str) -> List[str]:
        """- 生成路径下所有 db 文件的列表。

        - param
            - `basePath` 存储路径
        - return 该路径下所有的 db 文件
        """
        dbFileList: List[str] = FileUtils.listAllPaths(basePath, type=FileUtils.FILE, \
            extList=["db"])
        logging.info("Building db file list finished.")
        return dbFileList

    def readDbName(self, argvDbName: str) -> str:
        """- 获取数据库名称。

        - param
            - `argvDbName` 命令行传入的数据库名称
        - return 获取到的数据库名称
        """
        #dbName: str = ""
        #if os.path.isfile(argvDbName):
        #    dbName = argvDbName.replace("\\", "/")
        #else:
        #    dbName = input("Input SQLite DB File: ").replace("\\", "/")
        #if not os.path.isfile(dbName):
        #    raise FileNotFoundError("Invalid file: %s" % dbName)
        #return dbName
        return FileUtils.inputPath("Input SQLite DB File: ", argvDbName, type=FileUtils.FILE)

    def initOutputDir(self, dbName: str) -> str:
        """- 初始化存储文件夹。

        - param
            - `dbName` 数据库文件名
        - return 要存储到的目标文件夹
        """
        # 存储到数据库同名文件夹下，路径相同
        prefix: str = os.path.splitext(dbName)[0]
        # 加上时间戳前缀
        suffix: str = datetime.now().strftime("%Y%m%d-%H%M%S")
        outputDir: str = prefix + '-' + suffix
        if not os.path.isdir(outputDir):
            os.makedirs(outputDir)
        logging.info("outputDir = %s" % outputDir)
        return outputDir

    def connectDb(self, dbName: str) -> Tuple[Connection, Cursor]:
        """- 连接到数据库。

        - param
            - `dbName` 数据库文件名
        - return 元组，参数为 (数据库连接, 数据库游标)
        """
        dbConnection: Connection = sqlite3.connect(dbName)
        dbCursor: Cursor = dbConnection.cursor()
        logging.info("Database %s opened." % dbName)
        return (dbConnection, dbCursor)

    def queryRecords(self, dbCursor: Cursor) -> Cursor:
        """- 查询数据库。

        - param
            - `dbCursor` 数据库游标
        - return 游标
        """
        sql: str = """
        select c.`fid` id, c.`内容` content, t.`标题` title
        from `资料库` c
        left join `标题` t on t.`ID` = c.`fid`
        where t.`标题` != '说明文档'
            and content is not null
        """
        dbCursor.execute(sql)
        logging.info("Records fetched %s, %s, %s." \
            % (dbCursor.arraysize, dbCursor.rowcount, dbCursor.lastrowid))
        return dbCursor

    def saveAllRecords(self, outputDir: str, dbCursor: Cursor) -> None:
        """- 保存所有记录中的数据。

        - param
            - `outputDir` 存储文件夹
            - `dbCursor` 数据库游标
        """
        for row in dbCursor:
            logging.info("Saving row %s %s..." % (row[0], row[2]))
            filename, content = self.__extractRecord(row)
            self.__writeFile(outputDir, filename, content)
        logging.info("DONE!")

    def closeDb(self, dbConnection: Connection, dbCursor: Cursor) -> None:
        """- 关闭数据库。

        - param
            - `dbConnection` 数据库连接
        """
        if dbCursor != None:
            dbCursor.close()
        if dbConnection != None:
            dbConnection.close()

    def __extractRecord(self, row: Any) -> Tuple[str, bytes]:
        """- 解析记录，生成文件名和文件内容。

        - param
            - `row` 记录
        """
        id: int = row[0]
        data: Any = row[1]
        title: str = row[2]
        filename: str = "%s-%s" % (id, title)
        content: bytes = zlib.decompress(data)
        return (filename, content)

    def __writeFile(self, outputDir: str, filename: str, content: bytes) -> None:
        """- 写入记录到文件中。

        - param
            - `outputDir` 存储文件夹
            - `filename` 文件名
            - `content` 内容
        """
        # 替换掉不合法文件名的字符
        legalFilename: str = re.sub(r"[\\/:*?<>|]", "_", filename)
        # 替换尾部多余的 _ 和空格
        legalFilename = re.sub(r"_+$", "", legalFilename).strip()
        rvfFilename: str = "%s/%s.rvf" % (outputDir, legalFilename)
        with open(rvfFilename, "wb") as file:
            file.write(content)
            logging.info("Saved file: %s" % rvfFilename)

if __name__ == "__main__":
    RvfExtractHelper().main(sys.argv)
