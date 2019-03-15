from math import sin, cos, sqrt, atan2, radians



def calculate_average_distance(destination, team_locations):
    total_dist = 0

    # Approx radius of earth
    R = 6373.0
    
    end_lat = radians(destination.getLat())
    end_long = radians(destination.getLong())
    i = 0;
    for location in team_locations:
        # Long and Lat given by app are in degrees, therefore convert to radians
        start_long = radians(location.getLong())
        start_lat = radians(location.getLat())

        dlon = end_long - start_long
        dlat = end_lat - start_lat

        a = sin(dlat / 2)**2 + cos(start_lat) * cos(end_lat) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        i = i + 1
        total_dist += distance

    average_dist = total_dist / i
    return average_dist

    
