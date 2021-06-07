#!/usr/bin/env python

from typing import *
import uuid
import random
import string

class FakeDoc():
    def __init__(self) -> None:
        pass

    @staticmethod
    def generateTextFile(maxLength: int, maxLine: int) -> None:
        fakeDoc: FakeDoc = FakeDoc()
        title: str = fakeDoc.generateTitle()
        textLines: List[str] = ["- %s" % title]
        textLines.extend(fakeDoc.generateText(maxLength, maxLine))
        content: bytes = "\n".join(textLines).encode("utf-8")
        filename: str = title + ".txt"
        fakeDoc.writeToFile(filename, content)

    @staticmethod
    def generateBinaryFile(length: int) -> None:
        fakeDoc: FakeDoc = FakeDoc()
        title: str = fakeDoc.generateTitle() + ".bin"
        content: bytes = fakeDoc.generateBinary(length)
        fakeDoc.writeToFile(title, content)

    def generateTitle(self, ) -> str:
        print("Generating title...")
        title: str = uuid.uuid4().hex
        return title

    def generateText(self, maxLength: int, maxLine: int) -> List[str]:
        print("Generating text content...")
        textContent: List[str] = []
        line: int = random.randint(1, maxLine)
        for _ in range(line):
            length: int = random.randint(1, maxLength)
            textLine:str = "".join([random.choice(string.ascii_letters + string.digits + " .") \
                for _ in range(length)]).strip()
            textLine = "- %s" % textLine
            textContent.append(textLine)
        return textContent

    def generateBinary(self, length: int) -> bytes:
        print("Generating binary content...")
        binaryContent: bytes = random.randbytes(length)
        return binaryContent

    def writeToFile(self, filename: str, content: bytes) -> None:
        print("Writing to %s..." % filename)
        with open(filename, "wb") as file:
            file.write(content)

def main() -> None:
    for _ in range(50):
        FakeDoc.generateTextFile(2048, 1000)
    print("ALL DONE!")

if __name__ == "__main__":
    main()
