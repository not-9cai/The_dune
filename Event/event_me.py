from IO import io_me
from battle import battle_scene
from Event import plot_me

class Event:
    def __init__(self):
        self.name = 'dummy'
        self.IsFinished = 0

    def showPlot(self,hero):
        #hero.print_status()
        io_me.printStuff('dummy plot', 0)
        self.IsFinished = 1
        return 1


    def updateEvent(self,hero):
        return 0
        #do nothing




class TestEvent(Event):
    def __init__(self):
        self.name = 'event1'
        self.IsFinished = 0

    def showPlot(self, hero):
        io_me.printStuff("event1", 0)
        if (hero.flags['event1'] == 'not achieved'):
            io_me.printStuff("event1 not complete", 0.5)
            io_me.printStuff("input 1 to complete event1, else do nothing", 0)
            line = input()
            if (line == '1'):
                hero.flags['event1'] = 'achieved'
                io_me.printStuff('event1 achieved', 0)
                self.IsFinished = -1
        else:
            io_me.printStuff("事件已完成", 0)

        return 1


class TestEvent2(Event):
    def __init__(self):
        self.name = 'event2'
        self.IsFinished = -1

    def showPlot(self, hero):
        io_me.printStuff("event2（只有完成event1后才会刷新）", 0)

        return 1

    def updateEvent(self,hero):
        if (hero.flags['event1'] != 'not achieved'):
            self.IsFinished = 0
        return 0


class BattleEvent(Event):
    def __init__(self):
        self.name = 'battle'
        self.IsFinished = 0

    def showPlot(self, hero):
        io_me.printStuff("input damage delt to hero", 0)
        damage = int(io_me.getStuff(''))
        dmg_took = hero.take_damage(damage)
        io_me.printStuff(hero.name + "受到了" + str(dmg_took) + "点伤害", 0)
        if (hero.HP <= 0):
            hero.flags['Alive'] = False
            io_me.printStuff(hero.name + "倒下了", 0)
        self.IsFinished = 1

        return 1


class HealEvent(Event):
    def __init__(self):
        self.name = 'healing'
        self.IsFinished = 0

    def showPlot(self, hero):
        heal = 10
        heal_took = hero.heal_hero(heal)
        io_me.printStuff(hero.name + "的生命值恢复了" + str(heal_took), 0)
        self.IsFinished = 1

        return 1


class BattleMonsterEvent(Event):
    def __init__(self,monster):
        self.name = 'battle'
        self.IsFinished = 0
        self.monster = monster
        self.monsterBackup = monster.clone()

    def showPlot(self, hero):
        print("Battle"+str(self.monster.name))
        while(hero.isAlive() and self.monster.isAlive()):
            dmg_took = hero.take_damage(self.monster.attack(hero))
            io_me.printStuff(hero.name + "受到了" + str(dmg_took) + "点伤害——————HP(" + str(hero.HP) + "/" + str(hero.MaxHP) + ")", 0.3)
            dmg_delt = self.monster.take_damage(hero.attack(self.monster))
            io_me.printStuff(self.monster.name + "受到了" + str(dmg_delt) + "点伤害——————HP(" + str(self.monster.HP) + "/" + str(self.monster.MaxHP) + ")", 0.3)
        if (hero.HP <= 0):
            hero.flags['Alive'] = False
            io_me.printStuff(hero.name + "倒下了", 0)
        else:
            hero.gainExp(self.monster)
            io_me.printStuff(hero.name + "获胜", 0)
        self.IsFinished = 1

        return 1

    def updateEvent(self, hero):
        self.monster = self.monsterBackup.clone()
        return 0



class BattleBossEvent(Event):
    def __init__(self,Boss):
        self.name = 'Boss'
        self.IsFinished = 0
        self.Boss = Boss
        self.monsterBackup = Boss.clone()




class BattleFixedMonsterEvent(Event):
    def __init__(self,num,monsterDic):
        self.name = 'battle_fixed'
        self.IsFinished = 0
        self.monsters = []
        self.monsterBackup = []
        self.myMonsterDic = monsterDic
        if num == 0:
            self.monsters.append(monsterDic.getRandomMonster())
            self.monsterBackup.append(self.monsters[0].clone())
            self.monsters.append(monsterDic.getRandomMonster())
            self.monsterBackup.append(self.monsters[1].clone())


    def showPlot(self, hero):
        #print("Battle"+str(self.monster.name))
        self.battleScene = battle_scene.BattleScene()
        self.battleScene.addEntity(hero)
        for mon in self.monsters:
            self.battleScene.addEntity(mon)
        self.battleScene.run()
        if (hero.HP <= 0):
            hero.flags['Alive'] = False
            io_me.printStuff(hero.name + "倒下了", 0)
        else:
            for mon in self.monsters:
                hero.gainExp(mon)
            io_me.printStuff(hero.name + "获胜", 0)
        self.IsFinished = 1

        return 1

    def updateEvent(self, hero):
        for i in range (len(self.monsterBackup)):
            self.monsters[i] = self.monsterBackup[i].clone()
        return 0



class BattleRandomMonsterEvent(Event):
    def __init__(self,num,monsterDic):
        self.name = 'battle_random'
        self.IsFinished = 0
        self.monsters = []
        self.myMonsterDic = monsterDic
        if num == 0:
            self.monsters.append(monsterDic.getRandomMonster())
            #self.monsters.append(monsterDic.getRandomMonster())


    def showPlot(self, hero):
        #print("Battle"+str(self.monster.name))
        self.battleScene = battle_scene.BattleScene()
        self.battleScene.addEntity(hero)
        for mon in self.monsters:
            self.battleScene.addEntity(mon)
        self.battleScene.run()
        if (hero.HP <= 0):
            hero.flags['Alive'] = False
            io_me.printStuff(hero.name + "倒下了", 0)
        else:
            for mon in self.monsters:
                hero.gainExp(mon)
            io_me.printStuff(hero.name + "获胜", 0)
        self.IsFinished = 1

        return 1

    def updateEvent(self, hero):
        for i in range (len(self.monsters)):
            self.monsters[i] = self.myMonsterDic.getRandomMonster()
        return 0



class PlotEvent(Event):
    def __init__(self,filename):
        self.name = "PlotEvent" + filename
        self.filename = "Event/plots/"+ filename + ".txt"
        self.IsFinished = 0

    def showPlot(self, hero):
        self.myplot = plot_me.Plots(self.config.textspeed)
        self.myplot.readFile(self.filename)
        self.IsFinished = 1

        return 1


class BattleMultipleEvent(Event):
    def __init__(self,num,monsterDic,heroDic):
        self.name = 'battle_multple'
        self.IsFinished = 0
        self.monsters = []
        self.myMonsterDic = monsterDic
        self.heroes = []
        self.myHeroDic = heroDic
        if num == 0:
            self.monsters.append(monsterDic.getRandomMonster())
            self.monsters.append(monsterDic.getRandomMonster())
            self.monsters.append(monsterDic.getRandomMonster())
            self.heroes.append(heroDic.getRandomHero())

    def showPlot(self, hero):
        # print("Battle"+str(self.monster.name))
        self.battleScene = battle_scene.BattleScene()
        for mon in self.monsters:
            self.battleScene.addEntity(mon)
        for otherhero in self.heroes:
            otherhero.SPD = 40
            self.battleScene.addEntity(otherhero)
        self.battleScene.addEntity(hero)
        self.battleScene.run()
        if (hero.HP <= 0):
            hero.flags['Alive'] = False
            io_me.printStuff(hero.name + "倒下了", 0)
        else:
            for mon in self.monsters:
                hero.gainExp(mon)
            io_me.printStuff(hero.name + "获胜", 0)
        self.IsFinished = 1
        return 1

    def updateEvent(self, hero):
        for i in range(len(self.monsters)):
            self.monsters[i] = self.myMonsterDic.getRandomMonster()
        for j in range(len(self.heroes)):
            self.heroes[i] = self.myHeroDic.getRandomHero()
        return 0


