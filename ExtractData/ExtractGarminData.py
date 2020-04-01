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

    # The Garmin system creates a number of files which appear to have a maximum number of entries per file.
    # The longer the watch has been gathering data, the more files will be present.
    for sleepFile in fileNames:
        data = pd.read_json(sleepFile)
        # Concatenate the data onto the main dataframe.
        sleepData = pd.concat([sleepData, data], ignore_index=True, sort=False)

    # Making the date and time columns datetime objects.
    sleepData['sleepStartTimestampGMT'] = pd.to_datetime(sleepData['sleepStartTimestampGMT']) 
    sleepData['sleepEndTimestampGMT'] = pd.to_datetime(sleepData['sleepEndTimestampGMT'])
    sleepData['calendarDate'] = pd.to_datetime(sleepData['calendarDate'])

    return sleepData

    # Save the raw data to a csv.
def saveRawSleepEntries(sleepData):

    sleepData.to_csv('../FormattedData/GarminSleepData.csv', index=False)

    return None


# This will remove the entries where the sleep for that day was not successfully recorded.
def removeUnconfirmedSleepEntries(sleepData):

    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'UNCONFIRMED'].index, inplace = True)

    return sleepData

# This saves only the confirmed sleep data to a csv file.
def saveConfirmedSleepEntries(sleepData):

    sleepData.to_csv('../FormattedData/ConfirmedSleepDataEntries.csv', index=False)

    return None


if __name__ == "__main__":

    # Extract all of the raw data and save it to a csv file.
    sleepData = loadData()
    saveRawSleepEntries(sleepData)

    # Extract the confirmed entries and save this to a csv file.
    confirmedSleepEntries = removeUnconfirmedSleepEntries(sleepData)
    saveConfirmedSleepEntries(confirmedSleepEntries)