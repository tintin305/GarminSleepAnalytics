#!/usr/bin/env python

import csv
import pandas as pd
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import datetime

import glob

def loadData():


    folderLocation = './Data/DI_CONNECT/DI-Connect-Wellness/*.json'

    fileNames = []

    fileNames = glob.glob(folderLocation)

    sleepData = pd.DataFrame()


    for sleepFile in fileNames:
        data = pd.read_json(sleepFile)

        sleepData = pd.concat([sleepData, data], ignore_index=True, sort=False)

    # Making the date and time columns datetime objects.
    sleepData['sleepStartTimestampGMT'] = pd.to_datetime(sleepData['sleepStartTimestampGMT']) 
    sleepData['sleepEndTimestampGMT'] = pd.to_datetime(sleepData['sleepEndTimestampGMT'])
    sleepData['calendarDate'] = pd.to_datetime(sleepData['calendarDate'])


    print(sleepData.mean())



    sleepData = []
    return sleepData



if __name__ == "__main__":

    sleepData = loadData()

