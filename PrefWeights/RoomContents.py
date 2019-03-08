

class Room:

    def __init__(self, itemList):
        self.itemList = itemList

    def checkItem(self, itemname):
        if itemname in self.itemList:
            return True
        else:
            return False

    def addItem(self, itemname):
        self.itemList.append(itemname)

    def removeItem(self,itemname):
        if itemname in self.itemList:
            self.itemList.remove(itemname)
            return True
        else:
            return False