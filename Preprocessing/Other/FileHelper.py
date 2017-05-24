#!/usr/bin/python3
import os
import configparser as cp

def check_and_generate_folders(folders):
    for f in folders:
        if not os.path.exists(f):
            print("Not found folder", f, "\nFrom config file, creating folders.")
            os.makedirs(f)
