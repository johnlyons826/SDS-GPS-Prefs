import UserPreferences as UP
import RoomContents as RC
import Prefoperations as PO

class PreferenceTests:
    def weightingTest():
        roomItems = ["projector", "table", "chair", "whiteboard"]
        userPrefs = [UP.Preference("projector", 0.6) , UP.Preference("table", 0.3), UP.Preference("chair", 0.9), UP.Preference("whiteboard", -0.5)]
        room = RC.Room(roomItems)
        
        weighting = PO.PrefOps.calculateWeighting(room, userPrefs)

        assert weighting == 1.3


def main():
    PreferenceTests.weightingTest();


if __name__ == "__main__" : main()