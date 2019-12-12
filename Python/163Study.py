import urllib.parse as urlparse
import urllib.request as urlrequest
import json

reqHeaders = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    #"Host":"study.163.com",
    #"Origin":"https://study.163.com",
    #"Referer":"https://study.163.com/courses",
    #"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
}

rawReqData = {
    "keyword":"",
    "pageIndex":1,
    "pageSize":50,
    "relativeOffset":0,
    "searchTimeType":-1,
    "orderType":50,
    "priceType":-1,
    "activityId":0,
    "qualityType":0
}

#encodedReqData = urlparse.urlencode(rawReqData).encode('utf-8')
encodedReqData = json.dumps(rawReqData).encode('utf-8')
request = urlrequest.Request('https://study.163.com/p/search/studycourse.json', encodedReqData, reqHeaders)
response = urlrequest.urlopen(request)
print(response.read().decode('utf-8'))
