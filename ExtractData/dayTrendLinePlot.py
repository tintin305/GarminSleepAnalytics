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


# Plots a line for each sleep type for each day of the week.
def plotDayTrend(sleepData):


    return None


if __name__ == "__main__":

    sleepData = AnalyseData.loadConfirmedData()

    plotDayTrend(sleepData)


