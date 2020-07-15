class Damage:
    def __init__(self,type,damage):
        self.type = type
        self.damage = damage


def damageHero(damage,hero):
    if(damage.type == 'physics'):
        if(damage.damage > hero.DEF):
            return damage.damage - hero.DEF
        else:
            return 0
    if(damage.type == 'magic'):
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
    if(damage.type == 'magjc'):
        return damage.damage
