import damage_compute_me as DComp
import entity_me

class Monster(entity_me.Entity):
    def __init__(self):
        self.name = 'Monster'
        self.HP = 100
        self.MaxHP = 100
        self.MP = 100
        self.ATK = 30
        self.DEF = 30
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
        return DComp.Damage('physics',self.ATK)

    def clone(self):
        return Monster()

    def getSPD(self):
        return self.SPD


class Slime(Monster):
    def __init__(self):
        self.name = 'Slime'
        self.HP = 100
        self.MaxHP = 100
        self.MP = 100
        self.ATK = 130
        self.DEF = 30
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
        self.ATK = 10
        self.DEF = 30
        self.EXP = 100
        self.SPD = 10

    def attack(self,hero):
        return DComp.Damage('magic', self.ATK)

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
        self.EXP = 200
        self.SPD = 20

    def attack(self,hero):
        return DComp.Damage('physics', self.ATK)

    def clone(self):
        return Ogre()