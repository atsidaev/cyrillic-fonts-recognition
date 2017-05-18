#!/usr/bin/python3

import Preprocessing.Other.ConfigGenerator as CnfGen
import Preprocessing.ImageSet.LearningImageSetGenerator as learning
import Preprocessing.ImageSet.TestingImageSetGenerator as testing
import Preprocessing.ImageSet.LabelTrainingSet as label


def prepare_dataset():
    CnfGen.generate_default_config()
    learning.generate_learning_images()
    label.label_training_set()
    testing.generate_testing_samples()


if __name__ == "__main__":
    prepare_dataset()