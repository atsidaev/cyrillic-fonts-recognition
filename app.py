#!/usr/bin/python3
import Preprocessing.Other.ConfigGenerator as cg
from Learning import PrepareDataset as pd
from Learning import KNNClassifier as knn
from Learning import SVMClassifier as svm
from Learning import GaussianProcessClassifier as gp
from Learning import ClassifierTools as tools
import configparser as cp
if __name__ == "__main__":

    cg.generate_default_config()
    pd.prepare_dataset()

    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    trainingSetFolder = config.get("Directories", "LearningSampleFolder")
    testingSetFolder = config.get("Directories", "TestingSampleFolder")
    print("Read datasets")
    trainFeat, trainLabels = tools.read_dataset(trainingSetFolder)
    testFeat, testLabels = tools.read_dataset(testingSetFolder)

    print("Train Classifiers...")
    knn.train_classifier(trainFeat, trainLabels)
    svm.train_classifier(trainFeat, trainLabels)
   # gp.train_classifier(trainFeat, trainLabels)


    print("Test Classifiers...")
    knn.test_classifier(testFeat, testLabels)
    svm.test_classifier(testFeat, testLabels)
    #gp.test_classifier(testFeat, testLabels)
