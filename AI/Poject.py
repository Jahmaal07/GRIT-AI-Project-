# example/st_app.py

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import numpy as np

url = "https://docs.google.com/spreadsheets/d/1LMzSaBylCm8f0iO_h_Pv3_0e-iDQIbYJh1UfwDmD_6A/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

data1= pd.DataFrame(conn.read(spreadsheet=url,worksheet="1567253166",ttl=5,), range(20))
data2 = conn.read(spreadsheet=url,worksheet="0",ttl=5,)
st.dataframe(data2)
st.line_chart(data1,)

