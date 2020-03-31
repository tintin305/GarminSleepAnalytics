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

# Values of sleepMeanValues are formatted in a vector in the order of: deepSleepSeconds, lightSleepSeconds, remSleepSeconds, awakeSleepSeconds.
def plotMeanPieChart(sleepMeanValues):

    # TODO Determine what/if the DPI setting for this needs to be.
    # TODO There is a warning on creating the postscript, that the backend doesn't support transparency.
    # TODO Have the values for each of the part of the chart displayed on the chart.

    labels = ['deepSleepSeconds','lightSleepSeconds','remSleepSeconds','awakeSleepSeconds']
    sizes = [sleepMeanValues[0], sleepMeanValues[1], sleepMeanValues[2], sleepMeanValues[3]]
    colours = ['darkblue', 'blue', 'purple', 'pink']
    # explode = (0.1, 0, 0, 0)  # explode 1st slice

    patches, texts = plt.pie(sizes, colors=colours, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    fileName = '../AnalysisFigures/MeanSleepSecondsPerType'

    plt.savefig(fileName + '.eps', format='eps', dpi=2200, bbox_inches='tight')
    plt.savefig(fileName + '.pdf', format='pdf', dpi=2200, bbox_inches='tight')
    plt.close('all')

    return None

# Plots a line for each sleep type for each day of the week.
def plotDayTrend(sleepData):



    return None



def dayOfWeekData(sleepData):

    sleepData['Day'] = sleepData['sleepEndTimestampGMT'].dt.dayofweek

    # Removing days that have NaN values, ie days that are 'Off Wrist', or 'AUTO_CONFIRMED_FINAL'
    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'AUTO_CONFIRMED_FINAL'].index, inplace=True)
    sleepData.drop(sleepData[sleepData['sleepWindowConfirmationType'] == 'OFF_WRIST'].index, inplace=True)

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

    meanDaysData = [retroData, deepSleepData, lightSleepData, remSleepData, awakeSleepData, unmeasurableSleepData]
    
    with open('../FormattedData/meanDaysData.csv','w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(meanDaysData)

    return meanDays

# This will plot seven pie charts on one figure showing each day of the week.
def plotPieChartDayOfWeek(daySleepData):

    labels = ['deepSleepSeconds','lightSleepSeconds','remSleepSeconds','awakeSleepSeconds']
    sizes = [sleepMeanValues[0], sleepMeanValues[1], sleepMeanValues[2], sleepMeanValues[3]]
    colours = ['darkblue', 'blue', 'purple', 'pink']
    # explode = (0.1, 0, 0, 0)  # explode 1st slice

    patches, texts = plt.pie(sizes, colors=colours, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    fileName = '../AnalysisFigures/MeanSleepSecondsPerType'

    plt.savefig(fileName + '.eps', format='eps', dpi=2200, bbox_inches='tight')
    plt.savefig(fileName + '.pdf', format='pdf', dpi=2200, bbox_inches='tight')
    plt.close('all')



    return None


def timeViolinPlots(daySleepData):


    print(daySleepData[0])
    sns.set(style='whitegrid')
    # fig, ax = plt.subplots(figsize =(9, 7)) 
    sns.violinplot(x = 'AwakeSleepSeconds', data = daySleepData[0]['awakeSleepSeconds'])
    plt.show()



    return None


# This will return the number corresponding to whatever day string you provide the function.
def daySwitcher(day):

    switcher = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }

    return switcher.get(day, 'Invalid day')


def plotStartEndSleepTimes(sleepData):


    # This gets that start sleep datetime in a list.    
    startDate = sleepData['sleepStartTimestampGMT'].to_list()

    # This gets the start sleep date.
    startDay = [date.date() for date in startDate]

    # This gets the start sleep time.
    startTime = [date.time() for date in startDate]

    # This does the same except for the end sleep time.
    endDate = sleepData['sleepEndTimestampGMT'].to_list()
    endDay = [date.date() for date in endDate]

    endTime = [date.time() for date in endDate]

    plt.scatter(startDay, startTime, color='blue')
    plt.scatter(endDay, endTime, color='red')
    plt.gcf().autofmt_xdate()
    plt.title('Start and end times')
    # plt.gcf().autofmt_ydate()
    plt.show()


    return None


def plotDayStartEndSleepTimes(daySleepData, day):

    mondayData = daySleepData[daySwitcher(day)]

    # This gets that start sleep datetime in a list.    
    mondayStartDate = mondayData['sleepStartTimestampGMT'].to_list()

    # This gets the start sleep date.
    mondayStartDay = [date.date() for date in mondayStartDate]

    # This gets the start sleep time.
    mondayStartTime = [date.time() for date in mondayStartDate]

    # This does the same except for the end sleep time.
    mondayEndDate = mondayData['sleepEndTimestampGMT'].to_list()
    mondayEndDay = [date.date() for date in mondayEndDate]

    mondayEndTime = [date.time() for date in mondayEndDate]

    plt.scatter(mondayStartDay, mondayStartTime, color='blue')
    plt.scatter(mondayEndDay, mondayEndTime, color='red')
    plt.gcf().autofmt_xdate()
    plt.title('Start and end times for %s' % str(day))
    # plt.gcf().autofmt_ydate()
    plt.show()

    return None


def plotDaySleepDistribution(daySleepData):

    # Get a column which represents the total sleep per day. This is the sum of the individual sleep types.
    mondayData = daySleepData[0]
    mondayData['AccumulatedSleep'] = mondayData['deepSleepSeconds'] + mondayData['lightSleepSeconds'] + mondayData['remSleepSeconds']
    
    tuesdayData = daySleepData[1]
    tuesdayData['AccumulatedSleep'] = tuesdayData['deepSleepSeconds'] + tuesdayData['lightSleepSeconds'] + tuesdayData['remSleepSeconds']

    wednesdayData = daySleepData[2]
    wednesdayData['AccumulatedSleep'] = wednesdayData['deepSleepSeconds'] + wednesdayData['lightSleepSeconds'] + wednesdayData['remSleepSeconds']

    thursdayData = daySleepData[3]
    thursdayData['AccumulatedSleep'] = thursdayData['deepSleepSeconds'] + thursdayData['lightSleepSeconds'] + thursdayData['remSleepSeconds']

    fridayData = daySleepData[4]
    fridayData['AccumulatedSleep'] = fridayData['deepSleepSeconds'] + fridayData['lightSleepSeconds'] + fridayData['remSleepSeconds']

    saturdayData = daySleepData[5]
    saturdayData['AccumulatedSleep'] = saturdayData['deepSleepSeconds'] + saturdayData['lightSleepSeconds'] + saturdayData['remSleepSeconds']

    sundayData = daySleepData[6]
    sundayData['AccumulatedSleep'] = sundayData['deepSleepSeconds'] + sundayData['lightSleepSeconds'] + sundayData['remSleepSeconds']


    mondaySleepList = mondayData['AccumulatedSleep'].to_numpy()
    mondaySleepList = np.divide(mondaySleepList, 60**2)
    # mondayDataFrame = pd.DataFrame({'Monday': mondaySleepList})

    # mondayDataFrame.Monday.plot(kind='hist', density=True)
    mean = mondaySleepList.mean()    
    sigma = mondaySleepList.std()

    s = np.random.normal(mean, sigma, 3000)
    # print(abs(mean - np.mean(std)) < 0.01)
    # print(abs(std - np.std(std, ddof=1)) < 0.01)

    count, bins, ignored = plt.hist(s, 100, normed=True)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mean)**2 / (2 * sigma**2) ), linewidth=2, color='r', label='Monday')
    plt.show()

    return None

if __name__ == "__main__":

    # Load in the confirmed sleep data entries.
    sleepData = loadConfirmedData()

    # Save the mean values from each of the different sleep groups.
    setMeanValues(sleepData)

    sleepMeanValues = getMeanValues()

    # plotMeanPieChart(sleepMeanValues)

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = dayOfWeekData(sleepData)

    # plotStartEndSleepTimes(sleepData)

    # plotDayStartEndSleepTimes(daySleepData, 'Monday')

    # timeViolinPlots(daySleepData)


    # meanDays(daySleepData)

    # plotDayTrend(sleepData)

    # plotPieChartDayOfWeek(daySleepData)


    plotDaySleepDistribution(daySleepData)

