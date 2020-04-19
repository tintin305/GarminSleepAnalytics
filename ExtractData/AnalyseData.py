#!/usr/bin/env python

import csv
import pandas as pd
import numpy as np
import sys, os
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import glob
import seaborn as sns


import ExtractGarminData

from scipy.stats import norm
import pylab

import warnings
warnings.filterwarnings("ignore")

# Load in the confirmed sleep entries.
def loadConfirmedData():

    fileName = '../FormattedData/ConfirmedSleepDataEntries.csv'
    sleepData = pd.read_csv(fileName)

    # Making the date and time columns datetime objects.
    sleepData['sleepStartTimestampGMT'] = pd.to_datetime(sleepData['sleepStartTimestampGMT']) 
    sleepData['sleepEndTimestampGMT'] = pd.to_datetime(sleepData['sleepEndTimestampGMT'])
    sleepData['calendarDate'] = pd.to_datetime(sleepData['calendarDate'])

    # It appears as if the time in the json file is not accommodating for the GMT+2. So I am applying this here.
    sleepData['sleepStartTimestampGMT'] = sleepData['sleepStartTimestampGMT'] + timedelta(hours=2)
    sleepData['sleepEndTimestampGMT'] = sleepData['sleepEndTimestampGMT'] + timedelta(hours=2)

    return sleepData


def setMeanValues(sleepData):

    deepSleepAverage = sleepData['deepSleepSeconds'].mean()
    lightSleepAverage = sleepData['lightSleepSeconds'].mean()
    remSleepAverage = sleepData['remSleepSeconds'].mean()
    awakeSleepAverage = sleepData['awakeSleepSeconds'].mean()

    fileName = '../FormattedData/meanSleepSeconds.csv'
    with open(fileName, 'w') as outFile:
        outFile.write('deepSleepSeconds,' + str(deepSleepAverage) + '\n')
        outFile.write('lightSleepSeconds,' + str(lightSleepAverage) + '\n')
        outFile.write('remSleepSeconds,' + str(remSleepAverage) + '\n')
        outFile.write('awakeSleepSeconds,' + str(awakeSleepAverage) + '\n')

    return None


def getMeanValues():

    fileName = '../FormattedData/meanSleepSeconds.csv'
    sleepData = pd.read_csv(fileName, header=None)

    deepSleepAverage = sleepData[1].iloc[0]
    lightSleepAverage = sleepData[1].iloc[1]
    remSleepAverage = sleepData[1].iloc[2]
    awakeSleepAverage = sleepData[1].iloc[3]

    sleepMeanValues = [deepSleepAverage, lightSleepAverage, remSleepAverage, awakeSleepAverage]

    return sleepMeanValues


def removeNanEntries(sleepData):

    # Removing days that have NaN values, ie days that are 'Off Wrist', or 'AUTO_CONFIRMED_FINAL'
    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'AUTO_CONFIRMED_FINAL'].index, inplace=True)
    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'OFF_WRIST'].index, inplace=True)
    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'AUTO_CONFIRMED'].index, inplace=True)

    return sleepData


def dayOfWeekData(sleepData):

    sleepData['Day'] = sleepData['sleepEndTimestampGMT'].dt.dayofweek

    # Removint the rows that have NaN entries as part of the sleep.
    sleepData = removeNanEntries(sleepData)

    sundayData = sleepData[sleepData['Day']==0]
    mondayData = sleepData[sleepData['Day']==1]
    tuesdayData = sleepData[sleepData['Day']==2]
    wednesdayData = sleepData[sleepData['Day']==3]
    thursdayData = sleepData[sleepData['Day']==4]
    fridayData = sleepData[sleepData['Day']==5]
    saturdayData = sleepData[sleepData['Day']==6]


    daySleepData = [sundayData, mondayData, tuesdayData, wednesdayData, thursdayData, fridayData, saturdayData]

    return daySleepData


# Gets the mean values for each sleep type for each day of the week.
def setMeanDays(daySleepData):

    meanSunday = daySleepData[0].mean()
    meanMonday = daySleepData[1].mean()
    meanTuesday = daySleepData[2].mean()
    meanWednesday = daySleepData[3].mean()
    meanThursday = daySleepData[4].mean()
    meanFriday = daySleepData[5].mean()
    meanSaturday = daySleepData[6].mean()


    meanDays = [meanSunday, meanMonday, meanTuesday, meanWednesday, meanThursday, meanFriday, meanSaturday]

    retroData = []
    for day in meanDays:
        retroData.append(day['retro'])

    deepSleepData = []
    for day in meanDays:
        deepSleepData.append(day['deepSleepSeconds'])

    lightSleepData = []
    for day in meanDays:
        lightSleepData.append(day['lightSleepSeconds'])

    remSleepData = []
    for day in meanDays:
        remSleepData.append(day['remSleepSeconds'])

    awakeSleepData = []
    for day in meanDays:
        awakeSleepData.append(day['awakeSleepSeconds'])

    unmeasurableSleepData = []
    for day in meanDays:
        unmeasurableSleepData.append(day['unmeasurableSeconds'])

    meanDaysData = [retroData, deepSleepData, lightSleepData, remSleepData, awakeSleepData, unmeasurableSleepData]
    
    with open('../FormattedData/meanDaysData.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(meanDaysData)

    return None


# Gets the mean values for each sleep type for each day of the week.
def getMeanDays(daySleepData):

    meanSunday = daySleepData[0].mean()
    meanMonday = daySleepData[1].mean()
    meanTuesday = daySleepData[2].mean()
    meanWednesday = daySleepData[3].mean()
    meanThursday = daySleepData[4].mean()
    meanFriday = daySleepData[5].mean()
    meanSaturday = daySleepData[6].mean()


    meanDays = [meanSunday, meanMonday, meanTuesday, meanWednesday, meanThursday, meanFriday, meanSaturday]

    retroData = []
    for day in meanDays:
        retroData.append(day['retro'])

    deepSleepData = []
    for day in meanDays:
        deepSleepData.append(day['deepSleepSeconds'])

    lightSleepData = []
    for day in meanDays:
        lightSleepData.append(day['lightSleepSeconds'])

    remSleepData = []
    for day in meanDays:
        remSleepData.append(day['remSleepSeconds'])

    awakeSleepData = []
    for day in meanDays:
        awakeSleepData.append(day['awakeSleepSeconds'])

    unmeasurableSleepData = []
    for day in meanDays:
        unmeasurableSleepData.append(day['unmeasurableSeconds'])

    meanDaysData = [retroData, deepSleepData, lightSleepData, remSleepData, awakeSleepData, unmeasurableSleepData]
    
    
    return meanDays



# This will return the number corresponding to whatever day string you provide the function.
def daySwitcher(day):

    switcher = {
        'Sunday': 0,
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6
    }

    return switcher.get(day, 'Invalid day')




if __name__ == "__main__":

    # Load in the confirmed sleep data entries.
    sleepData = loadConfirmedData()

    # Save the mean values from each of the different sleep groups.
    setMeanValues(sleepData)

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = dayOfWeekData(sleepData)


    # meanDays(daySleepData)






