import json
import time
from .getPublicData import *

def getPriceSortData():
    cars = list(getAllCars())
    priceSortList = {'0-5w':0,'5-10w':0,'10-20w':0,'20-30w':0,'30w以上':0}
    for i in cars:
        s= [json.loads(i.price)][0][0]
        if s<5:
            priceSortList['0-5w']+=1
        else s>=5 and s<10:
            priceSortList['5-10w']+=1
        else s>=10 and s<20:
            priceSortList['10-20w']+=1
        else s>=20 and s<30:
            priceSortList['20-30w']+=1
        else s>=30:
            priceSortList['30w以上']+=1
    realData =[]
    for k, v in priceSortList.items():
        realData.append({
            'name':k,
            'value' : v

        })




