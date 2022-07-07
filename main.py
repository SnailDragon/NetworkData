import time
import os

downtimeIn = input("Enter time between tests (hh:mm:ss): ")
downtime = int(downtimeIn[0:2]) * 60*60 + int(downtimeIn[3:5]) * 60 + int(downtimeIn[6:8])

timelimitIn = input("Enter duration of test or skip (dd:hh:mm:ss): ")
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