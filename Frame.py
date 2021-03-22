'''
游戏的框架信息都存在这个类中
'''


class Framework:
    def __init__(self, screenWidth=3840, screenHeight=2160):
        self.screenWidth = screenHeight
        self.screenHeight = screenHeight

        #x轴横着，y轴竖直

        self.chooseTable_X = screenWidth * 0.25  #选择面板左上角的x
        self.chooseTable_Y = screenHeight * 0.85  #选择面板左上角的y

        self.chooseChess_width = screenWidth * 0.1  #牌的宽度
        self.chooseChess_height = screenHeight * 0.15  #牌的高度

        self.gap_width = screenWidth * 0.005

        self.dButton_X = screenWidth * 0.2
        self.dButton_Y = self.chooseTable_Y
        self.dButton_width = screenWidth * 0.1
        self.dButton_height = screenWidth * 0.07

        self.fButton_X = self.dButton_X
        self.fButton_Y = screenHeight * 0.9
        self.fButton_width = self.dButton_width
        self.fButton_height = self.dButton_height
