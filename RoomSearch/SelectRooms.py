import requests as rq
import PrefWeights.Prefoperations as po
import GPSOperations.GPSOperations as gps
from datetime import date as d
from datetime import time as t
from datetime import datetime as dt
import datetime as DT
import re


def fetchRooms():
    roomsRq = rq.get("http://sds.samchatfield.com/api/room")
    rooms = roomsRq.json()
    return rooms

def fetchUser(userID):
    usersRq = rq.get("http://sds.samchatfield.com/api/user/" + userID)
    users = usersRq.json()
    return users


def evalRooms(weighted_rooms):
    bestRoomID = ""
    bestWeight = -9999999999
    for rooms in weighted_rooms:
        if rooms[1] > bestWeight:
            bestWeight = rooms[1]
            bestRoomID = rooms[0]

    return bestRoomID

def pickRooms(userIDs, bookingTime):

    rooms = fetchRooms()
    userInfo = []
    for user in userIDs:
        userInfo.append(fetchUser(user))

    weighted_rooms = po.calculateWeighting(userInfo, rooms)

    userLocations = []
    for user in userInfo:
        bestTimeDiff = DT.timedelta(5000,50000,500000)
        bestLoc = user["locations"][0]
        for location in user["locations"]:
            timeStr = location["time"]
            timeStr = timeStr[:-5]
            time = dt.strptime(timeStr, "%Y-%m-%dT%H:%M:%S")
            diff_to_booking = bookingTime - time
            if abs(diff_to_booking) < bestTimeDiff:
                bestTimeDiff = diff_to_booking
                bestLoc = location
        userLocations.append(bestLoc)



    for room in weighted_rooms:
        location = room[0]["location"]
        average_distance = gps.calculate_average_distance(location, userLocations)
        dist_weight = 1 / average_distance * 1000
        room[1] -=  dist_weight
    
    best_room = evalRooms(weighted_rooms)
    return best_room["roomId"]

        




if __name__ == "__main__" : pickRooms(["1234567"])





