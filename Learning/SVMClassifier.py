#!/usr/bin/python3

import sklearn.svm as svm
import Learning.ClassifierTools as tools
import pickle
import configparser as cp
import os


def read_parameters():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    c = float(config.get("SVMSettings", "C"))
    cache_size = int(config.get("SVMSettings", "cache_size"))
    class_weight = None#config.get("SVMSettings", "class_weight")
    coef0 = float(config.get("SVMSettings", "coef0"))
    decision_function_shape = config.get("SVMSettings", "decision_function_shape")
    degree = int(config.get("SVMSettings", "degree"))
    gamma = config.get("SVMSettings", "gamma")
    kernel = config.get("SVMSettings", "kernel")
    max_iter = int(config.get("SVMSettings", "max_iter"))
    probability = bool(config.get("SVMSettings", "probability"))
    random_state = None#config.get("SVMSettings", "random_state")
    shrinking = bool(config.get("SVMSettings", "shrinking"))
    tol = float(config.get("SVMSettings", "tol"))
    verbose = bool(config.get("SVMSettings", "verbose"))
    return c, cache_size, class_weight, coef0, decision_function_shape, degree, gamma, kernel, max_iter, probability, random_state, shrinking, tol, verbose


def train_classifier():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))

    train_set_folder = config.get("Directories", "learningsamplefolder")

    features, labels = tools.read_dataset(train_set_folder)
    features = tools.normalize_set(features)
    c, cache_size, class_weight, coef0, decision_function_shape, degree, gamma, kernel, max_iter, probability, random_state, shrinking, tol, verbose = read_parameters()
    classifier = svm.SVC(C=c, cache_size=cache_size, class_weight=class_weight, coef0=coef0,
                         decision_function_shape=decision_function_shape, degree=degree, gamma=gamma, kernel=kernel,
                         max_iter=max_iter, probability=probability, random_state=random_state, shrinking=shrinking,
                         tol=tol, verbose=verbose)
    classifier.fit(features, labels)
    tools.save_model(classifier, "SVMModel")


def test_classifier():
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    filename = config.get("Models", "SVMModel")
    test_set_folder = config.get("Directories", "testingsamplefolder")
    features, labels = tools.read_dataset(test_set_folder)
    features = tools.normalize_set(features)
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.score(features, labels)
    print("Accurancy for SVM:", result*100, "%")
