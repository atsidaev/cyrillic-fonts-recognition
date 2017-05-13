#!/usr/bin/python3

import Preprocessing.Contours.ContourExtractor as Contour
import cv2
from matplotlib import pyplot as plt


if __name__ == "__main__":
    image = Contour.open_image("sample.png")
    original = cv2.imread("sample.png", cv2.CV_8UC1)

    img, contours, hierarchy = Contour.extract_all_countours(image)
    bounding_img = Contour.draw_bounding_boxes(img, contours, hierarchy)
    plt.subplot(121), plt.imshow(original, cmap='gray'), plt.title('original')
    plt.subplot(122), plt.imshow(bounding_img, cmap='gray'), plt.title('bounding')
    plt.show()

    bounding_img2, bounding_contours, hierarchy = Contour.extract_all_countours(bounding_img)
    for i in range(0,len(bounding_contours)):
        Contour.write_sample(original, bounding_contours[i], str(i), (64,64))
