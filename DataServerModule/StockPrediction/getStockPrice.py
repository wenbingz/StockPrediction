from django.http import HttpResponse
from django.core import serializers
import tushare as ts
import json
from pandas import DataFrame

def get_price_data(request):
        stockCode = getRequestParameter(request, 'stockcode')
        beginDate = getRequestParameter(request, 'begindate')
        endDate = getRequestParameter(request, 'enddate')
        json_date = json.dumps((''))
        if stockCode != '' and beginDate != '' and endDate != '':
                df = ts.get_hist_data(stockCode, beginDate, endDate)
                if df is not None and not df.empty:
                        json_data = df.to_json(orient='split')
                else:
                        json_data = json.dumps(('fectching error'))
        else:
                json_data = json.dumps(('please check your parameter'))
        return HttpResponse(json_data, content_type='application/json')
def getRequestParameter(request, parameterName):
        if request.method=='GET' and parameterName in request.GET:
                return request.GET[parameterName]
        return ''
