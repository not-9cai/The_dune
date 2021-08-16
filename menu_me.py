from container import event_pool_me as eventpool, monster_dictionary_me
from Event import event_me as event
from IO import io_me

import sys
import os
import time



class Menu:
    def __init__(self):
        self.name = 'standardmenu'
        self.events = eventpool.Eventpool()
        self.eventcount = 0
        self.monsterDic = monster_dictionary_me.MonsterDictionary()
        self.heroDic = monster_dictionary_me.HeroDictionary()
        self.ranEvent = 0




    def standardInitialize(self):
        self.initializeMonsters()
        self.initializeEvent()



    def initializeMonsters(self):
        monster = 'fucked'
        #do nothing


    def initializeEvent(self):
        self.events.removeAllEvent()
        self.events.config = self.config
        #self.events.addEvent(event.TestEvent())
        #self.events.addEvent(event.TestEvent2())
        #self.events.addEvent(event.BattleEvent())
        #self.events.addEvent(event.BattleMonsterEvent(self.monsterDic.getMonster('slime')))
        #self.events.addEvent(event.BattleFixedMonsterEvent(0, self.monsterDic))
        #self.events.addEvent(event.BattleRandomMonsterEvent(0, self.monsterDic))
        self.events.addEvent(event.BattleMultipleEvent(0,self.monsterDic, self.heroDic))
        #self.events.addEvent(event.PlotEvent("序章"))
        #self.events.addEvent(event.HealEvent())

    def run(self,hero):
        def case1(hero):    # 显示人物状态
            hero.print_status()

        def case2(hero):    # 抽取随机事件
            self.ranEvent = 0
            newEvent = self.events.getAvaliableRandomEvent()
            tempEventCount = newEvent.showPlot(hero)
            self.eventcount += tempEventCount
            hero.eventcount += tempEventCount

        def case3(hero):   #显示当前事件池中可选事件
            self.events.showAvaliableEvent()

        def case4(hero):  # 结束游戏
            io_me.printStuff('你再次沉沉的睡去，就好像，一切从未发生过', 0)
            io_me.printStuff('Game Over', 0)
            sys.exit(0)   #这可能不太对2333333

        def default(hero):  # 默认情况下执行的函数
            io_me.printStuff('你胡乱做了些什么，然而什么都没有发生', 0.3)


        menupannel = {1:case1,2:case2,3:case3,4:case4}

        if(self.ranEvent == 0):
            io_me.printStuff("你从家中醒来，再一次凝望着熟悉的天花板。这一次，似乎会有什么不同。", 1)
            self.ranEvent = 2
        io_me.printStuff("做些什么事情？1=显示人物状态，2=抽随机事件，3=显示当前可选事件,4=退出", 0)
        line = int(io_me.getStuff(''))
        menupannel.get(line, default)(hero)


    def updateMenu(self,hero):
        io_me.printStuff("updating playable level", 0)
        time.sleep(0.3)
        os.system('cls')
        #self.events.removePlayedEvent(hero)
        self.events.updateEventStatus(hero)
        hero.updateHero()
