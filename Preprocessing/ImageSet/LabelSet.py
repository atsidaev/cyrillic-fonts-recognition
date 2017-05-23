#!/usr/bin/python3

import Preprocessing.Other.FileHelper as fh
import configparser as cp
import os
import csv


def label_files(image_data_folder, csvfile):
    files = [f for f in os.listdir(image_data_folder) if os.path.isfile(os.path.join(image_data_folder, f)) and f.endswith(".png")]
    for i in range(0, len(files)):
        filename = files[i].split("_")
        file_class = get_class(filename[1], csvfile)
        new_name = os.path.join(image_data_folder, str(i) + "_" + file_class + ".png")
        os.rename(os.path.join(image_data_folder, files[i]), new_name)

def label_files1(image_data_folder, csvfile):
    files = [f for f in os.listdir(image_data_folder) if os.path.isfile(os.path.join(image_data_folder, f)) and f.endswith(".png")]
    for i in range(0, len(files)):
        filename = files[i].split("_")
        file_class = get_class(filename[0], csvfile)
        new_name = os.path.join(image_data_folder, str(i) + "_" + file_class + ".png")
        os.rename(os.path.join(image_data_folder, files[i]), new_name)

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


def label_training_set():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    TTFData = config.get('Directories', 'ttfdata')
    csv_file = config.get('Datasets', 'classes')
    image_folder = config.get('Directories', 'learningsamplefolder')

    if not os.path.exists(TTFData) or not os.path.exists(image_folder):
        fh.check_and_generate_folders([TTFData, image_folder])
    generate_classes_csv(TTFData, csv_file)
    label_files(image_folder, csv_file)

def lable_testing_set():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    TTFData = config.get('Directories', 'ttfdata')
    csv_file = config.get('Datasets', 'classes')
    image_folder = config.get('Directories', 'testingsamplefolder')

    if not os.path.exists(TTFData) or not os.path.exists(image_folder):
        fh.check_and_generate_folders([TTFData, image_folder])
    generate_classes_csv(TTFData, csv_file)
    label_files1(image_folder, csv_file)