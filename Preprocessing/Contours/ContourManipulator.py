#!/usr/bin/python3
import cv2
import os
from matplotlib import pyplot as plt

def draw_contour(img, contour, name):
    x, y, w, h = cv2.boundingRect(contour)
    roi = get_roi(img, x, y, w, h)
    cv2.imwrite(name, roi)

def get_roi(img,x,y,w,h):
    roi = img[y:y + h, x:x + w]
    return roi

def get_name(path):
    base = os.path.basename(path)
    nostring = os.path.splitext(base)[0].replace("_stringseg_","")
    noword = os.path.splitext(nostring)[0].replace("_wordseg_","")
    nochar = os.path.splitext(noword)[0].replace("_char_","")
    return nochar

def draw_vertical_borders(borders, height, img):
    for b in borders:
        cv2.line(img, ( b[0], 0), (b[0], height-1), (0,255,0))
    show_image_pyplot(img)

def show_image_pyplot(img):
    plt.imshow(img, cmap='gray')
    plt.show()

def get_character_segments(img, borders):
    height, widht, channels = img.shape
    segments = []
    for i in range(0, len(borders)):
        if i == (len(borders) - 1):
            break
        else:
            segment_length = abs(borders[i+1][0] - borders[i][0])
            roi = get_roi(img, borders[i][0], 0,segment_length ,height)
            segments.append(roi)
    return segments

def draw_segment(roi, name):
    cv2.imwrite(name, roi)