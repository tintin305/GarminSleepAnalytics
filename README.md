# GarminSleepAnalytics
Extraction and analysis of sleep data from Garmin watches.


The aim of this repository is to gain insight from the wealth of data that is gathered from wearing a smartwatch.

The Garmin series of watches is capable of recording a number of parameters about the sleep of the user.

The Garmin application currently works such that the user selects what time is usually alotted for sleep. It then makes assumptions based on the movement data, in addition to the other sensors included in the watch.

Garmin allows for the download of this data (as well as other data sets that they record.) for the user to make use of.

# Data Download

The current system of viewing the data that the watch records is from [this](https://connect.garmin.com/modern/) link from Garmin.

The downside of this system is that the user is constrained by the visuals presented by the Garmin team, which is often handy, however, sometimes it can be helpful to view it in different ways, or to observe long term trends. The connect application currently doesn't offer this functionality.

Garmin, as with all companies who gather data on their users, are required by [certain regulations](https://www.garmin.com/en-US/account/datamanagement/) to provide users with the ability to download all of the data that is associated with them. This is also to do with the privacy policies that they enforce.

The best way to download all of this data is to use the following [link](https://www.garmin.com/en-US/account/datamanagement/exportdata/) where you can choose to [delete your data](https://www.garmin.com/en-US/account/datamanagement/deletedata/), [view your data](https://www.garmin.com/en-US/account/datamanagement/viewdata/), or [request your data for export](https://www.garmin.com/en-US/account/datamanagement/exportdata/).

The data takes a while to be compiled from their side, then it is sent through as an email.

# Data Format


The data generated is downloaded as a zipped file. It contains a number of folders with all of the different data that is kept.
The data for the sleep is kept in the following directory:

```
/DI_CONNECT/DI-Connect-Wellness/
```

The formats for each of the sleep data files have the following naming schemes:

```
2019-06-29_2019-10-07_123456789_sleepData.json
```

## JSON Format

The structure suggests that each file contains the sleep data for the range specified in the file name. It is then followed by an eight digit number, which must correspond to some form of user ID used by Garmin.


The sleep data is stored in a JSON format. The format of the file is illustrated as follows, where each entry corresponds to a _sleep activity_:

```
{"sleepStartTimestampGMT":"2019-08-04T20:28:00.0","sleepEndTimestampGMT":"2019-08-05T04:30:00.0","calendarDate":"2019-08-05","sleepWindowConfirmationType":"ENHANCED_CONFIRMED_FINAL","deepSleepSeconds":600,"lightSleepSeconds":19440,"remSleepSeconds":8460,"awakeSleepSeconds":420,"unmeasurableSeconds":0,"retro":false}
```

The corresponds to a successful sleep recording.

In the case that the system could not detect the sleep activity, then the entry will have the following structure:

```
{"sleepStartTimestampGMT":"2019-08-03T20:00:00.0","sleepEndTimestampGMT":"2019-08-04T04:00:00.0","calendarDate":"2019-08-04","sleepWindowConfirmationType":"UNCONFIRMED","retro":false}
```



















