#!/usr/bin/python3
import sys
import os
import Preprocessing.TTF.FontManipulator as manipulator
import Preprocessing.TTF.FontPainter as painter
import Preprocessing.Contours.ContourExtractor as Contour
import cv2
import numpy as np

if __name__ == "__main__":
    image = "sample.png"
    img, contours, hierarchy = Contour.extract_all_countours(image)
    coordinates = Contour.find_contour_coordinates(img, contours, hierarchy)
    nearest = Contour.get_nearest_graph(coordinates)
    target_contours = []
    mark = [False] * len(nearest)
    for i in range(0, len(nearest)):
        if mark[i] == True:
            continue
        for j in range(0, len(nearest[i])):
            target_contours.append(coordinates[j][1])
        rect = cv2.minAreaRect(target_contours)
        print("done")

