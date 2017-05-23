#!/usr/bin/python3


import numpy as np
import argparse
import imutils
import cv2
import os

def image_to_feature_vector(image):
    img = cv2.imread(image,1)
    return img.flatten()

def get_lable_from_file(filename):
    return os.path.splitext(filename)[0].split("_")[1]



def extract_color_histogram(img, bins=(8, 8, 8)):
    image = cv2.imread(img, 1)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1, 2], None, bins,[0, 180, 0, 256, 0, 256])
    if imutils.is_cv2():
        hist = cv2.normalize(hist)
    else:
        cv2.normalize(hist, hist)
    return hist.flatten()