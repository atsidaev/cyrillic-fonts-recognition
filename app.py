#!/usr/bin/python3
import Preprocessing.Other.ConfigGenerator as cg
from Learning import PrepareDataset as pd
from Learning import KNNClassifier as knn
from Learning import SVMClassifier as svm
if __name__ == "__main__":
    cg.generate_default_config()
    pd.prepare_dataset()

    print("Train Classifiers...")
    knn.train_classifier()
    svm.train_classifier()

    print("Test Classifiers...")
    knn.test_classifier()
    svm.test_classifier()