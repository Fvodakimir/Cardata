from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import getPublicData
from .utils import getCenterData

def center(request):
    if request.method == 'GET':
        sumCar,highVolume,topCar,mostBrand,mostModel,averagePrice = getCenterData.getBaseData()
        return JsonResponse({
            'sumCar' : sumCar,
            'highVolume' : highVolume,
            'topCar' : topCar,
            'mostBrand' : mostBrand,
            'mostModel' : mostModel,
            'averagePrice' : averagePrice
        })