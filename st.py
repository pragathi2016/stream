import datetime
from datetime import date
import pandas as pd 
from datetime import timedelta
from datetime import datetime as dt
import time

import streamlit as st

a=pd.read_csv('mo_ch1.csv')
a=pd.DataFrame(a)
a=a.dropna()
print(a)
a=a.rename(columns={'Unnamed: 11':'Strike','Unnamed: 7':'pnl'})
a=a[['Strike','pnl']]
print(a)

st.write(a)
tot=0
for i in a['pnl']:
    i=int(i)
    tot+=i

st.write(f'total pnl is {tot}')
# import numpy as np

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# # Streamlit widgets automatically run the script from top to bottom. Since
# # this button is not connected to any other logic, it just causes a plain
# # rerun.
# st.button("Re-run")