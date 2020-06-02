# CopyModifiedFiles
# Date: 2019-12-17
# Author: tyfanchz

r"""
使用方法：
    1、将修改过的文件列表记录到文本文件中，作为配置文件
    2、运行脚本，输入配置文件路径（可直接拖入）
    3、脚本将自动在目标文件夹中创建目录树，并按照webapp的目录结构将文件复制过去

配置文件格式：
    1、TYPE: `DIST`|`SRC`  `DIST`
        *复制方式，值为`DIST`则复制class文件并按照webapp文件目录存放；
        值为`SRC`则复制源码文件并按照原路径存放
    2、FROM: <FromPath>  ``
        +指定复制的来源文件夹
    3、TO: <ToPath>  `destination`
        *指定复制的目标文件夹
    4、PREFIX: <Prefix>  ``
        *可选，指定要忽略的前缀
    5、WEB: <WebResourcesPrefix>  `web WebRoot`
        *可选，指定Web资源存放的文件夹
    6、RES: <ResourcesPrefix>  `resources`
        *可选，指定resources文件夹
    7、SRC: <SourcePrefixes>  ``
        *可选，指定源代码存放的目录
    -8、其他：-
        -Java或和Java文件一起的文件行用/开头-
        -Web资源文件行`web`或`WebRoot`开头-
        -resources资源文件行用`resources`开头-
配置文件示例：
    ```
    TYPE: DIST
    FROM: /home/tyfanch/project/out
    TO: /home/tyfanch/project/dist
    /cn/abc/def/SomeClass1.java
    /cn/abc/def/SomeClass2.java
    /cn/abc/def/SomeClass3.java
    web/html/somePage1.html
    web/html/somePage2.html
    resources/applicationContext.xml
    resource/mybatis-config.xml
    ```
"""

from typing import List, Dict
import sys
import os
import shutil
import re
import logging


CONFIG_COPY_TYPE: str = 'TYPE'
CONFIG_FROM: str = 'FROM'
CONFIG_TO: str = 'TO'
CONFIG_PREFIX: str = 'PREFIX'
CONFIG_WEB: str = 'WEB'
CONFIG_RES: str = 'RES'
CONFIG_SRC: str = 'SRC'

COPY_TYPE_DIST: str = 'DIST'
COPY_TYPE_SRC: str = 'SRC'

DEF_COPY_TYPE: str = COPY_TYPE_DIST
DEF_WEB_PREFIX: str = 'web WebRoot'
DEF_RESOURCES_PREFIX: str = 'resources'
DEF_SRC_PREFIX: str = ''


class MainClass():
    """主类
    """
    def __init__(self) -> None:
        super().__init__()
        pass

    def main(self, filename: str = '') -> None:
        """复制的主方法。

        通过读取配置文件来复制需要的文件。

        - filename: 配置文件名
        """
        if not os.path.isfile(filename):
            filename = input('Filename: ')

        FileCopier().copyFilesByType(filename, {
            COPY_TYPE_DIST: DistFileCopier(),
            COPY_TYPE_SRC: SrcFileCopier()
        })

        pass


class FileCopier():
    """文件复制的父类
    """
    def __init__(self) -> None:
        super().__init__()
        pass

    def copyFilesByType(self, filename: str,
            fileCopierDict: Dict[str, object]) -> None:
        """根据复制类型来复制文件
        """
        fileLines: List[str] = self.getFileLines(filename)
        copyType: str = self.getCopyType(fileLines)

        if copyType.upper() in fileCopierDict:
            fileCopier = fileCopierDict[copyType]
        else:
            fileCopier = fileCopierDict[DEF_COPY_TYPE]

        fileCopier.copyFiles(filename)

        pass

    def getFileLines(self, filename: str) -> List[str]:
        """获取文件内容，并转化为数组
        """
        fileContent: str = ''
        fileLines: List[str] = []

        # 获取文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            fileContent = file.read()

        # 将文件内容分割存到数组中，不添加空行，
        # 并替换反斜杠为斜杠、去除多余斜杠、去除每行的无效空格
        for line in fileContent.splitlines():
            formattedLine: str = line.replace('\\', '/').strip()

            if formattedLine != '':
                fileLines.append(formattedLine)

        return fileLines
        pass

    def getCopyConfig(self, fileLines: List[str]) -> Dict[str, str]:
        """获取文件中的配置信息
        """
        copyConfig: Dict[str, str] = {
            CONFIG_COPY_TYPE: self.getCopyType(fileLines),
            CONFIG_FROM: self.getFromDir(fileLines),
            CONFIG_TO: self.getToDir(fileLines),
            CONFIG_PREFIX: self.getPrefix(fileLines),
            CONFIG_WEB: self.getWebPrefix(fileLines),
            CONFIG_RES: self.getResourcesPrefix(fileLines),
            CONFIG_SRC: self.getSrcPrefix(fileLines)
        }

        return copyConfig
        pass

    def getCopyType(self, fileLines: List[str]) -> str:
        """获取复制方式信息
        """
        copyType: str = DEF_COPY_TYPE

        for line in fileLines:
            if re.match(CONFIG_COPY_TYPE + r' *:.*', line.upper()):
                copyType = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        return copyType
        pass

    def getFromDir(self, fileLines: List[str]) -> str:
        """获取源文件夹信息
        eg: copy/from/path
        """
        fromDir: str = ''

        for line in fileLines:
            if re.match(CONFIG_FROM + r' *:.*', line.upper()):
                fromDir = line[line.find(':') + 1:].strip()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        if fromDir == '':
            raise Exception('!!!! File does not have `%s` line' % CONFIG_FROM)

        # 删除尾部多余或重复的/
        fromDir = re.sub(r'/+$', '', fromDir, flags=re.IGNORECASE)

        return fromDir
        pass

    def getToDir(self, fileLines: List[str]) -> str:
        """获取目标文件夹信息
        eg: copy/to/path
        """
        toDir: str = 'destination'

        for line in fileLines:
            if re.match(CONFIG_TO + r' *:.*', line.upper()):
                toDir = line[line.find(':') + 1:].strip()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 删除尾部多余或重复的/
        toDir = re.sub(r'/+$', '', toDir, flags=re.IGNORECASE)

        return toDir
        pass

    def getPrefix(self, fileLines: List[str]) -> str:
        """获取所有行的前缀信息，以/结尾
        eg: some/path/of/prefix/
        """
        prefix: str = ''

        for line in fileLines:
            if re.match(CONFIG_PREFIX + r' *:.*', line.upper()):
                prefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 删除尾部多余或重复的/，再加上/
        prefix = re.sub(r'/+$', '', prefix, flags=re.IGNORECASE) + '/'

        return prefix
        pass

    def getWebPrefix(self, fileLines: List[str]) -> str:
        """获取web文件夹的前缀信息，以/结尾
        eg: (^web/|^WebRoot/)
        """
        webPrefix: str = DEF_WEB_PREFIX
        webPrefixItems: List[str] = []
        webPrefixPattern: str = ''

        for line in fileLines:
            if re.match(CONFIG_WEB + r' *:.*', line.upper()):
                webPrefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 将前缀分割重组，组成正则表达式项
        for item in re.split(' +', webPrefix.upper()):
            webPrefixItems.append('^' + re.sub(r'(^/+|/+$)', '',
                item.strip(), flags=re.IGNORECASE) + '/')

        # 组成最终的正则表达式
        webPrefixPattern = '(' + '|'.join(webPrefixItems) + ')'

        return webPrefixPattern
        pass

    def getResourcesPrefix(self, fileLines: List[str]) -> str:
        """获取resources文件夹的前缀信息，以/结尾
        eg: (^res/|^resource/|^resources/)
        """
        resourcesPrefix: str = DEF_RESOURCES_PREFIX
        resourcesPrefixItems: List[str] = []
        resourcesPrefixPattern: str = ''

        for line in fileLines:
            if re.match(CONFIG_RES + r' *:.*', line.upper()):
                resourcesPrefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 将前缀分割重组，组成正则表达式项
        for item in re.split(' +', resourcesPrefix.upper()):
            resourcesPrefixItems.append('^' + re.sub(r'(^/+|/+$)', '',
                item.strip(), flags=re.IGNORECASE) + '/')

        # 组成最终的正则表达式
        resourcesPrefixPattern = '(' + '|'.join(resourcesPrefixItems) + ')'

        return resourcesPrefixPattern
        pass

    def getSrcPrefix(self, fileLines: List[str]) -> str:
        """获取src文件夹前缀信息，以/结尾
        eg: (^/|^src/|^source/|^main/src/)
        """
        srcPrefix: str = DEF_SRC_PREFIX
        srcPrefixItems: List[str] = []
        srcPrefixPattern: str = ''

        for line in fileLines:
            if re.match(CONFIG_SRC + r' *:.*', line.upper()):
                srcPrefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 将前缀分割重组，组成正则表达式项
        for item in re.split(' +', srcPrefix.upper()):
            srcPrefixItems.append('^' + re.sub(r'(^/+|/+$)', '',
                item.strip(), flags=re.IGNORECASE) + '/')

        # 组成最终的正则表达式
        srcPrefixPattern = '(' + '|'.join(srcPrefixItems) + ')'

        return srcPrefixPattern
        pass

    def copyFile(self, baseFromDir: str, baseToDir: str,
        file: str) -> None:
        """复制文件
        """
        fromFile: str = baseFromDir + '/' + file
        toFile: str = baseToDir + '/' + file

        print('---- Copying %s\n     to %s' % (fromFile, toFile))

        try:
            if os.path.isfile(fromFile):
                # 如果fromFile为一个文件则复制
                # 获取目标文件所在目录
                folder: str = os.path.split(toFile)[0]
                # 在目标目录里面创建相应的目录结构
                os.makedirs(folder, exist_ok=True)
                # 复制文件和属性
                shutil.copyfile(fromFile, toFile)
                shutil.copystat(fromFile, toFile)
                print('---- Done.')
            else:
                print('!!!! Not a file.\n\n\n\n')
        except Exception as e:
            print(e)

        pass


class DistFileCopier(FileCopier):
    """复制dist文件的类
    """
    def __init__(self) -> None:
        super().__init__()

    def getWebFiles(self, fileLines: List[str],
        copyConfig: Dict[str, str]) -> List[str]:
        """获取静态资源文件信息
        """
        webFiles: List[str] = []
        prefix: str = copyConfig[CONFIG_PREFIX]
        webPrefix: str = copyConfig[CONFIG_WEB]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部多余的/
            line = re.sub(r'^/+', '', line, flags=re.IGNORECASE)

            if re.match(webPrefix, line.upper()):
                webFiles.append(line[line.find('/') + 1:])

        return webFiles
        pass

    def getResourcesFiles(self, fileLines: List[str],
        copyConfig: Dict[str, str]) -> List[str]:
        """获取资源文件信息
        """
        resourcesFiles: List[str] = []
        prefix: str = copyConfig[CONFIG_PREFIX]
        resourcesPrefix: str = copyConfig[CONFIG_RES]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部多余的/
            line = re.sub(r'^/+', '', line, flags=re.IGNORECASE)

            if re.match(resourcesPrefix, line.upper()):
                resourcesFiles.append(line[line.find('/') + 1:])

        return resourcesFiles
        pass

    def getClassFiles(self, fileLines: List[str],
        copyConfig: Dict[str, str]) -> List[str]:
        """获取.class文件信息
        """
        classFiles: List[str] = []
        prefix: str = copyConfig[CONFIG_PREFIX]
        webPrefix: str = copyConfig[CONFIG_WEB]
        resourcesPrefix: str = copyConfig[CONFIG_RES]
        srcPrefix: str = copyConfig[CONFIG_SRC]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部多余的/
            line = re.sub(r'^/+', '', line, flags=re.IGNORECASE)

            # 如果行内容不是web前缀也不是resources前缀则认为是class文件
            if not re.match(webPrefix, line.upper()) \
                and not re.match(resourcesPrefix, line.upper()):
                # 删除src前缀
                line = re.sub(srcPrefix, '', line, flags=re.IGNORECASE)
                # 并替换后缀.java为.class
                line = re.sub(r'\.java$', '.class', line, flags=re.IGNORECASE)
                # 添加到文件列表中
                classFiles.append(line)

        return classFiles
        pass

    def copyFiles(self, filename: str) -> None:
        """复制文件的总方法
        """
        fileLines: List[str] = self.getFileLines(filename)
        print('$$$$ fileLines: ', fileLines)

        print('==============================================================')
        copyConfig: Dict[str, str] = self.getCopyConfig(fileLines)
        copyType: str = copyConfig[CONFIG_COPY_TYPE]
        fromDir: str = copyConfig[CONFIG_FROM]
        toDir: str = copyConfig[CONFIG_TO]
        webPrefix: str = copyConfig[CONFIG_WEB]
        resourcesPrefix: str = copyConfig[CONFIG_RES]
        srcPrefix: str = copyConfig[CONFIG_SRC]
        print('$$$$ copyConfig: ', copyConfig)
        print('$$$$ copyType: ', copyType)
        print('$$$$ fromDir: ', fromDir)
        print('$$$$ toDir: ', toDir)
        print('$$$$ webPrefix: ', webPrefix)
        print('$$$$ resourcesPrefix: ', resourcesPrefix)
        print('$$$$ srcPrefix: ', srcPrefix)
        webFiles: List[str] = self.getWebFiles(fileLines, copyConfig)
        print('$$$$ webFiles: ', webFiles)
        resourcesFiles: List[str] = self.getResourcesFiles(fileLines,
            copyConfig)
        print('$$$$ resourcesFiles: ', resourcesFiles)
        classFiles: List[str] = self.getClassFiles(fileLines, copyConfig)
        print('$$$$ classFiles: ', classFiles)

        print('==============================================================')
        self.copyWebFiles(fromDir, toDir, webFiles)
        self.copyResourcesFiles(fromDir, toDir, resourcesFiles)
        self.copyClassFiles(fromDir, toDir, classFiles)
        pass

    def copyWebFiles(self, fromDir: str, toDir: str,
        webFiles: List[str]) -> None:
        """复制静态资源文件
        """
        baseFromDir: str = fromDir
        baseToDir: str = toDir

        print('$$$$ Copying web files...')

        for file in webFiles:
            self.copyFile(baseFromDir, baseToDir, file)

        pass

    def copyResourcesFiles(self, fromDir: str, toDir: str,
        resourcesFiles: List[str]) -> None:
        """复制资源文件
        """
        baseFromDir: str = fromDir + '/WEB-INF/classes'
        baseToDir: str = toDir + '/WEB-INF/classes'

        print('$$$$ Copying resources files...')

        for file in resourcesFiles:
            self.copyFile(baseFromDir, baseToDir, file)

        pass

    def copyClassFiles(self, fromDir: str, toDir: str,
        classFiles: List[str]) -> None:
        """复制.class文件
        """
        baseFromDir: str = fromDir + '/WEB-INF/classes'
        baseToDir: str = toDir + '/WEB-INF/classes'

        print('$$$$ Copying class files...')

        for file in classFiles:
            self.copyFile(baseFromDir, baseToDir, file)

        pass


class SrcFileCopier(FileCopier):
    """复制src文件的类
    """
    def __init__(self) -> None:
        super().__init__()
        pass

    def getSrcFiles(self, fileLines: List[str],
        copyConfig: Dict[str, str]) -> list:
        """获取源码文件信息
        """
        srcFiles: List[str] = []
        prefix: str = copyConfig[CONFIG_PREFIX]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部多余的/
            line = re.sub(r'^/+', '', line, flags=re.IGNORECASE)
            srcFiles.append(line)

        return srcFiles
        pass

    def copyFiles(self, filename: str) -> None:
        """复制文件的总方法
        """
        fileLines: List[str] = self.getFileLines(filename)
        print('$$$$ fileLines: ', fileLines)

        print('==============================================================')
        copyConfig: Dict[str, str] = self.getCopyConfig(fileLines)
        copyType: str = copyConfig[CONFIG_COPY_TYPE]
        fromDir: str = copyConfig[CONFIG_FROM]
        toDir: str = copyConfig[CONFIG_TO]
        print('$$$$ copyConfig: ', copyConfig)
        print('$$$$ copyType: ', copyType)
        print('$$$$ fromDir: ', fromDir)
        print('$$$$ toDir: ', toDir)
        srcFiles: List[str] = self.getSrcFiles(fileLines, copyConfig)
        print('$$$$ srcFiles: ', srcFiles)

        print('==============================================================')
        self.copySrcFiles(fromDir, toDir, srcFiles)

        pass

    def copySrcFiles(self, fromDir: str, toDir: str,
        srcFiles: List[str]) -> None:
        """复制源码文件
        """
        baseFromDir: str = fromDir
        baseToDir: str = toDir

        print('$$$$ Copying src files...')

        for file in srcFiles:
            self.copyFile(baseFromDir, baseToDir, file)
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv) >= 2:
        MainClass().main(sys.argv[1])
    else:
        MainClass().main()

    input('#### Finished.')
