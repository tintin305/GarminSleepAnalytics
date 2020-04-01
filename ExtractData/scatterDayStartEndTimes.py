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


def plotDayStartEndSleepTimes(daySleepData, day):

    mondayData = daySleepData[AnalyseData.daySwitcher(day)]

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


if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = dayOfWeekData(sleepData)

    plotDayStartEndSleepTimes(daySleepData, 'Monday')
    plotDayStartEndSleepTimes(daySleepData, 'Tuesday')
    plotDayStartEndSleepTimes(daySleepData, 'Wednesday')
    plotDayStartEndSleepTimes(daySleepData, 'Thursday')
    plotDayStartEndSleepTimes(daySleepData, 'Friday')
    plotDayStartEndSleepTimes(daySleepData, 'Saturday')
    plotDayStartEndSleepTimes(daySleepData, 'Sunday')


