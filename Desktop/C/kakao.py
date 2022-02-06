#-*- coding: utf-8 -*- 
import requests
import random
import json

url = 'https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users/'
token = 'e5b9b9b5af484bf123c5ae9620f36d03'
path = 'start'
headers = {'X-Auth-Token' : token, 'Content-Type' : 'application/json; charset=utf-8'}


arr = [[0 for i in range(5)] for j in range(5)]

trucks = []
fulls = []
lows = []
empties = []

def getLocation():
    #"locations" : [
    #   {"id" : 0, "located_bikes_count" : 3},
    # ]
    global fulls, lows, empties, arr
    fulls = []
    lows = []
    empties = []
    response = requests.get(url+"locations", headers = headers)
    for loc in response.json()["locations"]:
        arr[4-loc["id"]%5][int(loc["id"]/5)] = loc["located_bikes_count"]
        if loc["located_bikes_count"] >= 3:
            fulls.append(loc["id"])
        elif loc["located_bikes_count"] <= 1:
            lows.append(loc["id"])
        # elif loc["located_bikes_count"] == 0:
        #     empties.append(loc["id"])
    return response

def getTrucks():
    #트럭 id, 현재 위치, 싣고 있는 자전거 수
    # "trucks" : [
    #     {"id" : 0, "location_id":0, "loaded_bikes_count" : 0},
    # ]

    response = requests.get(url+"trucks", headers = headers)
    return response

def simulate(commands):
    # {
    #     "status" : "ready",
    #     "time" : 1,
    #     "faled_resquests_count" : 5,
    #     "distance" : 1.2,
    # }

    data = {"commands" : commands}
    response = requests.put(url + "simulate", headers = headers, data = json.dumps(data))
    return response


def score():
    response = requests.get(url + "score", headers = headers)
    return response

def setting():
    commands = []
    commands.append({"truck_id" : 0, "command" : [1, 1]})
    commands.append({"truck_id" : 1, "command" : [2, 1, 1]})
    commands.append({"truck_id" : 2, "command" : [2, 2, 1, 1]})
    commands.append({"truck_id" : 3, "command" : [2, 2, 2, 1, 1]})
    commands.append({"truck_id" : 4, "command" : [2, 2, 2, 2, 1, 1]})
    return commands

def trans(fr, to):
    minDist = 99999
    minId = -1
    minLoc = -1
    for truck in trucks["trucks"]:
        if truck["id"] == -1:
            continue
        dist = getDist(truck["location_id"], fr)
        if minDist > dist:
            minDist = dist
            minId = truck["id"]
            minLoc = truck["location_id"]

    command = []
    if minId == -1:
        return None
    
    command = move(minLoc, fr) + [5] + move(fr, to) + [6]

    if len(command > 10):
        command[9] = 6
    
    ret = {"truck_id" : minId, "command" : command}

    for truck in trucks["trucks"]:
        if truck["id"] == minId:
            truck["id"] = -1
    return ret

def move(fr, to):
    ret = []
    while fr != to:
        if (4- fr % 5) < (4-to%5):
            fr -= 1
            ret.append(3)
        elif (4-fr % 5) > (4 - to % 5):
            ret.append(1)
            fr += 1
        elif int(fr/5) < int(to/5):
            ret.append(2)
            fr += 5
        elif int(fr/5) > int(to/5):
            ret.append(4)
            fr -= 5
        else:
            break
    return ret

def start():
    data = {}
    data["problem"] = 2
    response = requests.post(url + "start", headers = headers, data = json.dumps(data))
    key = response.json()["auth_key"]

    headers["Authorization"] = key
    print(key)
    return response

def getDist(first, second):
    return abs((4-first%5) - (4-second%5)) + abs(int(first/5) - int(second/5))

if __name__ == "__main__":
    start()

    while True:
        commands = []
        sim = simulate(commands).json()
        print(sim)
        
        if(sim["status"] == "finished"):
            break


        commands = []

        getLocation()
        trucks = getTrucks().json()
        # commands + goToHot()
        