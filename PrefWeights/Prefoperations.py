from datetime import datetime as dt

def calculateWeighting(users_in_group, rooms, booking_time):
    weighted_rooms = []

    for room in rooms:
        room_free = True
        for booking in room['bookings']:
            temp_time = booking['start']
            temp_time = temp_time[:-5]
            temp_time = dt.strptime(temp_time, "%Y-%m-%dT%H:%M:%S")
            if booking_time == temp_time:
                room_free = False
        if room_free:
            temp_weight = 0
            for user in users_in_group:
                for prefKey in user['preferences']:
                    if prefKey in room['equipment']:
                        temp_weight += user['preferences'][prefKey]
                    else:
                        temp_weight -= user['preferences'][prefKey]
            weighted_rooms.append([room, temp_weight])
        

    return weighted_rooms




