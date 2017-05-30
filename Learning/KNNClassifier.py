#!/usr/bin/python3


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
import Learning.ClassifierTools as tools
import pickle
import configparser as cp


def train_classifier(features, labels):
    model = KNeighborsClassifier(n_neighbors=76, weights='distance', algorithm='kd_tree', metric='minkowski', p=2)
    model.fit(features, labels)
    tools.save_model(model, "KNNmodel")


def test_classifier(features, labels):
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "knnmodel")
    loaded_model = pickle.load(open(filename, 'rb'))
    print("KNN Report \n")
    print(classification_report(loaded_model.predict(features), labels))
    result = loaded_model.score(features, labels)
    print("Accurancy for KNN:", result * 100, "%")
