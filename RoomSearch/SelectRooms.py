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

def createClusters(locations):
    clusters = []
    for point1 in locations:
        point1Neighbours = [point1]
        for point2 in locations:
            if point1 != point2:
                dist = gps.calculateDistance(point1, point2)
                if dist < 0.25:
                    point1Neighbours.append(point2)
                
        clusters.append(point1Neighbours)
    biggestCluster = []
    for cluster in clusters:
        if len(cluster) > len(biggestCluster):
            biggestCluster = cluster
    return biggestCluster
                    
def bumpPrefs(best_room, userInfo):
    prefs_to_bump = []
    for equipment in best_room['equipment']:
        prefs_to_bump.append(equipment)

    preferences = userInfo[0]['preferences']
    user_prefs = []
    for pref in preferences:
        user_prefs.append([pref, preferences[pref]])


    for (pref,score) in user_prefs:
        if pref in prefs_to_bump:
            score += 0.05
            if score > 1:
                score = 1.0
    return user_prefs

def pickRooms(userIDs, bookingTime):

    rooms = fetchRooms()
    userInfo = []
    for user in userIDs:
        userInfo.append(fetchUser(user))

    weighted_rooms = po.calculateWeighting(userInfo, rooms, bookingTime)

    userLocations = []
    for user in userInfo:
        if user['locations'] != []:
        
            bestTimeDiff = 9999999.0
            bestLoc = user["locations"][0]
            for location in user["locations"]:
                timeStr = location["time"]
                timeStr = timeStr[:-5]
                time = dt.strptime(timeStr, "%Y-%m-%dT%H:%M:%S")

                user_weekday = time.weekday()
                booking_weekday = bookingTime.weekday()
                user_hour = time.hour
                booking_hour = bookingTime.hour
                day_diff = abs(user_weekday - booking_weekday)
                hour_diff = abs(user_hour - booking_hour)
                diff_to_booking = day_diff + 1/24 * hour_diff
                if abs(diff_to_booking) < bestTimeDiff:
                    bestTimeDiff = diff_to_booking
                    bestLoc = location
            userLocations.append(bestLoc)

    biggestCluster = createClusters(userLocations)
    if len(biggestCluster) > 1:
        userLocations = biggestCluster


    for room in weighted_rooms:
        location = room[0]["location"]
        average_distance = gps.calculate_average_distance(location, userLocations)
        dist_weight = 1 / average_distance * 1000
        room[1] +=  dist_weight
    
    #best_room = evalRooms(weighted_rooms)
    best_rooms = sorted(weighted_rooms, key=lambda x: x[1], reverse=True)
    cur_num = 0
    results= []

    for i in range (0,3):
        if i >= len(best_rooms):
            break
        temp_dict = {}
        temp_dict["roomId"] =  best_rooms[i][0]["roomId"]
        temp_dict["Score"] = best_rooms[i][1]
        results.append(temp_dict)

    #bumped = bumpPrefs(best_room, userInfo)
    

  
    return results

        




if __name__ == "__main__" : pickRooms(["1234567"])





