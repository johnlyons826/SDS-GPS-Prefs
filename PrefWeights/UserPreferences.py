

class Preference:

    def __init__(self, prefName, prefValue):
        self.prefName = prefName
        self.prefValue = prefValue

    def getValue(self):
        return self.prefValue

    def getName(self):
        return self.prefName

class UserPref:

    def __init__(self, prefList):
        self.prefList = prefList

    def getPref(self, prefName):
        for pref in prefName:
            if pref.getName() == prefName:
                return pref.getValue
        return 0
