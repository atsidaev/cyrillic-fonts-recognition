#!/usr/bin/python3
import Preprocessing.Other.ConfigGenerator as cg
from Learning import PrepareDataset as pd
from Learning import KNNClassifier as knn
from Learning import SVMClassifier as svm
from Learning import ClassifierTools as tools
from Preprocessing.Other.FileHelper import check_and_generate_folders
import configparser as cp
import argparse
import os

def training_routine():
    print("Initialize training routine")
    pd.prepare_dataset()
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    trainingSetFolder = config.get("Directories", "LearningSampleFolder")
    print("Read dataset")
    trainFeat, trainLabels = tools.read_dataset(trainingSetFolder)
    print("Train Classifiers...")
    knn.train_classifier(trainFeat, trainLabels)
    svm.train_classifier(trainFeat, trainLabels)

def pregen_test():
    print("Forming reports for pregenerated test set")
    config = cp.ConfigParser()
    config.read_file(open('config.ini'))
    testingSetFolder = config.get("Directories", "TestingSampleFolder")
    testFeat, testLabels = tools.read_dataset(testingSetFolder)
    knn.test_classifier(testFeat, testLabels)
    svm.test_classifier(testFeat, testLabels)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k',  help='predict with knn [-k filename.png]')
    parser.add_argument('-s', help='predict with svm [-s filename.png]')
    parser.add_argument('-t','--test', help='make model report with pregenerated data', action="store_true")
    args = parser.parse_args()
    if not any(vars(args).values()):
        print("Generate default configuration")
        cg.generate_default_config()
        config = cp.ConfigParser()
        config.read_file(open('config.ini'))
        folders = [config.get('Directories', 'ttfdata'), config.get('Directories', 'learningsamplefolder'),
                   config.get('Directories', 'testingsamplefolder'), config.get('Directories', 'rawimagefolder')]
        check_and_generate_folders(folders)
        if os.listdir(config.get('Directories', 'ttfdata')) == []:
            print("Now put your TTF/OTF files in TTFData folder to classify and launch program without args")
        else:
            training_routine()
    elif args.test:
        pregen_test()
    elif args.k:
        knn.predict(args.k)
    elif args.s:
        svm.predict(args.s)
    else:
        parser.print_help()
