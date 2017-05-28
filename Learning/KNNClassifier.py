#!/usr/bin/python3

from sklearn.neighbors import KNeighborsClassifier
import Learning.ClassifierTools as tools
import numpy as np
import pickle

import configparser as cp
import os

def train_knn_classifier():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))

    train_set_folder = config.get("Directories", "learningsamplefolder")
    pix, lab = tools.read_dataset(train_set_folder)

    n_neighbors_count = config.get("KNNSettings", "Neighbours")
    weights = config.get("KNNSettings", "Weights")
    algorithm = config.get("KNNSettings", "Algorithm")
    metric = config.get("KNNSettings", "Metric")
    power = config.get("KNNSettings", "PowerParameter")

    model = KNeighborsClassifier(n_neighbors=int(n_neighbors_count), weights=weights, algorithm=algorithm, metric=metric, p=int(power))
    model.fit(pix, lab)

    filename = config.get("Models", "knnmodel")
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    pickle.dump(model, open(filename, 'wb'))
    print("KNN model saved.")
    return filename

def test_knn_classifier():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "knnmodel")
    test_set_folder = config.get("Directories", "testingsamplefolder")
    pix,lab = tools.read_dataset(test_set_folder)
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(pix, lab)
    print("Occurancy for KNN:", result, "%")


