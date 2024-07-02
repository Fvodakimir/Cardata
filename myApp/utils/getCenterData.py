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

def getRollData():
    cars = list(getAllCars())
    carBrand = {}
    for i in cars:
        if carBrand.get(i.brand, -1) == -1:
            carBrand[str(i.brand)] = 1
        else:
            carBrand[str(i.brand)] += 1
    brandList = [(value, key) for  key, value in carBrand.items()]
    brandList = sorted(brandList,reverse=True)[:10]
    sortDict = {i[1]: i[0] for i in brandList}
    lastSortList = []
    for k, v in sortDict.items():
        lastSortList.append({
            'name' : k,
            'value' : v
        })
    return lastSortList

def getTypeRate():
    cars = list(getAllCars())
    carTypes = {}
    for i in cars:
        if carTypes.get(i.energyType, -1) == -1:
            carTypes[str(i.energyType)] = 1
        else:
            carTypes[str(i.energyType)] += 1
    oilRate = round(carTypes['汽油']/567 * 100,2)
    electricRate = round(carTypes['纯电动']/567 * 100,2)
    mixRate = round(100 - oilRate - electricRate, 2)
    return oilRate,electricRate,mixRate
