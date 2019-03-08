#class for representing locations
class GPSLocation:

    def __init__(self):
        self.latitude = 0;
        self.longitude = 0;

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def getLat(self):
        return self.latitude
    
    def getLong(self):
        return self.longitude