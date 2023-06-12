#!/usr/bin/env python

import os
import platform
import warnings

def refresh():
    if platform.system()=='Windows':
        os.system("cls")
    elif platform.system()=='Linux':
        os.system("clear")

refresh()
envPath = os.path.join(os.path.join(os.getcwd(), 'd33pster'), 'env.py')        
os.system(f"python {envPath}")
refresh()

# ch = int(input("Press 0 to train ... "))
# if ch==0:
#     trainPath = os.path.join(os.path.join(os.getcwd(), 'd33pster'), 'train.py')
#     os.system(f"python {trainPath}")

shellPath = os.path.join(os.path.join(os.getcwd(), 'd33pster'), 'shell.py')
os.system(f"python {shellPath}")