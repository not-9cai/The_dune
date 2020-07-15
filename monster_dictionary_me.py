import monster_me
import random

class MonsterDictionary:
    def __init__(self):
        self.name = 'defaultDic'
        self.monsterDic = {'slime': monster_me.Slime(), 'evilMage': monster_me.EvilMage(),'ogre':monster_me.Ogre()}

    def addMonster(self,monster,name):
        self.monsterDic[name] = monster

    def getMonster(self,name):
        return self.monsterDic[name].clone()

    def getRandomMonster(self):
        monList = list(self.monsterDic.keys())
        monName = monList[random.randint(0,len(monList)-1)]
        return self.monsterDic[monName].clone()

    def clone(self):
        mons = MonsterDictionary()
        mons.mosterDic = self.monsterDic.copy()
        return mons