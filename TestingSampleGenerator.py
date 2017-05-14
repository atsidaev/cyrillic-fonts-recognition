#!/usr/bin/python3

import Preprocessing.Contours.ContourExtractor as Contour
import cv2
from matplotlib import pyplot as plt

def generate_sample_from_image(image_name, sample_location):
    image = Contour.open_image(image_name)
    original = cv2.imread(image_name, cv2.CV_8UC1)
    img, contours, hierarchy = Contour.extract_all_countours(image)
    bounding_img = Contour.draw_bounding_boxes(img, contours, hierarchy)
    bounding_img2, bounding_contours, hierarchy = Contour.extract_all_countours(bounding_img)
    for i in range(0,len(bounding_contours)):
        Contour.write_sample(original, bounding_contours[i], str(i), (64,64))

def generate_samples_from_folder(path):
    return path

if __name__ == "__main__":
    generate_sample_from_image("sample.png")
