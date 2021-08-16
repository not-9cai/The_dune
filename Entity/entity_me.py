from IO import io_me
import random


class Entity:
    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

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

    def rollEVD(self,acc):
        return 1

    def getSPD(self):
        return 999

    def afterEVD(self,dmg):
        return dmg

    def action(self,battleScene):
        for it in battleScene.ATPool.entitypool:
            if self.validTarget(it):
                dmg_tmp = self.attack(it)
                valid_hit = it.rollEVD(dmg_tmp.acc)
                dmg_tmp.evd = valid_hit
                io_me.printStuff(self.name+" acc="+str(dmg_tmp.acc)+" ("+str(self.ACC)+"+("+str(dmg_tmp.acc-self.ACC)+"))"+", "+it.name+" evd="+str(valid_hit) , 0.1)
                dmg_tmp2 = self.afterEVD(dmg_tmp)
                if int(dmg_tmp2.changed) == 1:
                    io_me.printStuff(self.name + " acc=" + str(dmg_tmp2.acc) + " (" + str(self.ACC) + "+(" + str(dmg_tmp2.acc - self.ACC) + "))" + ", " + it.name + " evd=" + str(dmg_tmp2.evd), 0.1)
                if dmg_tmp2.acc > dmg_tmp2.evd:
                    dmg_took = it.take_damage(dmg_tmp2)
                    io_me.printStuff(it.name + " 受到了来自于 " + self.name + " 的" + str(dmg_took) + "点伤害——————HP(" + str(it.HP) + "/" + str(it.MaxHP) + ")", 0.3)
                    #print(it.ID + "受到了来自于" + self.ID +"的"+ str(dmg_took) + "点伤害——————HP(" + str(it.HP) + "/" + str(it.MaxHP) + ")")
                else:
                    io_me.printStuff(it.name + " 受到了来自于" + self.name + " 的攻击，但躲开了！",0.3)
                return dmg_tmp.ATdelay
        return 1