# -*- coding: utf-8 -*-
"""
使用方法：
    1、将修改过的文件列表记录到文本文件中，作为配置文件
    2、运行脚本，输入配置文件路径（可直接拖入）
    3、脚本将自动在目标文件夹中创建目录树，并按照webapp的目录结构将文件复制过去

配置文件格式：
    1、TYPE: DIST|SRC  "DIST"
        *复制方式，值为`DIST`则复制class文件并按照webapp文件目录存放；
        值为`SRC`则复制源码文件并按照原路径存放
    2、FROM: <FromPath>  ""
        +指定复制的来源文件夹
    3、TO: <ToPath>  "desination"
        *指定复制的目标文件夹
    4、PREFIX: <Prefix>  ""
        *可选，指定要忽略的前缀
    5、WEB: <WebResourcesPrefix>  "web|WebRoot"
        *可选，指定Web资源存放的文件夹
    6、RES: <ResourcesPrefix>  "resources"
        *可选，指定resources文件夹
    7、SRC: <SourcePrefixes>  "src"
        *可选，指定源代码存放的目录
    8、其他：
        Java或和Java文件一起的文件行用/开头
        Web资源文件行`web`或`WebRoot`开头
        resources资源文件行用`resources`开头
配置文件示例：
    TYPE: DIST
    FROM: /home/tyfanch/project/out
    TO: /home/tyfanch/project/dist
    /cn/abc/def/SomeClass1.java
    /cn/abc/def/SomeClass2.java
    /cn/abc/def/SomeClass3.java
    web/html/somePage1.html
    web/html/somePage2.html
    resources/applicationCOntext.xml
    resource/mybatis-config.xml
"""

import sys
import os
import shutil
import re


CONFIG_COPY_TYPE = 'TYPE'
CONFIG_FROM = 'FROM'
CONFIG_TO = 'TO'
CONFIG_PREFIX = 'PREFIX'
CONFIG_WEB = 'WEB'
CONFIG_RES = 'RES'
CONFIG_SRC = 'SRC'

COPY_TYPE_DIST = 'DIST'
COPY_TYPE_SRC = 'SRC'

DEF_COPY_TYPE = COPY_TYPE_DIST
DEF_WEB_PREFIX = 'web|WebRoot'
DEF_RESOURCES_PREFIX = 'resources'
DEF_SRC_PREFIX = ''


class MainClass():
    """主类
    """
    def __init__(self):
        super().__init__()
        pass

    def main(self, filename=''):
        """复制的主方法
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
    def __init__(self):
        super().__init__()
        pass

    def copyFilesByType(self, filename, fileCopierDict):
        """根据复制类型来复制文件
        """
        fileLines = self.getFileLines(filename)
        copyType = self.getCopyType(fileLines)

        if copyType.upper() in fileCopierDict:
            fileCopier = fileCopierDict[copyType]
        else:
            fileCopier = fileCopierDict[DEF_COPY_TYPE]

        fileCopier.copyFiles(filename)

        pass

    def getFileLines(self, filename):
        """获取文件内容，并转化为数组
        """
        fileContent = None
        fileLines = []

        # 获取文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            fileContent = file.read()

        # 将文件内容分割存到数组中，不添加空行，
        # 并替换反斜杠为斜杠、去除多余斜杠、去除每行的无效空格
        # fileLines = [line.replace('\\', '/').strip()
        #     for line in fileContent.splitlines()]
        for line in fileContent.splitlines():
            formattedLine = line.replace('\\', '/').strip()

            if formattedLine != '':
                fileLines.append(formattedLine)

        return fileLines
        pass

    def getCopyConfig(self, fileLines):
        """获取文件中的配置信息
        """
        copyConfig = {
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

    def getCopyType(self, fileLines):
        """获取复制方式信息
        """
        copyType = DEF_COPY_TYPE

        for line in fileLines:
            if re.match(CONFIG_COPY_TYPE + ' *:.*', line.upper()):
                copyType = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        return copyType
        pass

    def getFromDir(self, fileLines):
        """获取源文件夹信息
        eg: copy/from/path
        """
        fromDir = ''

        for line in fileLines:
            if re.match(CONFIG_FROM + ' *:.*', line.upper()):
                fromDir = line[line.find(':') + 1:].strip()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        if fromDir == '':
            raise Exception('!!!! File does not have `%s` line' % CONFIG_FROM)

        # 删除尾部多余或重复的/
        fromDir = re.sub(r'/+$', '', fromDir)

        return fromDir
        pass

    def getToDir(self, fileLines):
        """获取目标文件夹信息
        eg: copy/to/path
        """
        toDir = 'destination'

        for line in fileLines:
            if re.match(CONFIG_TO + ' *:.*', line.upper()):
                toDir = line[line.find(':') + 1:].strip()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 删除尾部多余或重复的/
        toDir = re.sub(r'/+$', '', toDir)

        return toDir
        pass

    def getPrefix(self, fileLines):
        """获取所有行的前缀信息，以/结尾
        eg: some/path/of/prefix/
        """
        prefix = ''

        for line in fileLines:
            if re.match(CONFIG_PREFIX + ' *:.*', line.upper()):
                prefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 删除尾部多余或重复的/，再加上/
        prefix = re.sub(r'/+$', '', prefix) + '/'

        return prefix
        pass

    def getWebPrefix(self, fileLines):
        """获取web文件夹的前缀信息，以/结尾
        eg: (^web/|^WebRoot/)
        """
        webPrefix = DEF_WEB_PREFIX
        webPrefixItems = []
        webPrefixPattern = ''

        for line in fileLines:
            if re.match(CONFIG_WEB + ' *:.*', line.upper()):
                webPrefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # # 删除首尾多余或重复的/，再加上/
        # webPrefix = re.sub(r'(^/+|/+$)', '', webPrefix) + '/'

        # 将前缀分割重组，组成正则表达式项
        for item in webPrefix.upper().split('|'):
            webPrefixItems.append('^' + re.sub(r'(^/+|/+$)', '', item.strip())
                + '/')

        # 组成最终的正则表达式
        webPrefixPattern = '(' + '|'.join(webPrefixItems) + ')'

        return webPrefixPattern
        pass

    def getResourcesPrefix(self, fileLines):
        """获取resources文件夹的前缀信息，以/结尾
        eg: (^res/|^resource/|^resources/)
        """
        resourcesPrefix = DEF_RESOURCES_PREFIX
        resourcesPrefixItems = []
        resourcesPrefixPattern = ''

        for line in fileLines:
            if re.match(CONFIG_RES + ' *:.*', line.upper()):
                resourcesPrefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 删除首尾多余或重复的/，再加上/
        # resourcesPrefix = re.sub(r'(^/+|/+$)', '', resourcesPrefix) + '/'

        # 将前缀分割重组，组成正则表达式项
        for item in resourcesPrefix.upper().split('|'):
            resourcesPrefixItems.append('^' + re.sub(r'(^/+|/+$)', '', item.strip())
                + '/')

        # 组成最终的正则表达式
        resourcesPrefixPattern = '(' + '|'.join(resourcesPrefixItems) + ')'

        return resourcesPrefixPattern
        pass

    def getSrcPrefix(self, fileLines):
        """获取src文件夹前缀信息，以/结尾
        eg: (^src/|^source/|^main/src/)
        """
        srcPrefix = DEF_SRC_PREFIX
        srcPrefixItems = []
        srcPrefixPattern = ''

        for line in fileLines:
            if re.match(CONFIG_SRC + ' *:.*', line.upper()):
                srcPrefix = line[line.find(':') + 1:].strip().upper()

                try:
                    fileLines.remove(line)
                except Exception as e:
                    print(e)

                break

        # 删除首尾多余或重复的/，再加上/
        # srcPrefix = re.sub(r'(^/+|/+$)', '', srcPrefix) + '/'

        # 将前缀分割重组，组成正则表达式项
        for item in srcPrefix.upper().split('|'):
            srcPrefixItems.append('^' + re.sub(r'(^/+|/+$)', '', item.strip())
                + '/')

        # 组成最终的正则表达式
        srcPrefixPattern = '(' + '|'.join(srcPrefixItems) + ')'

        return srcPrefixPattern
        pass

    def copyFile(self, baseFromDir, baseToDir, file):
        """复制文件
        """
        fromFile = baseFromDir + '/' + file
        toFile = baseToDir + '/' + file

        print('---- Copying %s\n     to %s' % (fromFile, toFile))

        try:
            if os.path.isfile(fromFile):
                # 如果fromFile为一个文件则复制
                # 获取目标文件所在目录
                folder = os.path.split(toFile)[0]
                # 在目标目录里面创建相应的目录结构
                os.makedirs(folder, exist_ok=True)
                # 复制文件
                shutil.copyfile(fromFile, toFile)
                print('---- Done.')
            else:
                print('!!!! Not a file.')
        except Exception as e:
            print(e)

        pass


class DistFileCopier(FileCopier):
    """复制dist文件的类
    """
    def __init__(self):
        super().__init__()

    def getWebFiles(self, fileLines, copyConfig):
        """获取静态资源文件信息
        """
        webFiles = []
        prefix = copyConfig[CONFIG_PREFIX]
        webPrefix = copyConfig[CONFIG_WEB]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部的/
            line = re.sub(r'^/', '', line)

            if re.match(webPrefix, line.upper()):
                webFiles.append(line[line.find('/') + 1:])

        return webFiles
        pass

    def getResourcesFiles(self, fileLines, copyConfig):
        """获取资源文件信息
        """
        resourcesFiles = []
        prefix = copyConfig[CONFIG_PREFIX]
        resourcesPrefix = copyConfig[CONFIG_RES]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部的/
            line = re.sub(r'^/', '', line)

            if re.match(resourcesPrefix, line.upper()):
                resourcesFiles.append(line[line.find('/') + 1:])

        return resourcesFiles
        pass

    def getClassFiles(self, fileLines, copyConfig):
        """获取.class文件信息
        """
        classFiles = []
        prefix = copyConfig[CONFIG_PREFIX]
        webPrefix = copyConfig[CONFIG_WEB]
        resourcesPrefix = copyConfig[CONFIG_RES]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            # 去掉头部的/
            line = re.sub(r'^/', '', line)

            # 如果行内容不是web前缀也不是resources前缀则认为是class文件
            if not re.match(webPrefix, line.upper()) \
                and not re.match(resourcesPrefix, line.upper()):
                # 添加到文件列表中，并替换后缀.java为.class
                classFiles.append(re.sub(r'\.java$', '.class', line))

        return classFiles
        pass

    def copyFiles(self, filename):
        """复制文件的总方法
        """
        fileLines = self.getFileLines(filename)
        print('$$$$ fileLines: ', fileLines)

        print('==============================================================')
        copyConfig = self.getCopyConfig(fileLines)
        copyType = copyConfig[CONFIG_COPY_TYPE]
        fromDir = copyConfig[CONFIG_FROM]
        toDir = copyConfig[CONFIG_TO]
        webPrefix = copyConfig[CONFIG_WEB]
        resourcesPrefix = copyConfig[CONFIG_RES]
        print('$$$$ copyConfig: ', copyConfig)
        print('$$$$ copyType: ', copyType)
        print('$$$$ fromDir: ', fromDir)
        print('$$$$ toDir: ', toDir)
        print('$$$$ webPrefix: ', webPrefix)
        print('$$$$ resourcesPrefix: ', resourcesPrefix)
        webFiles = self.getWebFiles(fileLines, copyConfig)
        print('$$$$ webFiles: ', webFiles)
        resourcesFiles = self.getResourcesFiles(fileLines, copyConfig)
        print('$$$$ resourcesFiles: ', resourcesFiles)
        classFiles = self.getClassFiles(fileLines, copyConfig)
        print('$$$$ classFiles: ', classFiles)

        print('==============================================================')
        self.copyWebFiles(fromDir, toDir, webFiles)
        self.copyResourcesFiles(fromDir, toDir, resourcesFiles)
        self.copyClassFiles(fromDir, toDir, classFiles)
        pass

    def copyWebFiles(self, fromDir, toDir, webFiles):
        """复制静态资源文件
        """
        baseFromDir = fromDir
        baseToDir = toDir

        print('$$$$ Copying web files...')

        for file in webFiles:
            self.copyFile(baseFromDir, baseToDir, file)

        pass

    def copyResourcesFiles(self, fromDir, toDir, resourcesFiles):
        """复制资源文件
        """
        baseFromDir = fromDir + '/WEB-INF/classes'
        baseToDir = toDir + '/WEB-INF/classes'

        print('$$$$ Copying resources files...')

        for file in resourcesFiles:
            self.copyFile(baseFromDir, baseToDir, file)

        pass

    def copyClassFiles(self, fromDir, toDir, classFiles):
        """复制.class文件
        """
        baseFromDir = fromDir + '/WEB-INF/classes'
        baseToDir = toDir + '/WEB-INF/classes'

        print('$$$$ Copying class files...')

        for file in classFiles:
            self.copyFile(baseFromDir, baseToDir, file)

        pass


class SrcFileCopier(FileCopier):
    """复制src文件的类
    """
    def __init__(self):
        super().__init__()
        pass

    def getSrcFiles(self, fileLines, copyConfig):
        """获取源码文件信息
        """
        srcFiles = []
        prefix = copyConfig[CONFIG_PREFIX]

        for line in fileLines:
            # 去掉前缀
            if line.upper().startswith(prefix):
                line = line[len(prefix):]

            srcFiles.append(re.sub(r'^/+', '', line))

        return srcFiles
        pass

    def copyFiles(self, filename):
        """复制文件的总方法
        """
        fileLines = self.getFileLines(filename)
        print('$$$$ fileLines: ', fileLines)

        print('==============================================================')
        copyConfig = self.getCopyConfig(fileLines)
        copyType = copyConfig[CONFIG_COPY_TYPE]
        fromDir = copyConfig[CONFIG_FROM]
        toDir = copyConfig[CONFIG_TO]
        print('$$$$ copyConfig: ', copyConfig)
        print('$$$$ copyType: ', copyType)
        print('$$$$ fromDir: ', fromDir)
        print('$$$$ toDir: ', toDir)
        srcFiles = self.getSrcFiles(fileLines, copyConfig)
        print('$$$$ srcFiles: ', srcFiles)

        print('==============================================================')
        self.copySrcFiles(fromDir, toDir, srcFiles)

        pass

    def copySrcFiles(self, fromDir, toDir, srcFiles):
        """复制源码文件
        """
        baseFromDir = fromDir
        baseToDir = toDir

        print('$$$$ Copying src files...')

        for file in srcFiles:
            self.copyFile(baseFromDir, baseToDir, file)
        pass


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        MainClass().main(sys.argv[1])
    else:
        MainClass().main()

    input('#### Finished.')
