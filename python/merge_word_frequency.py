# encoding: utf-8

from typing import List, Dict
import sys
import os
import logging


BASE_DIR: str = "D:/Users/tyfanchz/Desktop"
FLYPY_DIR: str = "tyz_flypy.dict"
WUBI_DIR: str = "tyz_wubi86.dict"


class App:
    def __init__(self) -> None:
        super().__init__()
        pass

    def main(self):

        pass

    def scanFiles(self, subDir: str) -> List[str]:
        pass

    def readFileHeader(self, fileName: str) -> str:
        pass

    def readFileLines(self, fileName: str) -> List[str]:
        pass

    def splitFileLines(self, fileLines: List[str]) -> List[str]:
        pass

    def mergeWordFrequency(self, flypyLineParts: List[str], wubiLineParts: List[str]) -> str:
        pass

    def writeFileLines(self, fileName: str, fileHeader: str, fileLines: List[str]) -> None:
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    App().main()
    input("#### Finished.")
