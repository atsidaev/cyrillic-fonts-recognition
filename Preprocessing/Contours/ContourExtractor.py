import os
import numpy as np
import cv2

def open_image(filename):
    img = cv2.imread(filename, cv2.CV_8UC1)
    img = cv2.GaussianBlur(img, (3, 3), 0);
    img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    return img

def extract_all_countours(img):
    cv2.bitwise_not(img, img)
    img, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)
    return img, contours, hierarchy

def draw_bounding_boxes(img, contours, hierarchy):
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 3)
    return cv2.bitwise_not(img,img)

def get_roi(img,x,y,w,h):
    roi = img[y:y + h, x:x + w]
    return roi

def write_sample(image, contour, prefix, name, sample_size, sample_folder):
    x, y, w, h = cv2.boundingRect(contour)
    roi = get_roi(image, x, y, w, h)
    temp_name = os.path.join(sample_folder, name + "_temp_.png")
    cv2.imwrite(temp_name, roi)
    img = cv2.imread(temp_name, 0)
    height, width = img.shape
    temp_img = cv2.imread(temp_name, 0)
    pts1 = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
    pts2 = np.float32([[0, 0], [sample_size[0], 0], [0, sample_size[1]], [sample_size[0], sample_size[1]]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(temp_img, M, (sample_size[0], sample_size[1]))
    filename = os.path.join(sample_folder,prefix + "_" + name + "_sample.png")
    cv2.imwrite(filename, dst)
    os.remove(temp_name)
