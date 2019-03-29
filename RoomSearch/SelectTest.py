import RoomSearch.SelectRooms as sr
from datetime import date as d
from datetime import time as t
from datetime import datetime as dt

class RoomSelectionTests:


    @staticmethod
    def individualTest1():
        userIds = ["1234567"]
        date = d(2019, 3, 21)
        time = t(22,0,0,0)
        bookingTime = dt.combine(date, time)
        bestRoom = sr.pickRooms(userIds, bookingTime)

    def individualTest2():
        userIds = ["1234567"]
        date = d(2019, 4, 21)
        time = t(10,0,0,0)
        bookingTime = dt.combine(date, time)
        bestRoom = sr.pickRooms(userIds, bookingTime)

def main():
    RoomSelectionTests.individualTest()

if __name__ == "__main__" : main()