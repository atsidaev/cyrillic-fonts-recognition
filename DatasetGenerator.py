#!/usr/bin/python3

from sklearn.neighbors import KNeighborsClassifier
import sklearn
from imutils import paths
import numpy as np
import configparser as cp
import imutils
import cv2
import os
import csv

def generate_labeled_dataset():
    return 0

def generate_classes_csv(raw_data_folder, csvfile):
    with open(csv_file, 'w') as csvfile:
        fieldnames = ['filename', 'class']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        files = [f for f in os.listdir(raw_data_folder) if
        os.path.isfile(os.path.join(raw_data_folder, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
        for i in range(0, len(files)):
            name = os.path.splitext(files[i])[0]
            writer.writerow({'filename': name, 'class': str(i)})

def generate_labled_csv(image_data_folder, csvfile):
    return 0
'''
def lable_files(image_data_folder, csvfile):
    files = [f for f in os.listdir(image_data_folder) if os.path.isfile(os.path.join(image_data_folder, f)) and f.endswith(".png")]
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
'''
def image_to_feature_vector(image):
    return image.flatten()

def get_lable(image):
    return None

def write_metric_to_file(metric, filename):
    return 0

if __name__ == "__main__":
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    TTFData = config.get('Directories', 'ttfdata')
    csv_file = config.get('Datasets', 'classes')
    dataset_folder = config.get('Directories', 'datasetfolder')
    if not os.path.exists(TTFData) or not os.path.exists(dataset_folder):
        if not os.path.exists(TTFData):
            os.makedirs(TTFData)
        if not os.path.exists(dataset_folder):
            os.makedirs(dataset_folder)
    generate_classes_csv(TTFData, csv_file)
