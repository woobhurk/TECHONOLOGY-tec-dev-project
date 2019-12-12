import urllib.request as urlrequest


class WebPageUtils:
    """
    网页自定义工具类
    """
    def __init__(self):
        """
        生成默认请求头
        """
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/71.0.3578.98 Safari/537.36"
        }

    def getHttpUrlBinary(self, url, headers=None):
        """
        获取URL指向的页面的二进制内容

        :returns: 网页二进制内容
        """
        if headers is None:
            headers = self.headers

        request = urlrequest.Request(url, headers=headers)
        response = urlrequest.urlopen(request)
        responseData = response.read()

        return responseData

    def getHttpUrlText(self, url, headers=None):
        """
        获取URL指向的页面的文本内容

        :returns: 网页内容的字符串
        """
        return self.getHttpUrlBinary(url, headers)

    def saveHttpUrlBinary(self, fileName, responseData):
        self.saveHttpUrlContent(fileName, responseData, "wb")

    def saveHttpUrlText(self, fileName, responseData):
        self.saveHttpUrlContent(fileName, responseData, "wt")

    def saveHttpUrlContent(self, fileName, responseData, mode):
        with open(fileName, mode) as file:
            file.write(responseData)
