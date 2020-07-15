import random

class Eventpool():
    def __init__(self):
        self.eventpool = []

    def addEvent(self,Event):
        self.eventpool.append(Event)

    def removeEvent(self,Event):
        self.eventpool.remove(Event)

    def getEvent(self,num):
        return self.eventpool[num]

    def getRandomEvent(self):
        num = random.randint(0,len(self.eventpool)-1)
        return self.getEvent(num)

    def getAvaliableRandomEvent(self):
        temp=[]
        for it in self.eventpool:
            if(it.IsFinished >= 0):
                temp.append(it)
        if(len(temp) == 0):
            return None
        else:
            num = random.randint(0, len(temp)-1)
            return temp[num]


    def getEventByname(self,name):
        for it in self.eventpool:
            if(it.name == name):
                return it
        return None

    def getRandomEventByname(self,name):
        temp=[]
        for it in self.eventpool:
            if(it.name == name):
                temp.append(it)
        if(len(temp) == 0):
            return None
        else:
            num = random.randint(0, len(temp)-1)
            return temp[num]


    def removeAllEvent(self):
        self.eventpool.clear()


    def showAllEvent(self):
        for it in self.eventpool:
            print(it.name)

    def showAvaliableEvent(self):
        for it in self.eventpool:
            if (it.IsFinished>=0):
                print(it.name)

    def removePlayedEvent(self,hero):
        for it in self.eventpool:
            if(it.IsFinished == 1):
                self.eventpool.remove(it)


    def updateEventStatus(self,hero):
        for it in self.eventpool:
            it.updateEvent(hero)