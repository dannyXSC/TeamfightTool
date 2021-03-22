import time
import json

from Reaction import *


class TeamfightTool:
    def __init__(self, rec):
        self.rec = rec
        self.configPath = "./scr/information.json"
        try:
            with open(self.configPath) as f:
                self.config = json.load(f)
        except:
            pass
        finally:
            pass

    def start(self, sleepTime=1):
        # set
        self.rec.setConfig(self.config)
        while True:
            if self.rec.end() == True:
                break
            # get info
            info = self.rec.getInfo()
            # process info
            info = self.rec.processInfo(info)
            # opration
            self.rec.opration(info)
            # sleep
            time.sleep(sleepTime)
