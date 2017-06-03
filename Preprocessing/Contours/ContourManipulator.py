#!/usr/bin/python3
import cv2
import os
from matplotlib import pyplot as plt

def get_roi(img,x,y,w,h):
    roi = img[y:y + h, x:x + w]
    return roi

def get_name(path):
    base = os.path.basename(path)
    return os.path.splitext(base)[0].replace("_stringseg_","")

def draw_vertical_borders(borders, height, img):
    for b in borders:
        cv2.line(img, ( b[0], 0), (b[0], height-1), (0,255,0))
    show_image_pyplot(img)

def show_image_pyplot(img):
    plt.imshow(img, cmap='gray')
    plt.show()