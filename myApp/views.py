from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import getPublicData
from .utils import getCenterData
from .utils import getCenterLeftData
from .utils import getBottomLeftData
from.utils import getCenterRightData
from .utils import getCenterChangeData
from .utils import getBottomRightData

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

def bottomLeft(request):
    if request.method == 'GET':
        brandList,volumeList,priceList = getBottomLeftData.getSquareData()
        return JsonResponse({
            'brandList':brandList,
            'volumeList':volumeList,
            'priceList':priceList
        })

def centerRight(request):
    if request.method == 'GET':
        realData= getCenterRightData.getPriceSortData()
        return JsonResponse({
            'realData':realData
        })
def bottomRight(request):
    if request.method == 'GET':
        carData = getBottomRightData.getRankData()
        return JsonResponse({
            'carData':carData
        })

def centerRightChange(request, energyType):
    if request.method == 'GET':
        oilData, electricData = getCenterChangeData.getCircleData()
        realData = []
        if energyType == 1:
            realData = oilData
        else:
            realData = electricData
        return JsonResponse({
            'realData':realData
        })
