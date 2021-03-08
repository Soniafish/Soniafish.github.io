# !/usr/bin/python2
# coding:utf-8

import urllib.request as request
import ssl    
import json
ssl._create_default_https_context = ssl._create_unverified_context

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
# src="https://data.taipei/api/v1/dataset/36847f3f-deff-4183-a5bb-800737591de5?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response)
    # print(data)
    alist=data["result"]["results"]
    # print(alist)

with open("data.txt", mode="w", encoding="utf-8") as file:
    for item in alist:
        itemFile = item["file"]
        itemImgSrc = itemFile.split('http://')
        # print(item["stitle"], item["longitude"], item["latitude"], "http://"+itemImgSrc[1])
        str = item["stitle"]+', '+item["longitude"]+', '+item["latitude"]+', '+'http://'+itemImgSrc[1]
        file.write(str+'\n')