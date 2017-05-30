#!/usr/bin/python3


import Learning.ClassifierTools as tools
import pickle
import configparser as cp
import sklearn.gaussian_process as gp
from sklearn.metrics import classification_report
def read_parameters():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))


def train_classifier(features, labels):
    classifier = gp.GaussianProcessClassifier()
    classifier.fit(features, labels)
    tools.save_model(classifier, "gaussmodel")

def test_classifier(features, labels):
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "gaussmodel")
    loaded_model = pickle.load(open(filename, 'rb'))
    print("Gaussian Report \n")
    print(classification_report(loaded_model.predict(features),labels))
    result = loaded_model.score(features, labels)
    print("Accurancy for Gaussian Model:", result*100, "%")


