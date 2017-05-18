#!/usr/bin/python3
import os

def check_and_generate_folders(folders):
    for f in folders:
        if not os.path.exists(f):
            os.makedirs(f)