import time
import speedtest

st = speedtest.Speedtest()

downtimeIn = input("Enter time between tests (hh:mm:ss): ")
downtime = int(downtimeIn[0:2]) * 60*60 + int(downtimeIn[3:5]) * 60 + int(downtimeIn[6:8])

timelimitIn = input("Enter duration of test or skip (dd:hh:mm:ss): ")
if(timelimitIn == ""):
    timelimit = int(timelimitIn[0:2]) * 60*60*24 + int(timelimitIn[3:5]) * 60*60 + int(timelimitIn[6:8]) * 60 + int(timelimitIn[9:11])
else:
    timelimit = 9999999999

start = time.time()

print(st.results.csv_header())
print()

while(time.time() - start < timelimit):
    
    # download = st.download()
    # upload = st.upload()

    # servernames = []
    # st.get_servers(servernames)
    # best = st.get_best_server()
    # ping = st.results.ping()

    # print(f"{download}, {upload}, ")

    print(st.results.csv())

    time.sleep(downtime)