import RoomSearch.SelectRooms as sr

class RoomSelectionTests:


    @staticmethod
    def individualTest():
        userIds = ["1234567"]
        bestRoom = sr.pickRooms(userIds)
        
        assert(bestRoom == "CS-225")




def main():
    RoomSelectionTests.individualTest()

if __name__ == "__main__" : main()