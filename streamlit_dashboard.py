import datetime
import streamlit  as st
import requests
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Internet Speed Test Dashboard")


top_container = st.container()
topcol1, topcol2 = st.columns(2)
current_year = datetime.date.today().year                         
year = topcol1.selectbox('Year', range(2024, current_year+1))
month = topcol2.selectbox('Month', range(1, 13))

##this is dummy data to test the dashboard (actuall data will come from the API calls)
from pandas import date_range, DataFrame
import numpy as np
timestamp = date_range('20240101 00:00','20240130 23:59',periods= 720)
download_speed_Mb = np.random.normal(0, 300, size = 720)
upload_speed_Mb = np.random.normal(0, 20, size = 720)
df = DataFrame(dict(timestamp = timestamp, download_speed_Mb = download_speed_Mb, upload_speed_Mb = upload_speed_Mb)).reset_index(drop = True)
df['date'] = df['timestamp'].dt.date
st.set_option('deprecation.showPyplotGlobalUse', False)


url = 'http://127.0.0.1:8000'
avg_speed = requests.get(url = f'{url}/get_avg_download_speed').json()
st.write(f"Average Internet Download Speed: {avg_speed['average_download_speed']:.2f} Mbps")


middle_container = st.container()
midcol1, midcol2 = st.columns(2)

midcol1.header("Download - Timeseries")
plt.plot(df['timestamp'], df['download_speed_Mb'], marker='o', linestyle='-')
plt.title('Download Speed over Time')
plt.xlabel('Timestamp')
plt.xticks(rotation=45)
plt.ylabel('Download Speed (Mbps)')
plt.axhline(y=300, color='r', linestyle='--')
plt.grid(True)
plt.show()
midcol1.pyplot() ##need argument here


midcol2.header("Upload - Timeseries")
plt.plot(df['timestamp'], df['upload_speed_Mb'], marker='o', linestyle='-')
plt.title('Upload Speed over Time')
plt.xlabel('Timestamp')
plt.xticks(rotation=45)
plt.ylabel('Upload Speed (Mbps)')
plt.grid(True)
plt.show()
midcol2.pyplot() ##need argument here

bottom_container = st.container()
avg_speeds_per_day = df.groupby('date')[['download_speed_Mb', 'upload_speed_Mb']].mean().reset_index()
botcol1, botcol2 = st.columns(2)

botcol1.header("Download - Average by day")
plt.bar(avg_speeds_per_day['date'], avg_speeds_per_day['download_speed_Mb'])
plt.title('Average Download Speed per Day')
plt.xlabel('Date')
plt.ylabel('Average Download Speed (Mbps)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.axhline(y=300, color='r', linestyle='--')
plt.show()
botcol1.pyplot()

botcol2.header("Upload - Average by day")
plt.bar(avg_speeds_per_day['date'], avg_speeds_per_day['upload_speed_Mb'])
plt.title('Average Upload Speed per Day')
plt.xlabel('Date')
plt.ylabel('Average Upload Speed (Mbps)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
botcol2.pyplot()