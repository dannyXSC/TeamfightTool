from project.Frame import Framework
from project.ChessInformation import chessInformation
from ChessInformation import *
from Recongnition import *
from Frame import *
from ReactionBase import *
from Mouse import *


class ReactionSimple(ReactionBase):
    def __init__(self):
        ReactionBase.__init__(self)
        self.recongnition = Recongnition()
        self.infoGetter = ChessInformation()
        self.frame = Framework()
        self.mouse = Mouse()
        self.endFlag = True

    def setConfig(self, config):
        self.neededHero = []
        for key, value in config.items():
            if value["Cost"] == 1:
                self.neededHero.append(key)

    def getInfo(self):
        imgList = list()
        for i in range(5):
            imgList.append(self.infoGetter.getChessImg(i, self.frame))
        return imgList

    def processInfo(self, info):
        return self.recongnition.get(info)

    def opration(self, info):
        if info == None:
            return
        for i in range(5):
            if info[i] in self.neededHero:
                self.mouse.buyChess(i)

    def end(self):
        return self.endFlag
