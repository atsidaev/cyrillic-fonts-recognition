#!/usr/bin/python3

import configparser as cp
import os
import csv


def lable_files(image_data_folder, csvfile):
    files = [f for f in os.listdir(image_data_folder) if os.path.isfile(os.path.join(image_data_folder, f)) and f.endswith(".png")]
    for i in range(0, len(files)):
        filename = files[i].split("_")
        file_class = get_class(filename[1], csvfile)
        new_name = os.path.join(image_data_folder, str(i) + "_" + file_class + ".png")
        os.rename(os.path.join(image_data_folder, files[i]), new_name)
        print(files[i], " ", os.path.basename(new_name), " ",file_class, "\n")


def get_class(name, csvfile):
    with open(csvfile, 'r') as csv:
        reader = csv.DictReader(csv)
        for row in reader:
            if name == row['filename']:
                return row['class']

def generate_classes_csv(raw_data_folder, csvfile):
    with open(csv_file, 'w') as csvfile:
        fieldnames = ['filename', 'class']#,'labels']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        files = [f for f in os.listdir(raw_data_folder) if
        os.path.isfile(os.path.join(raw_data_folder, f)) and (f.endswith(".otf") or f.endswith(".ttf"))]
        for i in range(0, len(files)):
            name = os.path.splitext(files[i])[0]
            writer.writerow({'filename': name, 'class': str(i)})


if __name__ == "__main__":
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    TTFData = config.get('Directories', 'ttfdata')
    csv_file = config.get('Datasets', 'classes')
    image_folder = config.get('Directories', 'learningsamplefolder')
    dataset_folder = config.get('Directories', 'datasetfolder')

    if not os.path.exists(TTFData) or not os.path.exists(dataset_folder):
        if not os.path.exists(TTFData):
            os.makedirs(TTFData)
        if not os.path.exists(dataset_folder):
            os.makedirs(dataset_folder)
    generate_classes_csv(TTFData, csv_file)
    lable_files(image_folder,csv_file)
