

def calculateWeighting(users_in_group, rooms):
    weighted_rooms = []
    for room in rooms:
        temp_weight = 0
        for user in users_in_group:
            for prefKey in user['preferences']:
                if prefKey in room['equipment']:
                    temp_weight += user['preferences'][prefKey]
                else:
                    temp_weight -= user['preferences'][prefKey]
        weighted_rooms.append([room, temp_weight])
        

    return weighted_rooms




