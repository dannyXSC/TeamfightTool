import pyautogui
import os
import asyncio
import time


class Mouse:
    def __init__(self):
        pass

    def buyChess(self, index, framework):
        X = framework.chooseTable_X + index * (
            framework.chooseChess_width + framework.gap_width)
        +framework.chooseChess_width/2
        Y = framework.chooseTable_Y+framework.chooseChess_height/2
        pyautogui.moveTo(X, Y, duration=0.5)
        pyautogui.click(clicks=2, button='left', interval=0.05)
