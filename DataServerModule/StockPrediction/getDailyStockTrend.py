from django.http import HttpResponse
from django.core import serializers
from urllib import request
import json
import re

def getDailyStockTrend(request_):
	stockCode = request_.GET['stockcode']
	if stockCode is not None and stockCode != '':
		url = "http://image.sinajs.cn/newchart/daily/n/sh"
		completeUrl = url + stockCode + ".gif"
		hs = {
			"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language" : "zh-CN,zh;q=0.9",
           		"Cache-Control" : "max-age=0",
           		"Connection" : "keep-alive",
           		"Host" : "image.sinajs.cn",
           		"Upgrade-Insecure-Requests" : "1",
           		"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
           	 }
		req = request.Request(completeUrl, headers=hs)
		response = request.urlopen(req,  timeout=8.0).read()
		return HttpResponse(response,content_type="image/gif")
