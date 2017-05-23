#!/usr/bin/python3

import Preprocessing.Other.ConfigGenerator as CnfGen
import Preprocessing.ImageSet.LearningImageSetGenerator as learning
import Preprocessing.ImageSet.TestingImageSetGenerator as testing
import Preprocessing.ImageSet.LabelSet as label
import Learning.KNNClassifier as knn

def prepare_dataset():
    CnfGen.generate_default_config()
    learning.generate_learning_images()
    label.label_training_set()
    testing.generate_testing_samples()
    label.lable_testing_set()


if __name__ == "__main__":
   # prepare_dataset()
    file = knn.train_knn_classifier()
    knn.use_knn_classifier()
