"""StockPrediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import getStockPrice
from . import getRealTimeStockPrice
from . import getStockNews
from . import getRealTimeStockTrend
from . import getDailyStockTrend
from . import getWeeklyStockTrend
from django.urls import path

urlpatterns = [
    path('getStockPrice/', getStockPrice.get_price_data),
    path('getRealTimeStockPrice/', getRealTimeStockPrice.getRealTimeStockPrice),
    path('getStockNews/', getStockNews.getStockNews),
    path('getRealTimeStockTrend/', getRealTimeStockTrend.getRealTimeStockTrend),
    path('getDailyStockTrend/', getDailyStockTrend.getDailyStockTrend),
    path('getWeeklyStockTrend/', getWeeklyStockTrend.getWeeklyStockTrend),
]
