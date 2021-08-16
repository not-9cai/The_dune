from battle import damage_compute_me as DComp
from Entity import entity_me, monster_me
import random
from IO import io_me


class Hero(entity_me.Entity):
    #flags = {}
    #MP = 0

    def __init__(self):
        self.flags = {'Alive': True, 'Class': 'Hero', 'event1': 'not achieved'}
        self.name = 'Steve'
        self.HP = 1000
        self.MaxHP = 1000
        self.MP = 100
        self.ATK = 100
        self.DEF = 100
        self.ATS = 150
        self.ADF = 0
        self.STR = 100
        self.INT = 100
        self.ACC = 25
        self.EVD = 30
        self.LVL = 0
        self.EXP = 0
        self.SPD = 10
        self.eventcount=0


    #flags是一个字典，每个逗号分开是一个条目。冒号前面是key，后面是value。可以通过key查value
    #比如Hero.flags['Alive']会返回True
    #你可以新增、删除或者修改条目，简单百度就可以了。
    #你也可以使用单独的变量来描述Hero的一个状态
    #Hero.MP就是100这个数了

    def print_status(self):
        io_me.printStuff("你看了看自己的身体", 1)
        if(self.flags['Alive'] == True):
            io_me.printStuff("我好像还活着", 0)
        else:
            io_me.printStuff("一阵眩晕感袭来，我好像已经。。死了？", 0)
        io_me.printStuff(self.name, 0)
        io_me.printStuff("HP:" + str(self.HP) + "/" + str(self.MaxHP), 0)
        io_me.printStuff("MP:" + str(self.MP), 0)
        io_me.printStuff("lvl:" + str(self.LVL), 0)
        line = io_me.getStuff("要不要看看详细情报？1=看看，2=算了")
        if line == '1':
            io_me.printStuff("ATK:" + str(self.ATK), 0)
            io_me.printStuff("DEF:" + str(self.DEF), 0)
            io_me.printStuff("SPD:" + str(self.SPD), 0)


    def heal_hero(self,healing):
        if(self.flags['Alive'] == True):
            actual_healing = DComp.HealHero(healing,self)
            self.HP += actual_healing
        return actual_healing

    def take_damage(self, damage):
        if(self.flags['Alive'] == True):
            actual_damage = DComp.damageHero(damage,self)
            self.HP -= actual_damage
        if(self.HP <= 0):
            self.flags['Alive'] = False
        return actual_damage

    def isAlive(self):
        return self.flags['Alive']

    def attack(self,monster):
        io_me.printStuff(self.name+" 的回合！", 0)
        chose = int(io_me.getStuff('physics=1,magic=2'))
        if chose == 1:
            if(isinstance(monster, monster_me.Slime)):
                return DComp.Damage('physics', self.ATK+2,self.ACC+ random.randint(1,100),self.SPD)
            else:
                return DComp.Damage('physics', self.ATK,self.ACC+ random.randint(1,100),self.SPD)
        if chose == 2:
            return DComp.Damage('magic', self.ATS,self.ACC+ random.randint(1,100),self.SPD*2)



    def gainExp(self,monster):
        self.EXP += monster.EXP

    def getInitiative(self):
        return 1

    def getSPD(self):
        return self.SPD

    def rollEVD(self,acc):
        return self.EVD

    def afterEVD(self,dmg):
        flag = io_me.getStuff("是否使用奇策？1=是 2=否")
        actualacc = dmg.acc-self.ACC
        dmg2 = dmg.clone()
        if int(flag) == 1:
            tmp1 = actualacc % 10
            tmp2 = int((actualacc - tmp1)/10)
            dmg2.acc = tmp2+tmp1*10+self.ACC
            dmg2.changed = 1
            return dmg2
        else:
            return dmg2

    def validTarget(self, otherEntity):
        if isinstance(self, Hero):
            return isinstance(otherEntity, monster_me.Monster) and otherEntity.isAlive()
        elif isinstance(self, monster_me.Monster):
            return isinstance(otherEntity, Hero) and otherEntity.isAlive()
        else:
            return False

    def updateHero(self):
        while(self.EXP >= 100):
            self.EXP -= 100
            self.LVL += 1
            self.MaxHP += 10
            self.ATK += 10
            self.DEF +=10
            self.HP = self.MaxHP

            io_me.printStuff(str(self.name) + "升到了" + str(self.LVL) + "级！", 0)

    def clone(self):
        tmp_hero = Hero()
        tmp_hero.name = self.name
        tmp_hero.ATK = self.ATK
        tmp_hero.HP = self.HP
        tmp_hero.MaxHP = self.MaxHP
        tmp_hero.MP = self.MP
        tmp_hero.DEF = self.DEF
        tmp_hero.ATS = self.ATS
        tmp_hero.ADF = self.ADF
        tmp_hero.STR = self.STR
        tmp_hero.INT = self.INT
        tmp_hero.ACC = self.ACC
        tmp_hero.EVD = self.EVD
        tmp_hero.LVL = self.LVL
        tmp_hero.EXP = self.EXP
        tmp_hero.SPD = self.SPD
        tmp_hero.eventcount = self.eventcount
        return tmp_hero