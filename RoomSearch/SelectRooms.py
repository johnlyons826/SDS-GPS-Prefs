import requests as rq
import PrefWeights.Prefoperations as po
import GPSOperations.GPSOperations as gps


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

def pickRooms(userIDs):

    rooms = fetchRooms()
    userInfo = []
    for user in userIDs:
        userInfo.append(fetchUser(user))

    weighted_rooms = po.calculateWeighting(userInfo, rooms)

    userLocations = []
    for user in userInfo:
        userLocations.append(user["locations"][0])

    for room in weighted_rooms:
        location = room[0]["location"]
        average_distance = gps.calculate_average_distance(location, userLocations)
        dist_weight = 1 / average_distance * 1000
        room[1] -=  dist_weight
    
    best_room = evalRooms(weighted_rooms)
    return best_room["roomId"]

        




if __name__ == "__main__" : pickRooms(["1234567"])





