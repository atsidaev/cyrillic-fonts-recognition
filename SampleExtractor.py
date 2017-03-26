import cv2
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib import pyplot as plt

def extract_from_grayscale_png(filename):
    img = cv2.imread('sample.png',  cv2.CV_8UC1)
    img = cv2.GaussianBlur(img, (3,3), 0);
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    cv2.bitwise_not(img, img);
    img2, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    idx = 0
    for cnt in contours:
        idx += 1
        x, y, w, h = cv2.boundingRect(cnt)
        roi = img2[y:y + h, x:x + w]
        cv2.imwrite(str(idx) + '.jpg', roi)
    plt.imshow(img2, 'gray')
    plt.show()


extract_from_grayscale_png("sample.png")
