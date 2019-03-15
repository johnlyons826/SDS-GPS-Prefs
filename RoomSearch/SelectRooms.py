import requests as rq
import PrefWeights.Prefoperations as po


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
    best_room = evalRooms(weighted_rooms)
    return best_room

        




if __name__ == "__main__" : pickRooms(["1234567"])





