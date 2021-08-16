from Entity import monster_me
from Entity import hero_me
import random

class MonsterDictionary:
    def __init__(self):
        self.name = 'defaultDic'
        self.monsterDic = {'slime': monster_me.Slime(), 'evilMage': monster_me.EvilMage(), 'ogre': monster_me.Ogre()}

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


class HeroDictionary:
    def __init__(self):
        self.name = 'defaultHeroDic'
        self.heroDic = {'guy': hero_me.Hero()}

    def addHero(self,monster,name):
        self.heroDic[name] = monster

    def getHero(self,name):
        return self.heroDic[name].clone()

    def getRandomHero(self):
        monList = list(self.heroDic.keys())
        monName = monList[random.randint(0,len(monList)-1)]
        return self.heroDic[monName].clone()

    def clone(self):
        heros = HeroDictionary()
        heros.heroDic = self.heroDic.copy()
        return heros