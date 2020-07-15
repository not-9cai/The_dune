from Entity import hero_me
import menu_me as menu
from IO import io_me

omc = hero_me.Hero()
omc.name = 'omc'

myMenu = menu.Menu()
myMenu.standardInitialize()

line = input("Do you want to skip story? 1=Yes,2=No")
if(not line == '1'):
    io_me.printStuff("Space，the final frontier.", 1.8)
    io_me.printStuff("These are the voyages of the starship Enterprise. ", 2.5)
    io_me.printStuff("Its five-year mission, to explore strange new worlds, to seek out new life and civilisations. To brovely go where no man has gone before.", 4)
    io_me.printStuff("以上内容均与本游戏无关", 2)


while(omc.isAlive()):
    myMenu.run(omc)
    myMenu.updateMenu(omc)