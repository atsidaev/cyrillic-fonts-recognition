#!/usr/bin/python3

import os
import configparser as cp
def change_cfg_value(section, variable, value):
    configfile_name = "config.ini"
    Config = cp.ConfigParser()
    Config.read(configfile_name)
    Config.set(section, variable, value)
    with open(configfile_name, "w+") as configfile:
        Config.write(configfile)

def generate_default_config():
    configfile_name =  "config.ini"

    if not os.path.isfile(configfile_name):
        print("Default config generation...")
        cfgfile = open(configfile_name, 'w')
        Config = cp.ConfigParser()

        Config.add_section('Directories')
        Config.set('Directories', 'Data', os.path.join(os.getcwd(), 'Data'))
        Config.set('Directories','TTFData', os.path.join(os.getcwd(), 'Data/TTFData'))
        Config.set('Directories', 'LearningSampleFolder', os.path.join(os.getcwd(), 'Data','LearningSamples'))
        Config.set('Directories', 'TestingSampleFolder', os.path.join(os.getcwd(), 'Data','TestingSamples'))
        Config.set('Directories', 'RawImageFolder', os.path.join(os.getcwd(), 'Data','RawImages'))

        Config.add_section('Datasets')
        Config.set('Datasets', 'Classes', os.path.join(os.getcwd(), "Data", "Classes.csv"))
        Config.set('Datasets', 'IsTrainingSetLabled', "False")
        Config.set('Datasets', 'IsTestingSetLabled', "False")

        #Config.add_section("DatasetSettings")
        #TODO: добавить настройки генерации выборки

        Config.add_section("Models")
        Config.set('Models', 'KnnModel', os.path.join(os.getcwd(), "Models", "KNN_model.sav"))

        Config.add_section("KNNSettings")
        Config.set("KNNSettings", "Neighbours", str(33))
        Config.set("KNNSettings", "Weights", "distance")
        Config.set("KNNSettings", "Algorithm", "kd_tree")
        Config.set("KNNSettings", "LeafSize", str(30))
        Config.set("KNNSettings", "Metric", "minkowski")
        Config.set("KNNSettings", "PowerParameter", str(2))

        Config.write(cfgfile)
        cfgfile.close()
