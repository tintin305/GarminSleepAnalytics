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

def plotMeanPieChart(sleepData):

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

def getMeanValues(sleepData):

    print(sleepData['deepSleepSeconds'].mean())
    print(sleepData['lightSleepSeconds'].mean())
    print(sleepData['remSleepSeconds'].mean())
    print(sleepData['awakeSleepSeconds'].mean())
    print(sleepData['unmeasurableSeconds'].mean())

    return None

# Plots a line for each sleep type for each day of the week.
def plotDayTrend(sleepData):



    return None

def dayData(sleepData):

    sleepData['Day'] = sleepData['sleepEndTimestampGMT'].dt.dayofweek

    mondayData = sleepData[sleepData['Day']==0]
    tuesdayData = sleepData[sleepData['Day']==1]
    wednesdayData = sleepData[sleepData['Day']==2]
    thursdayData = sleepData[sleepData['Day']==3]
    fridayData = sleepData[sleepData['Day']==4]
    saturdayData = sleepData[sleepData['Day']==5]
    sundayData = sleepData[sleepData['Day']==6]

    daySleepData = [mondayData, tuesdayData, wednesdayData, thursdayData, fridayData, saturdayData, sundayData]

    return daySleepData

# Gets the mean values for each sleep type for each day of the week.
def meanDays(daySleepData):

    meanMonday = daySleepData[0].mean()
    meanTuesday = daySleepData[1].mean()
    meanWednesday = daySleepData[2].mean()
    meanThursday = daySleepData[3].mean()
    meanFriday = daySleepData[4].mean()
    meanSaturday = daySleepData[5].mean()
    meanSunday = daySleepData[6].mean()

    meanDays = [meanMonday, meanTuesday, meanWednesday, meanThursday, meanFriday, meanSaturday, meanSunday]

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

    numDays = 5
    ind = np.arange(numDays)
    width = 0.35

    p1 = plt.bar(ind, retroData, color='b')
    p2 = plt.bar(ind, deepSleepData, color='r', bottom=retro)

    # plt.ylabel('Mean Seconds')
    # plt.title('Mean day sleep by type')
    # plt.xticks(ind, ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'))
    # plt.yticks(np.arange(0, 8100, 100))
    # plt.legend((p1[0], p2[0]), ('retro', 'Deep Sleep Data'))

    plt.show()

    return meanDays

if __name__ == "__main__":

    sleepData = loadData()
    
    sleepData = saveRawSleepEntries(sleepData)

    confirmedSleepEntries = removeUnconfirmedSleepEntries(sleepData)

    saveConfirmedSleepEntries(confirmedSleepEntries)

    # getMeanValues(sleepData)

    # plotMeanPieChart(sleepData)

    daySleepData = dayData(sleepData)

    meanDays(daySleepData)

    plotDayTrend(sleepData)




