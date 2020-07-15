import entity_me
import hero_me
import monster_me

class BattleScene:
    def __init__(self):
        self.name = 'BattleScene'
        self.ATPool = ATPool()
        self.entityCount = 1

    def addEntity(self, entity):
        self.ATPool.addEntity(entity,entity.creatID(self.entityCount))
        self.entityCount += 1

    def run(self):
        while(not self.ATPool.isEnd()):
            entityInAction = self.ATPool.getEntityInAction()
            self.ATPool.action(entityInAction,self)

class ATPool:
    def __init__(self):
        self.name = 'ATPool'
        self.ATPool_m = {}
        self.entitypool = []

    def addEntity(self, entity,entityID):
        entity.setID(entityID)
        self.ATPool_m[entityID] = entity.getInitiative()
        self.entitypool.append(entity)

    def getEntityInAction(self):
        entitySort = sorted(self.ATPool_m.items(), key=lambda x: x[1], reverse=False)
        return self.getEntityByID(entitySort[0][0])

    def getEntityByID(self, name):
        for entities in self.entitypool:
            if name == entities.getID():
                return entities
        return None

    def action(self,entity,battleScene):
        entity.action(battleScene)
        self.ATPool_m[entity.getID()] += entity.getSPD()

    def isEnd(self):
        heroes = 0
        enemies = 0
        for entities in self.entitypool:
            if isinstance(entities,hero_me.Hero) and entities.isAlive():
                heroes += 1
            if isinstance(entities,monster_me.Monster) and entities.isAlive():
                enemies += 1
        return not ((heroes>0) and (enemies>0))