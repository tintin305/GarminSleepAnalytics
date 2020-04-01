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


if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()


    plotStartEndSleepTimes(sleepData)


