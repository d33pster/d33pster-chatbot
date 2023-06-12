#!/usr/bin/env python

import warnings
import platform
import os

def refresh():
    if platform.system()=='Windows':
        os.system("cls")
    elif platform.system()=='Linux':
        os.system("clear")

os.system("conda create --name d33pster python=3.8 -y & conda activate d33pster")
refresh()
os.system("python.exe -m pip install --upgrade pip")
os.system("pip install rasa==3.5.11")
refresh()
os.system("conda deactivate")