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

if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = dayOfWeekData(sleepData)

    timeViolinPlots(daySleepData)

