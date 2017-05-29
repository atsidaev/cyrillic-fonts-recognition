#!/usr/bin/python3

from sklearn.neighbors import KNeighborsClassifier
import Learning.ClassifierTools as tools
import pickle
import configparser as cp


def read_parameters():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    n_neighbors_count = config.get("KNNSettings", "Neighbours")
    weights = config.get("KNNSettings", "Weights")
    algorithm = config.get("KNNSettings", "Algorithm")
    metric = config.get("KNNSettings", "Metric")
    power = config.get("KNNSettings", "PowerParameter")
    return n_neighbors_count, weights, algorithm, metric, power

def train_classifier():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))

    train_set_folder = config.get("Directories", "learningsamplefolder")
    features, labels = tools.read_dataset(train_set_folder)
    #TODO:проверить
    features = tools.normalize_set(features)

    n_neighbors_count, weights, algorithm, metric, power = read_parameters()

    model = KNeighborsClassifier(n_neighbors=int(n_neighbors_count), weights=weights, algorithm=algorithm,
                                 metric=metric, p=int(power))
    model.fit(features, labels)
    tools.save_model(model, "KNNmodel")


def test_classifier():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "knnmodel")
    test_set_folder = config.get("Directories", "testingsamplefolder")
    features, labels = tools.read_dataset(test_set_folder)

    features = tools.normalize_set(features)

    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(features, labels)
    print("Accurancy for KNN:", result*100, "%")
