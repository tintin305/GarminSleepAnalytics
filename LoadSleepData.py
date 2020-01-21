#!/usr/bin/env python

import csv
import pandas as pd
import numpy as np
import sys, os
import matplotlib.pyplot as plt

import glob

def loadData():


    folderLocation = './Data/DI_CONNECT/DI-Connect-Wellness/*.json'

    fileNames = []

    fileNames = glob.glob(folderLocation)

    sleepData = pd.DataFrame()


    for sleepFile in fileNames:
        data = pd.read_json(sleepFile)

        sleepData = pd.concat([sleepData, data], ignore_index=True)

    print(sleepData)



    sleepData = []
    return sleepData



if __name__ == "__main__":

    sleepData = loadData()

