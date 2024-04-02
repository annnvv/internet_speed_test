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


#TODO: use the year and month input to limit this query (will also need to update the endpoint to accept those two parameters)
url = 'http://127.0.0.1:8000'
avg_speed = requests.get(url = f'{url}/get_avg_download_speed').json()
st.write(f"Average Internet Download Speed: {avg_speed['average_download_speed']:.2f} Mbps")


middle_container = st.container()
midcol1, midcol2 = st.columns(2)

midcol1.header("Download - Timeseries")
fig, ax = plt.subplots()
ax.plot(df['timestamp'], df['download_speed_Mb'], marker='o', linestyle='-')
ax.set_title('Download Speed over Time')
ax.set_xlabel('Timestamp')
plt.xticks(rotation=45)
ax.set_ylabel('Download Speed (Mbps)')
ax.axhline(y=300, color='r', linestyle='--')
ax.grid(True)
midcol1.pyplot(fig)


midcol2.header("Upload - Timeseries")
fig2, ax2 = plt.subplots()
ax2.plot(df['timestamp'], df['upload_speed_Mb'], marker='o', linestyle='-')
ax2.set_title('Upload Speed over Time')
ax2.set_xlabel('Timestamp')
plt.xticks(rotation=45)
ax2.set_ylabel('Upload Speed (Mbps)')
ax2.axhline(y=20, color='r', linestyle='--')
ax2.grid(True)
midcol2.pyplot(fig2) 


bottom_container = st.container()
avg_speeds_per_day = df.groupby('date')[['download_speed_Mb', 'upload_speed_Mb']].mean().reset_index()
botcol1, botcol2 = st.columns(2)

botcol1.header("Download - Average by day")
fig3, ax3 = plt.subplots()
ax3.bar(avg_speeds_per_day['date'], avg_speeds_per_day['download_speed_Mb'])
ax3.set_title('Average Download Speed per Day')
ax3.set_xlabel('Date')
ax3.set_ylabel('Average Download Speed (Mbps)')
plt.xticks(rotation=45)
ax3.grid(axis='y')
ax3.axhline(y=300, color='r', linestyle='--')
botcol1.pyplot(fig3)

botcol2.header("Upload - Average by day")
fig4, ax4 = plt.subplots()
ax4.bar(avg_speeds_per_day['date'], avg_speeds_per_day['upload_speed_Mb'])
ax4.set_title('Average Upload Speed per Day')
ax4.set_xlabel('Date')
ax4.set_ylabel('Average Upload Speed (Mbps)')
plt.xticks(rotation=45)
ax4.grid(axis='y')
ax4.axhline(y=20, color='r', linestyle='--')
botcol2.pyplot(fig4)