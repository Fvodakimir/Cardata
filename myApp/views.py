from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import getPublicData
from .utils import getCenterData
from .utils import getCenterLeftData
from.utils import getCenterRightData

def center(request):
    if request.method == 'GET':
        sumCar,highVolume,topCar,mostBrand,mostModel,averagePrice = getCenterData.getBaseData()
        lastSortList = getCenterData.getRollData()
        getCenterData.getTypeRate()
        oilRate,electricRate,mixRate = getCenterData.getTypeRate()
        return JsonResponse({
            'sumCar' : sumCar,
            'highVolume' : highVolume,
            'topCar' : topCar,
            'mostBrand' : mostBrand,
            'mostModel' : mostModel,
            'averagePrice' : averagePrice,
            'lastSortList': lastSortList,
            'oilRate' : oilRate,
            'electricRate' : electricRate,
            'mixRate' : mixRate
        })
def centerLeft(request):
    if request.method == 'GET':
        lastPieList = getCenterLeftData.getPieBrandData()
        return JsonResponse({
            'lastPieList':lastPieList

        })
def centerRight(request):
    if request.method == 'GET':
        realData= getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData':realData


        })
