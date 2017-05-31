#!/usr/bin/python3

import Preprocessing.Other.FileHelper as fh
import Preprocessing.TTF.FontManipulator as fm
import configparser as cp
import Preprocessing.Other.ConfigGenerator as cfgen
import os
import csv
import sys

def normalize_ttf_lable():
    cnf = cp.ConfigParser()
    cnf.read_file(open('config.ini'))
    folder = cnf.get("Directories", "TTFData")
    fm.normalize_ttf_folder(folder)



def label_files(image_data_folder, csvfile, istesting = True):

    files = [f for f in os.listdir(image_data_folder) if os.path.isfile(os.path.join(image_data_folder, f)) and f.endswith(".png")]
    if files == []:
        print("No files found")
        sys.exit()

    reader = cp.ConfigParser()
    reader.read_file(open('config.ini'))

    chunk = 1
    if istesting == True:
        chunk = 0
        labled = reader.get('Datasets', 'IsTestingSetLabled')
        if labled == "True":
            return
        print("Lable testing set...")
    else:
        labled = reader.get('Datasets', 'IsTrainingSetLabled')
        if labled == "True":
            return
        print("Lable training set...")

    for i in range(0, len(files)):
        filename = files[i].split("_")
        file_class = get_class(filename[chunk], csvfile)
        if not file_class == None:
            new_name = os.path.join(image_data_folder, str(i) + "_" + file_class + ".png")
            os.rename(os.path.join(image_data_folder, files[i]), new_name)

    if istesting == True:
        cfgen.change_cfg_value("Datasets", 'IsTestingSetLabled', "True")
    else:
        cfgen.change_cfg_value("Datasets", 'IsTrainingSetLabled', "True")

def generate_classes_csv(raw_data_folder, csv_file):
    with open(csv_file, 'w') as csvfile:
        fieldnames = ['filename', 'class']#,'labels']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        files = [f for f in os.listdir(raw_data_folder) if
        os.path.isfile(os.path.join(raw_data_folder, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
        for i in range(0, len(files)):
            name = os.path.splitext(files[i])[0]
            writer.writerow({'filename': name, 'class': str(i)})

def get_class(name, csv_file):
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if name == row['filename']:
                return row['class']

def get_classes_names():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    file = config.get("Datasets", "classes")
    class_names = []
    with open(file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            class_names.append(row['filename'])
    return class_names

def label_training_set():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    TTFData = config.get('Directories', 'ttfdata')
    csv_file = config.get('Datasets', 'classes')
    image_folder = config.get('Directories', 'learningsamplefolder')

    if not os.path.exists(TTFData) or not os.path.exists(image_folder):
        fh.check_and_generate_folders([TTFData, image_folder])
        sys.exit()
    generate_classes_csv(TTFData, csv_file)
    label_files(image_folder, csv_file, istesting=False)

def lable_testing_set():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    TTFData = config.get('Directories', 'ttfdata')
    csv_file = config.get('Datasets', 'classes')
    image_folder = config.get('Directories', 'testingsamplefolder')

    if not os.path.exists(TTFData) or not os.path.exists(image_folder):
        fh.check_and_generate_folders([TTFData, image_folder])
        sys.exit()
    generate_classes_csv(TTFData, csv_file)
    label_files(image_folder, csv_file, istesting=True)