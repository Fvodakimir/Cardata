import json
import time
from .getPublicData import *

def getBaseData():
    cars = list(getAllCars())
    sumCar = len(cars)
    highVolume = cars[0].saleVolume
    topCar = cars[0].carName
    carModels = {}
    maxModel = 0
    mostModel = ''
    for i in cars:
        if carModels.get(i.carModel,-1) == -1:
            carModels[str(i.carModel)] = 1
        else:
            carModels[str(i.carModel)] += 1
    carModels = sorted(carModels.items(),key=lambda x:x[1],reverse=True)
    mostModel = carModels[0][0]
    carBrand = {}
    maxBrand = 0
    mostBrand = ''
    for i in cars:
        if carBrand.get(i.brand, -1) == -1:
            carBrand[str(i.brand)] = 1
        else:
            carBrand[str(i.brand)] += 1
    for k,v in carBrand.items():
        if v > maxBrand:
            maxBrand = v
            mostBrand = k
    carPrices = {}
    averagePrice = 0
    sumPrice = 0
    for i in cars:
        x = json.loads(i.price)[0] + json.loads(i.price)[1]
        sumPrice += x
    averagePrice = sumPrice / (sumCar * 2)
    averagePrice = round(averagePrice,2)
    #print(sumCar,highVolume,topCar,mostBrand,mostModel,averagePrice)
    return sumCar,highVolume,topCar,mostBrand,mostModel,averagePrice
