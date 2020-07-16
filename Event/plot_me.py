from IO import io_me

class Plots:
    def __init__(self,textspeed):
        self.name = 'dummyplot'
        self.plots = []
        self.skip = False
        self.textspeed = textspeed

    def show(self,skip):
        if not skip:
            for plot in self.plots:
                io_me.printStuff(plot,(10+len(plot))/self.textspeed)

    def tryShow(self):
        if self.skip == False:
            self.skip = io_me.getStuff("输入1跳过剧情") == '1'
            self.show(self.skip)




    def iniTestPlot(self):
        self.plots.clear()
        self.plots.append("这是一些测试信息")
        self.plots.append("主要用来测试文字显示速度是不是合适")
        self.plots.append("所以")
        self.plots.append("字多字少都会有一些")
        self.plots.append("总之，这是一些测试信息，这里都是正确的废话")


    def readFile(self,filename):
        fo = open(filename, "r", encoding='UTF-8')
        self.plots = fo.readlines()
        for i in range (len(self.plots)):
            self.plots[i] = self.plots[i].strip()
        self.show(self.skip)
        fo.close()