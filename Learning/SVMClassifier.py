#!/usr/bin/python3
import sklearn.preprocessing as pp
import sklearn.svm as svm
from sklearn.metrics import classification_report
import Learning.ClassifierTools as tools
import pickle
import configparser as cp
from Preprocessing.ImageSet import LabelSet as ls
from Preprocessing.ImageSet import TestingImageSetGenerator as tisg
import os

def train_classifier(features, labels):
    classifier = svm.SVC(C=2.0, kernel = 'linear',decision_function_shape = 'ovr')
    classifier.fit(features, labels)
    tools.save_model(classifier, "SVMModel")

def load():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "SVMmodel")
    loaded_model = pickle.load(open(filename, 'rb'))
    return loaded_model


def test_classifier(features, labels):
    loaded_model = load()
    print("SVM Report \n")
    print(classification_report(loaded_model.predict(features), labels, target_names=ls.get_classes_names()))

def predict(image):
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    dir = config.get("Directories", "rawimagefolder")
    tisg.generate_sample_from_image(image,"_temp_", dir)
    roi = [f for f in os.listdir(dir) if "_temp_" in f]
    labels = ls.get_classes_names()
    loaded_model = load()
    predictions = []
    for f in roi:
        vector = tools.normalize_set([tools.image_to_feature_vector(os.path.join(dir, f))])
        prediction = loaded_model.predict(vector)
        predictions.append(int(prediction[0]))
    for f in roi:
        os.remove(os.path.join(dir,f))
    result = max(set(predictions), key=predictions.count)
    print("SVM result for file", image, "is", labels[result])