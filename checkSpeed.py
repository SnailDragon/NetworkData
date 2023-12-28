import speedtest
import datetime
from os.path import exists
import sys

filePath = "output.csv"

if(len(sys.argv) == 2):
    filePath = sys.argv[1]

existed = exists(filePath)

with open(filePath, "a") as f:
    if(not existed):
        f.write("Date, Time, Server, Download (Mbps), Upload (Mbps), Ping (ms)\n")

    st = speedtest.Speedtest();

    date = datetime.datetime.now().strftime("%Y/%m/%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping
    server = "\"" + st.results.server["name"] + "\""
            
    f.write(f"{date}, {time}, {server}, {download}, {upload}, {ping}\n")

print("done " + datetime.datetime.now().strftime("%H:%M:%S") + "\n")
