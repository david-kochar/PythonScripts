# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 13:23:32 2020

@author: kocha
"""
from pathlib import Path
import shutil
import os

dirpath = Path("data_set")
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)
    
file_path = os.mkdir("data_set")