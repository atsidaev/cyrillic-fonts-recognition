#!/usr/bin/python3
import sklearn.preprocessing as skpreprocessing
import matplotlib.pyplot as plt
import configparser as cp
import numpy as np
import pickle
import imutils
import cv2
import os

def normalize_set(set):
    return skpreprocessing.normalize(set, norm='l2')


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

def read_dataset(dataset):
    files = [os.path.join(dataset,f) for f in os.listdir(dataset)]
    pixels = []
    lables = []
    for f in files:
        pixels.append(image_to_feature_vector(f))
        lables.append(get_lable_from_file(f))
    pixels = np.array(pixels)
    lables = np.array(lables)
    return pixels,lables

def save_model(model, name):
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", name)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    pickle.dump(model, open(filename, 'wb'))
    print(name, "saved.")
