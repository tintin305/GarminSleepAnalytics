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
import AnalyseData

from scipy.stats import norm
import pylab

import warnings
warnings.filterwarnings("ignore")


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

    sleepData = AnalyseData.loadConfirmedData()

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = dayOfWeekData(sleepData)

    plotDaySleepDistribution(daySleepData)
