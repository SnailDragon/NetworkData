import time
import os
import sys

downtimeIn = sys.argv[1]
downtime = int(downtimeIn[0:2]) * 60*60 + int(downtimeIn[3:5]) * 60 + int(downtimeIn[6:8])

timelimitIn = sys.argv[2]
if(timelimitIn != ""):
    timelimit = int(timelimitIn[0:2]) * 60*60*24 + int(timelimitIn[3:5]) * 60*60 + int(timelimitIn[6:8]) * 60 + int(timelimitIn[9:11])
else:
    timelimit = 9999999999

start = time.time()
current = time.time()

os.system("speedtest-cli --csv-header > output.csv")

while(current - start < timelimit):
    current = time.time()
    print(f"{current - start} < {timelimit}")
    os.system("speedtest-cli --csv >> output.csv")

    time.sleep(downtime)