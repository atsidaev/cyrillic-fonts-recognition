import os
import sys
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2
from Preprocessing.TTF import FontPainter as painter


def extract_all_countours(image):
    img = cv2.imread(image, cv2.CV_8UC1)
    img = cv2.GaussianBlur(img, (3,3), 0);
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.bitwise_not(img, img)#important!
    img2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    return img2, contours, hierarchy

def find_contour_coordinates(image, cnts, hierarchy):
    coordinates = []
    for c in cnts:
        box= cv2.boundingRect(c)
        coordinates.append([c, box])
    return coordinates
'''
def write_contour(img, image, contours):

    #x, y, w, h = cv2.boundingRect(contour)

    pts1 = np.float32([x,y])

    #roi = img[y:y + h, x:x + w]
    cv2.imwrite(image, [contours])

    #cv2.cv2.resize()
'''
def get_nearest_graph(coord_cnts):
    length = len(coord_cnts)
    nearest = [[]] * length
    for i in range(0, length):
        nearest[i].append(coord_cnts[i])
        for k in range(0, length - 1):
            if i != k:
                x, y, w, h = coord_cnts[i][1]
                x1, y1, w1, h1 = coord_cnts[k][1]
                vertical = find_vertical_distance(coord_cnts[i], coord_cnts[k])
                horisontal = find_horisontal_distance(coord_cnts[i], coord_cnts[k])
                if x < x1 and (x + w) < (x1 + w1):
                    cnt_area1 = cv2.contourArea(coord_cnts[i][0])
                    cnt_area2 = cv2.contourArea(coord_cnts[k][0])
                    if (cnt_area1/cnt_area2) < 0.3 or (cnt_area1/cnt_area2) < 0.3:
                        nearest[i].append(k)
    return nearest

def find_vertical_distance(coord_cnt1, coord_cnt2):
    x,y,w,h = coord_cnt1[1]
    x1,y1,w1,h1 = coord_cnt2[1]
    return dist.euclidean( (x,y), (x1+w1, y1+h1) )

def find_horisontal_distance(coord_cnt1, coord_cnt2):
    x,y,w,h = coord_cnt1[1]
    x1,y1,w1,h1 = coord_cnt2[1]
    return dist.euclidean( (x+w,y+h), (x1, y1) )

def find_min_vertical_distance(coord_cnts):
    distances = []
    for c in coord_cnts:
        for k in coord_cnts:
            distances.append(find_vertical_distance(c, k))
    return min(distances)

def find_min_horisontal_distance(coord_cnts):
    distances = []
    for c in coord_cnts:
        for k in coord_cnts:
            distances.append(find_horisontal_distance(c, k))
    return min(distances)




