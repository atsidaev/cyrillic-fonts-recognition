#!/usr/bin/python3
import configparser as cp
import os
import sys
import Preprocessing.Other.FileHelper as fh
import Preprocessing.TTF.FontManipulator as fontmanip
import Preprocessing.TTF.FontPainter as painter
from Preprocessing.ImageSet import TestingImageSetGenerator as tsg


def generate_learning_images():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    learningSampleFolder = config.get('Directories', 'learningsamplefolder')
    ttfData = config.get('Directories', 'ttfdata')
    is_labled = config.get("Datasets","istrainingsetlabled")
    if is_labled == "True":
        return
    if not os.path.exists(learningSampleFolder) or not os.path.exists(ttfData):
        fh.check_and_generate_folders([learningSampleFolder, ttfData])
    else:
        print("Learning images generation...")
        files = [f for f in os.listdir(ttfData) if os.path.isfile(os.path.join(ttfData, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
        s = ""
        text = s.join((painter.get_lower_cyrillic(), painter.get_upper_cyrillic(), painter.get_digits()))
        for f in files:
            #fontmanip.normalize_ttf_filename(os.path.join(ttfData, f))
            for i in text:
                painter.draw_sign(os.path.join(ttfData, f), i, 40, [64, 64], learningSampleFolder)
        images = [k for k in os.listdir(learningSampleFolder) if os.path.isfile(os.path.join(learningSampleFolder, k)) and k.endswith(".png")]
        for i in list(images):
            tsg.generate_sample_from_image(os.path.join(learningSampleFolder,i),str(i).replace(".png",""),learningSampleFolder)
            os.remove(os.path.join(learningSampleFolder, i))

if __name__ == "__main__":
    generate_learning_images()