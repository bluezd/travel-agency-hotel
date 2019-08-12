#!C:\Python27\python.exe
# -*- coding: utf8 -*-
import os, sys
if os.path.exists('./lib/python2.7/site-packages/'):
    sys.path.append('./lib/python2.7/site-packages/')

from flask import Flask
from flask_cors import CORS
import json
import time

class Hotel(object):
    def __init__(self, id, name, alias,address, rank, price, date):
        self.ID = id
        self.Name = name
        self.Alias = alias
        self.Address = address
        self.Rank = rank
        self.Price = price
        self.Date = date

def hotel_dict(obj):
    return obj.__dict__


global hotelList
hotelList = []

hotelList.append(Hotel("1","Shangri-La Hotel","SLA","No.66, Renmin Road, Zhongshan, 116001 Dalian, China","5 Star",1001,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("2","Bayshore Hotel Dalian","BHD","No.32 C1 Sector, Xinghaiwan Square, Shahekou, 116001 Dalian, China","5 Star",1000,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("3","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("4","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("5","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("6","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("7","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("8","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("9","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))
hotelList.append(Hotel("10","深圳罗湖智选假日酒店","HLD","罗湖区桂园北路6号","准三星",400,time.strftime("%d/%m/%Y")))

app = Flask(__name__)
CORS(app)

@app.route('/hotels', methods=['GET'])
def getHotels():
    return json.dumps(hotelList, default=hotel_dict).decode('unicode-escape').encode('utf8')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
