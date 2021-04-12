import os
import random

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from fake_useragent import UserAgentError

from com.tyfanchz.meizitu.WebPageUtils import WebPageUtils


class MzituScraper:
    """
    抓取妹子图（https://www.mzitu.com/all）下的所有图片
    """
    def __init__(self):
        """
        初始化fake_useragent实例
        """
        print("Initializing...")
        try:
            self.fakeUserAgent = UserAgent()
        except UserAgentError:
            self.fakeUserAgent = None
            print("Unable to resolve random User-Agent, use default.")

    def main(self):
        """
        主要处理方法
        """
        urlContent = self.resolveMainContent()
        imageAnchorDict = self.buildImageAnchorDict(urlContent)
        self.buildImageSeriesDict(imageAnchorDict)

    def resolveMainContent(self):
        """
        获取/all页面下的内容

        :returns: /all页面内容
        """
        print("---- initBeautifulSoup")
        webPageUtils = WebPageUtils()
        url = "https://www.mzitu.com/all"
        urlContent = webPageUtils.getHttpUrlText(url, headers=self.generateHostHeaders())
        return urlContent

    def buildImageAnchorDict(self, urlContent):
        """
        建立/all所有图片系列页面的字典，格式为：{SeriesTitle: SeriesUrl}

        :returns: 建立的字典
        """
        print("---- buildImageAnchorDict")
        # 获取/all页面内容
        beautifulSoup = BeautifulSoup(urlContent, "lxml")
        # 获取页面下的所有图片集锚点
        imageAnchorList = beautifulSoup.find("div", class_="all").find_all("a")
        # 删除第一个`早期`锚点
        imageAnchorList.pop(0)
        imageAnchorDict = dict()

        for imageAnchor in imageAnchorList:
            imageSeriesTitle = imageAnchor.get_text()
            imageSeriesUrl = imageAnchor['href']
            imageAnchorDict[imageSeriesTitle] = imageSeriesUrl

        return imageAnchorDict

    def buildImageSeriesDict(self, imageAnchorDict):
        """
        建立所有图片系列的图片文件地址字典，格式为：{SeriesTitle: [SeriesImageUrl_1, SeriesImageUrl_2, ...]}
        """
        print("---- buildImageSeriesDict")
        imageSeriesDict = dict()

        for (imageSeriesTitle, imageSeriesUrl) in imageAnchorDict.items():
            print("Current series: " + imageSeriesUrl)
            imageSeriesDict[imageSeriesTitle] = self.resolvePerImageUrlList(imageSeriesUrl)
            self.saveImages(imageSeriesTitle, imageSeriesDict[imageSeriesTitle])

    def resolvePerImageUrlList(self, imageSeriesUrl):
        """
        建立单个图片系列的图片文件列表

        :returns: 生成的图片文件url列表
        """
        print("---- resolveSingleImageUrlList")
        webPageUtils = WebPageUtils()
        imageUrlContent = webPageUtils.getHttpUrlText(imageSeriesUrl, headers=self.generateHostHeaders())
        beautifulSoup = BeautifulSoup(imageUrlContent, "lxml")
        imageUrlList = []
        # 获取图片页数
        imageUrlCount = int(beautifulSoup.find("div", class_="pagenavi").find_all("span")[-2].get_text())

        for imagePageNum in range(imageUrlCount + 1):
            imagePageUrl = imageSeriesUrl + "/" + str(imagePageNum)
            urlContent = webPageUtils.getHttpUrlText(imagePageUrl, headers=self.generateHostHeaders())
            beautifulSoup = BeautifulSoup(urlContent, "lxml")
            # 得到实际图片文件地址
            imageUrl = beautifulSoup.find("div", class_="main-image").find("img")['src']
            imageUrlList.append(imageUrl)
            print("    " + imageUrl)

        return imageUrlList

    def saveImages(self, imageSeriesTitle, imageUrlList):
        """
        保存图片
        """
        print("---- saveImages")
        webPageUtils = WebPageUtils()
        imageFolder = "./images/" + imageSeriesTitle
        os.makedirs(imageFolder, exist_ok=True)

        for imageUrl in imageUrlList:
            imageContent = webPageUtils.getHttpUrlBinary(imageUrl, headers=self.generatePicHeaders())

            with open(imageFolder + "/" + imageUrl[imageUrl.rindex("/") + 1:], "wb") as imageFile:
                imageFile.write(imageContent)
                print("    " + imageFile.name + " saved.")

    def generateHostHeaders(self):
        """
        生成随机的网页访问请求头

        :returns: 随机的请求头
        """
        hostHeaders = {
            "User-Agent": self.generateRandomUserAgent(),
            "Referer": "https://www.mzitu.com"
        }

        print("---- " + str(hostHeaders))
        return hostHeaders

    def generatePicHeaders(self):
        """
        生成随机的图片访问请求头

        :returns: 随机的请求头
        """
        picHeaders = {
            "User-Agent": self.generateRandomUserAgent(),
            "Referer": "https://i.meizitu.net"
        }

        print("---- " + str(picHeaders))
        return picHeaders

    def generateRandomUserAgent(self):
        """
        生成随机User-Agent

        :returns: 随机的User-Agent
        """
        userAgent = ""

        # 如果随机User-Agent无效则使用默认User-Agent
        if self.fakeUserAgent is None:
            userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                        "AppleWebKit/537.36 (KHTML, like Gecko) " \
                        "Chrome/71.0.3578.98 " \
                        "Safari/537.36 " \
                        "OPR/58.0.3135.59 (Edition beta)"
        else:
            rand = random.Random()
            randNum = rand.randint(0, 4)

            if randNum == 0:
                userAgent = self.fakeUserAgent.chrome
            elif randNum == 1:
                userAgent = self.fakeUserAgent.firefox
            elif randNum == 2:
                userAgent = self.fakeUserAgent.opera
            elif randNum == 3:
                userAgent = self.fakeUserAgent.edge
            elif randNum == 4:
                userAgent = self.fakeUserAgent.ie

            userAgent = self.fakeUserAgent.random

        # print("---- " + userAgent)
        return userAgent
