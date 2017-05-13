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
    average = Contour.find_average_distance(coordinates)
    nearest = Contour.get_nearest_graph(coordinates, average)
    idx = 0
    for c in contours:
      #  Contour.write_contour( img, str(idx) + "result.png", c)
        idx+=1


    print("done")

