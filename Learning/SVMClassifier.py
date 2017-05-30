#!/usr/bin/python3
import sklearn.preprocessing as pp
import sklearn.svm as svm
from sklearn.metrics import classification_report
import Learning.ClassifierTools as tools
import pickle
import configparser as cp

def train_classifier(features, labels):
    classifier = svm.SVC(C=2.0, kernel = 'linear',decision_function_shape = 'ovr')
    classifier.fit(features, labels)
    tools.save_model(classifier, "SVMModel")


def test_classifier(features, labels):
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "SVMModel")
    loaded_model = pickle.load(open(filename, 'rb'))
    print("SVM Report \n")
    print(classification_report(loaded_model.predict(features), labels))
    result = loaded_model.score(features, labels)
    print("Accurancy for SVM:", result*100, "%")
