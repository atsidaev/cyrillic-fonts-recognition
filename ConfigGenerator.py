#!/usr/bin/python3

import os
import configparser as cp

configfile_name =  "config.ini"

if not os.path.isfile(configfile_name):
    cfgfile = open(configfile_name, 'w')
    Config = cp.ConfigParser()
    Config.add_section('Directories')
    Config.set('Directories', 'Data', os.path.join(os.getcwd(), 'Data'))
    Config.set('Directories','TTFData', os.path.join(os.getcwd(), 'Data/TTFData'))
    Config.set('Directories', 'LearningSampleFolder', os.path.join(os.getcwd(), 'Data','LearningSamples'))
    Config.set('Directories', 'TestingSampleFolder', os.path.join(os.getcwd(), 'Data','TestingSamples'))
    Config.set('Directories', 'RawImageFolder', os.path.join(os.getcwd(), 'Data','RawImages'))
    Config.set('Directories', 'DatasetFolder', os.path.join(os.getcwd(),'Data','Datasets'))
    Config.add_section('Datasets')
    Config.set('Datasets', 'TrainingDataset', os.path.join(os.getcwd(), "Data","Datasets", "TrainingDataset.csv"))
    Config.set('Datasets', 'TestingDataset', os.path.join(os.getcwd(), "Data", "Datasets", "TestingDataset.csv"))
    Config.set('Datasets', 'Classes', os.path.join(os.getcwd(), "Data", "Datasets", "Classes.csv"))
    Config.write(cfgfile)
    cfgfile.close()
