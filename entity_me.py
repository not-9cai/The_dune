import hero_me
import monster_me
import time
import io_me

class Entity:
    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

    def validTarget(self, otherEntity):
        if isinstance(self, hero_me.Hero):
            return isinstance(otherEntity, monster_me.Monster) and otherEntity.isAlive()
        elif isinstance(self, monster_me.Monster):
            return isinstance(otherEntity, hero_me.Hero) and otherEntity.isAlive()
        else:
            return False

    def creatID(self,num):
        return self.name+str(num)

    def getID(self):
        return self.ID

    def setID(self,ID):
        self.ID = ID

    def take_damage(self, damage):
        return damage

    def getInitiative(self):
        return 0

    def getSPD(self):
        return 999

    def action(self,battleScene):
        for it in battleScene.ATPool.entitypool:
            if self.validTarget(it):
                dmg_took = it.take_damage(self.attack(it))
                io_me.printStuff(it.name + "受到了来自于" + self.name +"的"+ str(dmg_took) + "点伤害——————HP(" + str(it.HP) + "/" + str(it.MaxHP) + ")",0.3)
                #print(it.ID + "受到了来自于" + self.ID +"的"+ str(dmg_took) + "点伤害——————HP(" + str(it.HP) + "/" + str(it.MaxHP) + ")")
                return 0
        return 1