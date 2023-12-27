import speedtest
import datetime
from os.path import exists

existed = exists("output.csv")

with open("output.csv", "a") as f:
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

print("done")