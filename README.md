# NetworkData
A project to gather network data over a long period of time. 

## checkSpeed.py
The main script. Tests network connection speed (upload, download, ping) and stores it in csv format. Takes 1 optional argument defining the path of the output csv file. Default (no arguments) is to output.csv

## Crontab
You can use crontab to run checkSpeed at specified intervals.

### To setup:
Run `crontab -e`.

Then append this line to your crontab to run the script every 30 mins:

    0,30 * * * * python [absolute path to checkSpeed.py] [absolute path to output csv file]

Or every hour:

    0 * * * * python [absolute path to checkSpeed.py] [absolute path to output csv file]
