import time
import keyboard
from Frame import Framework
from ChessInformation import chessInformation
import json

from Recognition import *

picutre_path = "D:/MyProject/python/testLOL/picture/"

frame = Framework()
imgHandle = chessInformation()
cnt = 0
with open(r'D:\MyProject\python\testLOL\project\scr\information.json',
          'r') as f:
    config = json.load(f)
    rec = Recognition(config)

    def Id2Name(id):
        if id in config:
            return config[id]["HeroName"]
        else:
            return "None"

    while True:
        # print("get " + str(cnt))
        keyboard.wait("f9")
        for i in range(5):
            img = imgHandle.getChessImg(i, frame)
            print(Id2Name(rec.get(img)))

    # time.sleep(20)
# for i in range(5):
#     img = imgHandle.getChessImg(i, frame)
#     img.save('D:\\MyProject\\python\\testLOL\\picture\\' + str(i) + ".png",
#              "png")
# print(frame.dButton_X, frame.dButton_Y, frame.dButton_width,
#       frame.dButton_height)
# img = imgHandle.getImg(int(frame.dButton_X), int(frame.dButton_Y),
#                        int(frame.dButton_width), int(frame.dButton_height))
# img.save(picutre_path + "/dButton.png", "png")
