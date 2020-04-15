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
    sundayData = daySleepData[0]
    sundayData['AccumulatedSleep'] = sundayData['deepSleepSeconds'] + sundayData['lightSleepSeconds'] + sundayData['remSleepSeconds']

    mondayData = daySleepData[1]
    mondayData['AccumulatedSleep'] = mondayData['deepSleepSeconds'] + mondayData['lightSleepSeconds'] + mondayData['remSleepSeconds']
    
    tuesdayData = daySleepData[2]
    tuesdayData['AccumulatedSleep'] = tuesdayData['deepSleepSeconds'] + tuesdayData['lightSleepSeconds'] + tuesdayData['remSleepSeconds']

    wednesdayData = daySleepData[3]
    wednesdayData['AccumulatedSleep'] = wednesdayData['deepSleepSeconds'] + wednesdayData['lightSleepSeconds'] + wednesdayData['remSleepSeconds']

    thursdayData = daySleepData[4]
    thursdayData['AccumulatedSleep'] = thursdayData['deepSleepSeconds'] + thursdayData['lightSleepSeconds'] + thursdayData['remSleepSeconds']

    fridayData = daySleepData[5]
    fridayData['AccumulatedSleep'] = fridayData['deepSleepSeconds'] + fridayData['lightSleepSeconds'] + fridayData['remSleepSeconds']

    saturdayData = daySleepData[6]
    saturdayData['AccumulatedSleep'] = saturdayData['deepSleepSeconds'] + saturdayData['lightSleepSeconds'] + saturdayData['remSleepSeconds']




    mondaySleepList = mondayData['AccumulatedSleep'].to_numpy()
    mondaySleepList = np.divide(mondaySleepList, 60**2)

    tuesdaySleepList = tuesdayData['AccumulatedSleep'].to_numpy()
    tuesdaySleepList = np.divide(tuesdaySleepList, 60**2)

    wednesdaySleepList = wednesdayData['AccumulatedSleep'].to_numpy()
    wednesdaySleepList = np.divide(wednesdaySleepList, 60**2)

    thursdaySleepList = thursdayData['AccumulatedSleep'].to_numpy()
    thursdaySleepList = np.divide(thursdaySleepList, 60**2)

    fridaySleepList = fridayData['AccumulatedSleep'].to_numpy()
    fridaySleepList = np.divide(fridaySleepList, 60**2)

    saturdaySleepList = saturdayData['AccumulatedSleep'].to_numpy()
    saturdaySleepList = np.divide(saturdaySleepList, 60**2)

    sundaySleepList = sundayData['AccumulatedSleep'].to_numpy()
    sundaySleepList = np.divide(sundaySleepList, 60**2)


    fig, axes = plt.subplots(1, 7, figsize=(10,3), sharey=True, dpi=100)
    sns.distplot(mondaySleepList, color="dodgerblue", ax=axes[0], axlabel='Monday Sleep Hours')
    sns.distplot(tuesdaySleepList, color="dodgerblue", ax=axes[1], axlabel='Tuesday Sleep Hours')
    sns.distplot(wednesdaySleepList, color="dodgerblue", ax=axes[2], axlabel='Wednesday Sleep Hours')
    sns.distplot(thursdaySleepList, color="dodgerblue", ax=axes[3], axlabel='Thursday Sleep Hours')
    sns.distplot(fridaySleepList, color="dodgerblue", ax=axes[4], axlabel='Friday Sleep Hours')
    sns.distplot(saturdaySleepList, color="dodgerblue", ax=axes[5], axlabel='Saturday Sleep Hours')
    sns.distplot(sundaySleepList, color="dodgerblue", ax=axes[6], axlabel='Sunday Sleep Hours')
    fig.show()
    plt.show()


    kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'linewidth':2})
    plt.figure(figsize=(10,3), dpi=100)
    sns.distplot(mondaySleepList, label='Monday Sleep Hours', **kwargs)
    sns.distplot(tuesdaySleepList, label='Tuesday Sleep Hours', **kwargs)
    sns.distplot(wednesdaySleepList, label='Wednesday Sleep Hours', **kwargs)
    sns.distplot(thursdaySleepList, label='Thursday Sleep Hours', **kwargs)
    sns.distplot(fridaySleepList, label='Friday Sleep Hours', **kwargs)
    sns.distplot(saturdaySleepList, label='Saturday Sleep Hours', **kwargs)
    sns.distplot(sundaySleepList, label='Sunday Sleep Hours', **kwargs)
    plt.legend()
    plt.show()


    return None


if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = AnalyseData.dayOfWeekData(sleepData)

    plotDaySleepDistribution(daySleepData)
