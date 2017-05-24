#!/usr/bin/python3

import Preprocessing.Contours.ContourExtractor as Contour
import Preprocessing.TTF.FontPainter as painter
import Preprocessing.TTF.FontManipulator as fontmanip
import Preprocessing.Other.FileHelper as fh
import configparser as cp
import io
import cv2
import sys
import os
from os import listdir
from os.path import isfile, join



def generate_synthetic_raw_images(font_folder, sample_folder):
    files = [f for f in os.listdir(font_folder) if
             os.path.isfile(os.path.join(font_folder, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
    for f in files:
        fontname = os.path.join(font_folder, f)
        fontmanip.normalize_ttf_filename(fontname)
    files = [f for f in os.listdir(font_folder) if
             os.path.isfile(os.path.join(font_folder, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
    for f in files:
        fontname = os.path.join(font_folder, f)
        painter.draw_all_font_symbols(fontname, 40, (2048, 800), sample_folder)

def generate_sample_from_image(image_name, name_prefix, sample_folder):
    image = Contour.open_image(image_name)
    original = cv2.imread(image_name, 1)
    img, contours, hierarchy = Contour.extract_all_countours(image)
    bounding_img = Contour.draw_bounding_boxes(img, contours, hierarchy)
    bounding_img2, bounding_contours, hierarchy = Contour.extract_all_countours(bounding_img)
    for i in range(0,len(bounding_contours)):
        sample_name = str(i)
        Contour.write_sample_image(original, bounding_contours[i], name_prefix, sample_name, (32, 32), sample_folder)

def generate_testing_samples():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    testingSampleFolder = config.get('Directories', 'testingsamplefolder')
    rawImageFolder = config.get('Directories', 'rawimagefolder')
    ttfData = config.get('Directories', 'ttfdata')

    if not os.path.exists(testingSampleFolder) or not os.path.exists(rawImageFolder) or not os.path.exists(ttfData):
        fh.check_and_generate_folders([testingSampleFolder, rawImageFolder, ttfData])
    else:
        print("Testing images generation...")
        files = [f for f in listdir(rawImageFolder) if isfile(join(rawImageFolder, f)) and os.path.splitext(f)[1] == ".png"]
        if len(files) == 0:
            generate_synthetic_raw_images(ttfData, rawImageFolder)
            files = [f for f in listdir(rawImageFolder) if
                     isfile(join(rawImageFolder, f)) and os.path.splitext(f)[1] == ".png"]
        for f in files:
            prefix = f.replace(".png", "")
            generate_sample_from_image(os.path.join(rawImageFolder, f),prefix, testingSampleFolder)

if __name__ == "__main__":
    generate_testing_samples()