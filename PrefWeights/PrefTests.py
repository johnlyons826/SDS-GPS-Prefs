import PrefWeights.Prefoperations as po
import RoomSearch.SelectRooms as rs

class PreferenceTests:
    @staticmethod
    def weightingTest():
        users = [rs.fetchUser("1234567")]
        rooms = rs.fetchRooms()
        weighted_rooms = po.calculateWeighting(users, rooms)
        print(weighted_rooms)


def main():
    PreferenceTests.weightingTest()


if __name__ == "__main__" : main()