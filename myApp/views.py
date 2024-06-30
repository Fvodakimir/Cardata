from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .utils import getPublicData
from .utils import getCenterData

def center(request):
    if request.method == 'GET':
        getCenterData.getBaseData()
        return JsonResponse()