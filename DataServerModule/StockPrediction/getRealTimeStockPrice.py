from django.http import HttpResponse
from django.core import serializers
from urllib import request
import json
import re

def getRealTimeStockPrice(request_):
	stockCode = request_.GET['stockcode']
	json_data = json.dumps([''])
	if(stockCode is not None and stockCode != ''):
		url = "http://hq.sinajs.cn/"
		completeUrl = url + "list=sh" + stockCode
		hs = {"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           	 	"Accept-Language" : "zh-CN,zh;q=0.9",
           		"Cache-Control" : "max-age=0",
           		"Connection" : "keep-alive",
           		"Host" : "hq.sinajs.cn",
           		"Upgrade-Insecure-Requests" : "1",
           		"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
           		}
		req = request.Request(completeUrl, headers=hs)
		page = request.urlopen(req,  timeout=8.0).read()
		response_ = page.decode("GBK")
		pattern = re.compile('="(.*)"')
		groupsFound = pattern.findall(response_)
		if groupsFound is not None and len(groupsFound) > 0:
			json_data = json.dumps(groupsFound[0].split(sep=','),ensure_ascii=False)
	return HttpResponse(json_data, content_type='application/json')
