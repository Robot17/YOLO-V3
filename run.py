# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 12:30:21 2018

@author: wmy
"""

import sys
import argparse
from PIL import Image
import glob
import os
from predict import YOLO, detect_video, predict_testset, predict_valset, predict_trainset

def run(yolo, path, outdir):     
    for jpgfile in glob.glob(path):
        print(jpgfile)
        img = Image.open(jpgfile)
        img_name=os.path.basename(jpgfile)
        img = yolo.detect_image(img,img_name)
        # img.show()
        # img.save(os.path.join(outdir, os.path.basename(jpgfile)))
        pass
    pass

if __name__ == '__main__':
    yolo = YOLO()
    for i in range(8001, 10000):
        path = 'dataset/cartoon_test/00' + str(i) + '.jpg'
        run(yolo, path, 'output/')
    run(yolo, 'dataset/cartoon_test/010000.jpg', 'output/')