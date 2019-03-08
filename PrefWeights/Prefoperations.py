import RoomContents as rooms
import UserPreferences as usrprf


class PrefOps:
    def calculateWeighting(room, userPrefs):
        totalWeighting = 0
        for pref in userPrefs:
            if room.checkItem(pref.getName()):
                totalWeighting = round(totalWeighting + pref.getValue() * 1, 2)
            else:
                totalWeighting = round(totalWeighting + pref.getValue() * -1, 2)
            
        return totalWeighting




