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


if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()

    # This returns a vector where each item holds a dataframe for each day of the weeks data separated.
    daySleepData = AnalyseData.dayOfWeekData(sleepData)

    plotPieChartDayOfWeek(daySleepData)



