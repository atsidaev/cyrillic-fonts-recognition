#!/usr/bin/python3
import sys
import os
import Preprocessing.TTF.FontManipulator as manipulator
import Preprocessing.TTF.FontPainter as painter
import Preprocessing.Contours.ContourExtractor as Contour
import cv2

if __name__ == "__main__":
    image = "sample.png"
    img, contours, hierarchy = Contour.extract_all_countours(image)
    coordinates = Contour.find_contour_coordinates(img, contours, hierarchy)
    average = Contour.find_average_distances(coordinates)
    resulting_contours = []
    '''
    for i in list(coordinates):
        for k in coordinates:
            if Contour.find_distance_between(i, k) <= average:
                cn = Contour.merge_contours(i, k, img)
                coordinates.remove(i)
                coordinates.remove(k)
                coordinates.append(cn)
    '''
    print("done")

