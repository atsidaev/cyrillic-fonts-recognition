import os
import sys

import cv2

from Preprocessing.TTF import FontPainter as painter

def extract_all_countours(image):
    img = cv2.imread(image, cv2.CV_8UC1)
    img = cv2.GaussianBlur(img, (3,3), 0);
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.bitwise_not(img, img);
    img2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    return img2, contours, hierarchy

def write_countours(img, contours, name, dest):
    idx = 0
    for cnt in contours:
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img[y:y + h, x:x + w]
        cv2.imwrite(os.path.join(dest, str(idx) + '_' + name[:-4].replace("_alltogether","") + '.png'), cv2.bitwise_not(roi, roi))
