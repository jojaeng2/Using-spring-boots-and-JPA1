#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json



#
# Complete the 'getTopRatedFoodOutlets' function below.
#
# URL for cut and paste
# https://jsonmock.hackerrank.com/api/food_outlets?city=<city>&page=<pageNumber>
#
# The function is expected to return an array of strings.
# The function accepts only city argument (String).
#
header_url = 'https://jsonmock.hackerrank.com/api/food_outlets?city='
body_url = '&page='
def getTopRatedFoodOutlets(city):
    res = []
    req = requests.get(header_url+city)
    pages = int(req.json()['total_pages'])
    maxi = 0
    for i in range(1, pages+1):
        main_req = requests.get(header_url+ city + body_url + str(i))
        mj = main_req.json()['data']
        for j in mj:
            maxi = max(maxi, j['user_rating']['average_rating'])
    for i in range(1, pages+1):
        main_req = requests.get(header_url+ city + body_url + str(i))
        mj = main_req.json()['data']
        for j in mj:
            if j['user_rating']['average_rating'] == maxi:
                res.append(j['name'])
    
    
    # Write your code here
    return res
if __name__ == '__main__':