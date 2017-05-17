#!/usr/bin/python3

import os
import configparser as cp

configfile_name =  "config.ini"

if not os.path.isfile(configfile_name):
    cfgfile = open(configfile_name, 'w')
    Config = cp.ConfigParser()
    Config.add_section('Directories')
    Config.set('Directories','TTFData', os.path.join(os.getcwd(), 'TTFData'))
    Config.set('Directories', 'LearningSampleFolder', os.path.join(os.getcwd(), 'LearningSamples'))
    Config.set('Directories', 'TestingSampleFolder', os.path.join(os.getcwd(), 'TestingSamples'))
    Config.set('Directories', 'RawImageFolder', os.path.join(os.getcwd(), 'RawImages'))
    Config.set('Directories', 'DatasetFolder', os.path.join(os.getcwd(),'Datasets'))
    Config.add_section('Datasets')
    Config.set('Datasets', 'TrainingDataset', os.path.join(os.getcwd(), "Datasets", "TrainingDataset.csv"))
    Config.set('Datasets', 'TestingDataset', os.path.join(os.getcwd(), "Datasets", "TestingDataset.csv"))
    Config.set('Datasets', 'Classes', os.path.join(os.getcwd(), "Datasets", "Classes.csv"))
    Config.write(cfgfile)
    cfgfile.close()
