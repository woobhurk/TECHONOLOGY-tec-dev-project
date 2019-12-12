# -*- coding: utf-8 -*-
import sys
import os
import shutil

"""
使用方法：
    1、将修改过的文件列表记录到txt文件中，作为配置文件
        1.1、复制方式用`TYPE:`开头，值可以是：
            src：按照源代码路径复制
            dist：按照webapp路径复制
            默认为dist
        1.2、源文件夹行用`FROM:`开头
        1.3、目标文件夹行用`TO:`开头，可以不存在
        1.4、静态资源文件行使用`web`或者`WebRoot`开头
        1.5、resource文件行使用`resources`开头
        1.6、class文件行使用`/`开头
    2、运行脚本，拖入配置文件
    3、脚本将自动在目标文件夹中创建目录树，并按照webapp的目录结构将文件复制过去
"""


class MainClass():
    def __init__(self):
        super().__init__()
        pass

    def main(self, fileType, filename):
        """复制的主方法
        """
        if not os.path.isfile(filename):
            filename = input('Filename: ')

        self.copyFilesByType(fileType, filename)

        pass

    def copyFilesByType(self, fileType, filename):
        """通过制定文件类型来复制不同的文件
        """
        if fileType == 'src':
            fileCopier = SrcFileCopier()
        else:
            fileCopier = DistFileCopier()

        fileCopier.copyFiles(filename)

        pass


class FileCopier():
    def __init__(self):
        super().__init__()
        pass

    def getFileContentLines(self, filename):
        """获取文件内容，并转化为数组
        """
        fileContent = None
        fileContentLines = []

        # 获取文件内容
        with open(filename, 'r', encoding='utf-8') as file:
            fileContent = file.read()

        # 将文件内容分割存到数组中
        fileContentLines = fileContent.splitlines()

        # 替换反斜杠为斜杠，并去除每行的无效空格
        for i in range(len(fileContentLines)):
            fileContentLines[i] = fileContentLines[i].replace('\\', '/') \
                .strip()

        return fileContentLines
        pass

    # def getFileType(self, fileContentLines):
    #     """获取复制方式信息"""
    #     fileType = 'DIST'

    #     for line in fileContentLines:
    #         if line.upper().startswith('TYPE'):
    #             fileType = line[line.find(':') + 1:].strip()
    #             break

    #     return fileType
    #     pass

    def getFromDir(self, fileContentLines):
        """获取源文件夹信息
        """
        fromDir = ''

        for line in fileContentLines:
            if line.upper().startswith('FROM'):
                fromDir = line[line.find(':') + 1:].strip()
                break

        if fromDir == '':
            raise Exception('!!!! File does not have `FROM:` line')

        if not fromDir.endswith('/'):
            fromDir += '/'

        return fromDir
        pass

    def getToDir(self, fileContentLines):
        """获取目标文件夹信息
        """
        toDir = ''

        for line in fileContentLines:
            if line.upper().startswith('TO'):
                toDir = line[line.find(':') + 1:].strip()
                break

        if toDir == '':
            raise Exception('!!!! File does not have `TO:` line')

        if not toDir.endswith('/'):
            toDir += '/'

        return toDir
        pass

    def getPrefix(self, fileContentLines):
        """获取所有行的前缀信息
        """
        prefix = ''

        for line in fileContentLines:
            if line.upper().startswith('PREFIX'):
                prefix = line[line.find(':') + 1:].strip()
                break;

        if not prefix.endswith('/'):
            prefix += '/'

        return prefix
        pass

    def getWebPrefix(self, fileContentLines):
        """获取web文件夹的前缀信息
        """
        webPrefix = 'web'

        for line in fileContentLines:
            if line.upper().startswith('WEB'):
                webPrefix = line[line.find(':') + 1:].strip()
                break;

        webPrefix.replace('/', '')

        return webPrefix
        pass

    def getResourcePrefix(self, fileContentLines):
        """获取resources文件夹的前缀信息
        """
        resourcePrefix = 'resources'

        for line in fileContentLines:
            if line.upper().startswith('RES'):
                resourcePrefix = line[line.find(':') + 1:].strip()
                break;

        resourcePrefix.replace('/', '')

        return resourcePrefix
        pass

    def copyFile(self, baseFromDir, baseToDir, file):
        """复制文件
        """
        fromFile = baseFromDir + file
        toFile = baseToDir + file

        print('---- Copying %s\n     to %s' % (fromFile, toFile))

        try:
            if os.path.isfile(fromFile):
                # 如果源文件为一个文件则复制
                folder = os.path.split(toFile)[0]
                # 在目标目录里面创建相应的目录结构
                os.makedirs(folder, exist_ok=True)
                # 复制文件
                shutil.copyfile(fromFile, toFile)
                print('---- Copied.')
        except Exception as e:
            print(e)

        pass


class SrcFileCopier(FileCopier):
    def __init__(self):
        super().__init__()
        pass

    def copyFiles(self, filename):
        print('==============================================================')
        fileContentLines = super().getFileContentLines(filename)
        print('fileContentLines: ', fileContentLines)
        print('==============================================================')
        fromDir = super().getFromDir(fileContentLines)
        print('fromDir: ', fromDir)
        print('==============================================================')
        toDir = super().getToDir(fileContentLines)
        print('toDir: ', toDir)
        print('==============================================================')
        allFiles = self.getAllFiles(fileContentLines)
        print('allFiles: ', allFiles)
        print('==============================================================')
        self.copyAllFiles(fromDir, toDir, allFiles)

        pass

    def getAllFiles(self, fileContentLines):
        allFiles = []

        for line in fileContentLines:
            if line.startswith('/'):
                # 去除行头的/
                allFiles.append(line[1:])

        return allFiles
        pass

    def copyAllFiles(self, fromDir, toDir, allFiles):
        baseFromDir = fromDir
        baseToDir = toDir

        print('$$$$ Copying all files...')

        for file in allFiles:
            super().copyFile(baseFromDir, baseToDir, file)
        pass


class DistFileCopier(FileCopier):
    def __init__(self):
        super().__init__()

    def copyFiles(self, filename):
        print('==============================================================')
        fileContentLines = super().getFileContentLines(filename)
        print('fileContentLines: ', fileContentLines)
        print('==============================================================')
        fromDir = super().getFromDir(fileContentLines)
        print('fromDir: ', fromDir)
        print('==============================================================')
        toDir = super().getToDir(fileContentLines)
        print('toDir: ', toDir)
        print('==============================================================')
        webPrefix = super().getWebPrefix(fileContentLines)
        print('webPrefix: ', webPrefix)
        print('==============================================================')
        resourcePrefix = super().getResourcePrefix(fileContentLines)
        print('resourcePrefix: ', resourcePrefix)
        print('==============================================================')
        staticFiles = self.getStaticFiles(fileContentLines)
        print('staticFiles: ', staticFiles)
        print('==============================================================')
        resourceFiles = self.getResourceFiles(fileContentLines)
        print('resourceFiles: ', resourceFiles)
        print('==============================================================')
        classFiles = self.getClassFiles(fileContentLines)
        print('classFiles: ', classFiles)
        print('==============================================================')
        self.copyStaticFiles(fromDir, toDir, staticFiles)
        self.copyResourceFiles(fromDir, toDir, resourceFiles)
        self.copyClassFiles(fromDir, toDir, classFiles)
        pass

    def getStaticFiles(self, fileContentLines):
        """获取静态资源文件信息
        """
        staticFiles = []

        for line in fileContentLines:
            if line.upper().startswith('WEB/') \
                or line.upper().startswith('WEBROOT/'):
                staticFiles.append(line[line.find('/') + 1:])

        return staticFiles
        pass

    def getResourceFiles(self, fileContentLines):
        """获取资源文件信息
        """
        resourceFiles = []

        for line in fileContentLines:
            if line.upper().startswith('RESOURCES/'):
                resourceFiles.append(line[line.find('/') + 1:])

        return resourceFiles
        pass

    def getClassFiles(self, fileContentLines):
        """获取.class文件信息
        """
        classFiles = []

        for line in fileContentLines:
            if line.startswith('/') and line.endswith('.java'):
                classFiles.append(line[1:-5] + '.class')
            elif line.startswith('/'):
                classFiles.append(line[line.find('/') + 1:])

        return classFiles
        pass

    def copyStaticFiles(self, fromDir, toDir, staticFiles):
        """复制静态资源文件
        """
        baseFromDir = fromDir
        baseToDir = toDir

        print('$$$$ Copying static files...')

        for file in staticFiles:
            super().copyFile(baseFromDir, baseToDir, file)

        pass

    def copyResourceFiles(self, fromDir, toDir, resourceFiles):
        """复制资源文件
        """
        baseFromDir = fromDir + 'WEB-INF/classes/'
        baseToDir = toDir + 'WEB-INF/classes/'

        print('$$$$ Copying resource files...')

        for file in resourceFiles:
            super().copyFile(baseFromDir, baseToDir, file)

        pass

    def copyClassFiles(self, fromDir, toDir, classFiles):
        """复制.class文件
        """
        baseFromDir = fromDir + 'WEB-INF/classes/'
        baseToDir = toDir + 'WEB-INF/classes/'

        print('$$$$ Copying class files...')

        for file in classFiles:
            super().copyFile(baseFromDir, baseToDir, file)

        pass


if __name__ == "__main__":
    MainClass().main(sys.argv[1], sys.argv[2])
    input('#### Finished.')
