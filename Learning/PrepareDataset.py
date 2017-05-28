#!/usr/bin/python3

import Preprocessing.TTF.FontManipulator as fmanip
import Preprocessing.Other.ConfigGenerator as CnfGen
import Preprocessing.ImageSet.LearningImageSetGenerator as learning
import Preprocessing.ImageSet.TestingImageSetGenerator as testing
import Preprocessing.ImageSet.LabelSet as label
import Learning.KNNClassifier as knn

def prepare_dataset():
    label.normalize_ttf_lable()
    learning.generate_learning_images()
    testing.generate_testing_samples()
    label.label_training_set()
    label.lable_testing_set()


if __name__ == "__main__":
    prepare_dataset()

