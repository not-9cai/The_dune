import damage_compute_me as DComp
import monster_me
import entity_me
import io_me

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
        self.STR = 100
        self.INT = 100
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
        io_me.printStuff("你看了看自己的身体",1)
        if(self.flags['Alive'] == True):
            io_me.printStuff("我好像还活着",0)
        else:
            io_me.printStuff("一阵眩晕感袭来，我好像已经。。死了？",0)
        io_me.printStuff(self.name,0)
        io_me.printStuff("HP:"+str(self.HP) + "/"+str(self.MaxHP),0)
        io_me.printStuff("MP:"+str(self.MP),0)
        io_me.printStuff("lvl:"+str(self.LVL),0)
        line = io_me.getStuff("要不要看看详细情报？1=看看，2=算了")
        if line == '1':
            io_me.printStuff("ATK:" + str(self.ATK),0)
            io_me.printStuff("DEF:" + str(self.DEF),0)
            io_me.printStuff("SPD:" + str(self.SPD),0)


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
        if(isinstance(monster,monster_me.Slime)):
            return DComp.Damage('physics', self.ATK+2)
        else:
            return DComp.Damage('physics', self.ATK)

    def gainExp(self,monster):
        self.EXP += monster.EXP

    def getInitiative(self):
        return 1

    def getSPD(self):
        return self.SPD

    def updateHero(self):
        while(self.EXP >= 100):
            self.EXP -= 100
            self.LVL += 1
            self.MaxHP += 10
            self.ATK += 10
            self.DEF +=10
            self.HP = self.MaxHP

            io_me.printStuff(str(self.name) + "升到了" + str(self.LVL) + "级！",0)