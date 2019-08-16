import os
from glob import glob
import pandas as pd

# Path where all input files are stores:
PATH = 'C://Users//t3175ks//Downloads//2019//Automation_Projects//To Khemraj S'

# Extension of file
EXT = "*.csv"

# All file names are stored in a variable all_csv_files
all_csv_files = [file
                 for path, subdir, files in os.walk(PATH)
                 for file in glob(os.path.join(path, EXT))]

