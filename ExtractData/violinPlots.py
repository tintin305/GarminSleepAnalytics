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


def timeViolinPlots(daySleepData):


    print(daySleepData[0])
    sns.set(style='whitegrid')
    # fig, ax = plt.subplots(figsize =(9, 7)) 
    sns.violinplot(x = 'AwakeSleepSeconds', data = daySleepData[0]['awakeSleepSeconds'])
    plt.show()


    return None


def monthlyViolinPlots(sleepData):

        # The dataframe needs to be formatted such that one column shows the total sleep for that whole day.
    sleepData['AccumulatedSleep'] = sleepData['deepSleepSeconds'] + sleepData['lightSleepSeconds'] + sleepData['remSleepSeconds']
    sleepData['AccumulatedSleep'] = sleepData['AccumulatedSleep'].div(60**2)
    sleepData['Month'] = sleepData['calendarDate'].apply(lambda t: t.strftime('%Y-%m'))
    sns.violinplot(data=sleepData, x='Month', y='AccumulatedSleep')
    plt.show()

    print(sleepData)


    return None


if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    # daySleepData = dayOfWeekData(sleepData)

    # timeViolinPlots(daySleepData)

    sleepData = AnalyseData.removeNanEntries(sleepData)
    monthlyViolinPlots(sleepData)
