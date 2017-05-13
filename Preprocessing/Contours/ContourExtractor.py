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
        box= cv2.minAreaRect(c)
        box = cv2.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)
        cX = np.average(box[:, 0])
        cY = np.average(box[:, 1])
        coordinates.append([(cX,cY), c, box])
    return coordinates

def write_contour(img, image, contour):

    x, y, w, h = cv2.boundingRect(contour)
    '''
    pts1 = np.float32([x,y])
    '''
    roi = img[y:y + h, x:x + w]
    cv2.imwrite(image, roi)

    #cv2.cv2.resize()


def get_nearest_graph(coord_cnts, near_dest):
    length = len(coord_cnts)
    nearest = [[]] * length
    for i in range(0, length):
        nearest[i].append(i)
        for k in range(0, length - 1):
            if find_distance_between(coord_cnts[i], coord_cnts[k]) <= near_dest:
                nearest[i].append(k)
    return nearest

def find_distance_between(coord_cnt1, coord_cnt2):
    return dist.euclidean((coord_cnt1[0][0],coord_cnt1[0][1]), (coord_cnt2[0][0], coord_cnt2[0][1]))


def find_average_distance(coord_cnts):
    sum = 0
    for c in coord_cnts:
        for k in coord_cnts:
            sum += find_distance_between(c, k)
    return sum/len(coord_cnts)

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
'''
def write_countours(img, contours, name, dest):
    idx = 0
    for cnt in contours:
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(dest, str(idx) + '_' + name[:-4].replace("_alltogether","") + '.png'), cv2.bitwise_not(roi, roi))
'''
