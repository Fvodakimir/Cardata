import json
import time
from .getPublicData import *

def getPriceSortData():
    cars = list(getAllCars())
    priceSortList = {'0-5萬':0,'5-10萬':0,'10-20萬':0,'20-30萬':0,'30萬以上':0}
    for i in cars:
        s= [json.loads(i.price)][0][0]
        if s<5:
            priceSortList['0-5萬']+=1
        elif s>=5 and s<10:
            priceSortList['5-10萬']+=1
        elif s>=10 and s<20:
            priceSortList['10-20萬']+=1
        elif s>=20 and s<30:
            priceSortList['20-30萬']+=1
        elif s>=30:
            priceSortList['30萬以上']+=1
    realData =[]
    for k, v in priceSortList.items():
        realData.append({
            'name':k,
            'value' : v
        })
    return realData





