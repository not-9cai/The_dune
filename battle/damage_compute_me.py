class Damage:
    def __init__(self,type,damage,acc,delay):
        self.type = type
        self.damage = damage
        self.acc = acc
        self.evd = 0
        self.ATdelay = delay
        self.changed = 0

    def clone(self):
        tmp = Damage(self.type, self.damage, self.acc, self.ATdelay)
        tmp.evd = self.evd
        tmp.changed = self.changed
        return tmp


def damageHero(damage,hero):
    if(damage.type == 'physics'):
        if(damage.damage > hero.DEF):
            return damage.damage - hero.DEF
        else:
            return 0
    if(damage.type == 'magic'):
        return damage.damage - hero.ADF

    if(damage.type == 'true'):
        return damage.damage
    else: return 0


def HealHero(heal,hero):
    if(hero.HP + heal < hero.MaxHP):
        return heal
    elif(hero.HP < hero.MaxHP):
        return hero.MaxHP - hero.HP
    else:
        return 0

def damageMonster(damage,monster):
    if(damage.type == 'physics'):
        if(damage.damage > monster.DEF):
            return damage.damage - monster.DEF
        else:
            return 0
    if(damage.type == 'magic'):
        return damage.damage - monster.ADF

    if(damage.type == 'true'):
        return damage.damage

    return 0
