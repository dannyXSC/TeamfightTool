import io
from PIL import Image
from PyQt5.QtGui import QImage
import numpy as np
from PyQt5.QtCore import QBuffer
from PyQt5.QtWidgets import QApplication
import PyQt5.QtGui as QtGui
import win32gui
import sys

from Frame import Framework


class ChessInformation:
    def __init__(self):
        pass

    def QImage2PILImage(self, img):
        buffer = QBuffer()
        buffer.open(QBuffer.ReadWrite)
        img.save(buffer, "PNG")
        pil_im = Image.open(io.BytesIO(buffer.data()))
        return pil_im

    #获取index位置的图片，并返回pil格式的img
    def getChessImg(self, index, framework):
        startX = framework.chooseTable_X + index * (
            framework.chooseChess_width + framework.gap_width)
        startY = framework.chooseTable_Y
        width = framework.chooseChess_width
        height = framework.chooseChess_height

        hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(hwnd, startX, startY, width, height).toImage()
        return self.QImage2PILImage(img)

    # 获取Index位置的图片，并返回Np.array
    def getChessArray(self, index, framework):
        img = self.getChessImg(index, framework)
        return np.array(img)

    #获得指定位置图片（测试用）
    def getImg(self, x, y, width, height):
        hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
        app = QApplication(sys.argv)
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(hwnd, x, y, width, height).toImage()
        return self.QImage2PILImage(img)
