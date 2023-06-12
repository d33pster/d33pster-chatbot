#!/usr/bin/env python
import os
import warnings

os.system("conda activate d33pster")
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=DeprecationWarning)
    os.system("rasa train")

os.system("conda deactivate")