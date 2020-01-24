#!/usr/bin/env python

import csv
import pandas as pd
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import datetime
import matplotlib.pyplot as plt

import glob

def loadData():

    folderLocation = '../GarminData/DI_CONNECT/DI-Connect-Wellness/*.json'

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

    return sleepData


def saveRawSleepEntries(sleepData):

    sleepData.to_csv('../FormattedData/GarminSleepData.csv', index=False)

    return sleepData


# This will remove the entries where the sleep for that day was not successfully recorded.s
def removeUnconfirmedSleepEntries(sleepData):

    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'UNCONFIRMED'].index, inplace = True)

    return sleepData

def saveConfirmedSleepEntries(sleepData):

    sleepData.to_csv('../FormattedData/ConformedSleepDataEntries.csv', index=False)

    return None

def getMeanValues(sleepData):

    print(sleepData['deepSleepSeconds'].mean())
    print(sleepData['lightSleepSeconds'].mean())
    print(sleepData['remSleepSeconds'].mean())
    print(sleepData['awakeSleepSeconds'].mean())
    print(sleepData['unmeasurableSeconds'].mean())
 
    labels = ['deepSleepSeconds','lightSleepSeconds','remSleepSeconds','awakeSleepSeconds','unmeasurableSeconds']
    sizes = [(sleepData['deepSleepSeconds'].mean()), (sleepData['lightSleepSeconds'].mean()), (sleepData['remSleepSeconds'].mean()), (sleepData['awakeSleepSeconds'].mean()), (sleepData['unmeasurableSeconds'].mean())]
    colours = ['darkblue', 'blue', 'purple', 'pink', 'red']
    explode = (0.1, 0, 0, 0)  # explode 1st slice

    patches, texts = plt.pie(sizes, colors=colours, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

    return None

if __name__ == "__main__":

    sleepData = loadData()
    
    sleepData = saveRawSleepEntries(sleepData)

    confirmedSleepEntries = removeUnconfirmedSleepEntries(sleepData)

    saveConfirmedSleepEntries(confirmedSleepEntries)

    getMeanValues(sleepData)




