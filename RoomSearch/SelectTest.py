import RoomSearch.SelectRooms as sr
from datetime import date as d
from datetime import time as t
from datetime import datetime as dt

class RoomSelectionTests:


    @staticmethod
    def individualTest():
        userIds = ["1234567"]
        date = d(2019, 3, 16)
        time = t(12,0,0,0)
        bookingTime = dt.combine(date, time)
        bestRoom = sr.pickRooms(userIds, bookingTime)
        
        assert(bestRoom == "LIBRARY-148")




def main():
    RoomSelectionTests.individualTest()

if __name__ == "__main__" : main()