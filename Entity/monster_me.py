from battle import damage_compute_me as DComp
from Entity import entity_me,hero_me
import random

class Monster(entity_me.Entity):
    def __init__(self):
        self.name = 'Monster'
        self.HP = 100
        self.MaxHP = 100
        self.MP = 100
        self.ATK = 30
        self.DEF = 30
        self.ATS = 0
        self.ADF = 0
        self.ACC = 0
        self.EVD = 10
        self.EXP = 100
        self.SPD = 10

    def isAlive(self):
        return self.HP >= 0

    def take_damage(self, damage):
        actual_damage = DComp.damageMonster(damage,self)
        self.HP -= actual_damage
        return actual_damage

    def print_status(self):
        print(self.name)
        print("HP:"+str(self.HP))
        print("MP:"+str(self.MP))

    def attack(self,hero):
        return DComp.Damage('physics',self.ATK,self.ACC+ random.randint(1,100),self.SPD)

    def clone(self):
        return Monster()

    def rollEVD(self,acc):
        return self.EVD

    def getSPD(self):
        return self.SPD

    def validTarget(self, otherEntity):
        if isinstance(self, hero_me.Hero):
            return isinstance(otherEntity, Monster) and otherEntity.isAlive()
        elif isinstance(self, Monster):
            return isinstance(otherEntity, hero_me.Hero) and otherEntity.isAlive()
        else:
            return False


class Slime(Monster):
    def __init__(self):
        self.name = 'Slime'
        self.HP = 100
        self.MaxHP = 100
        self.MP = 100
        self.ATK = 130
        self.DEF = 30
        self.ATS = 0
        self.ADF = 0
        self.ACC = 0
        self.EVD = 20
        self.EXP = 100
        self.SPD = 10


    def clone(self):
        return Slime()

class EvilMage(Monster):
    def __init__(self):
        self.name = 'EvilMage'
        self.HP = 100
        self.MaxHP = 100
        self.MP = 100
        self.ATK = 0
        self.ATS = 10
        self.ADF = 50
        self.DEF = 30
        self.ACC = 0
        self.EVD = 20
        self.EXP = 100
        self.SPD = 10

    def attack(self,hero):
        return DComp.Damage('magic', self.ATS,self.ACC+ random.randint(1,100),self.SPD)

    def clone(self):
        return EvilMage()



class Ogre(Monster):
    def __init__(self):
        self.name = 'Ogre'
        self.HP = 300
        self.MaxHP = 300
        self.MP = 100
        self.ATK = 200
        self.DEF = 30
        self.ATS = 150
        self.ADF = 0
        self.ACC = 0
        self.EVD = 20
        self.EXP = 200
        self.SPD = 20

    def clone(self):
        return Ogre()