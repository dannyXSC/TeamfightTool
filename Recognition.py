import numpy as np
import json
from PIL import Image, ImageTk


class Recognition:
    def __init__(self, configJSON):
        thetaPath = r"./scr/theta.txt"
        self.num_labels = []
        data = configJSON
        print("loading theta...")
        for key, value in data.items():
            self.num_labels.append(key)
        # print(self.num_labels)
        self.num_labels.append(str(-1))
        with open(thetaPath, 'r') as f:
            self.theta = f.read().split(',')
            size = len(self.theta)
            self.theta = np.array(self.theta)
            self.theta = self.theta.astype(np.float)
            self.theta.shape = (59, int(size / 59))
        print("finish load theta...")

    #img: ndarray
    def get(self, source):
        if type(source) is np.ndarray:
            img = source
            img = np.array(img)
            img = img.flatten() / 256
            img = np.insert(img, 0, 1)
            tRes = np.dot(img, self.theta.T)
            p = np.argmax(tRes, axis=0)
            return self.num_labels[p]
        else:
            # list
            resList = []
            for img in source:
                img = source
                img = np.array(img)
                img = img.flatten() / 256
                img = np.insert(img, 0, 1)
                tRes = np.dot(img, self.theta.T)
                p = np.argmax(tRes, axis=0)
                resList.append(self.num_labels[p])
            return resList

    
