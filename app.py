#!/usr/bin/python3
import Preprocessing.Other.ConfigGenerator as cg
from Learning import PrepareDataset as pd

if __name__ == "__main__":
    cg.generate_default_config()
    pd.prepare_dataset()
