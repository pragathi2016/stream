import datetime
from datetime import date
import pandas as pd 
from datetime import timedelta
from datetime import datetime as dt
import time

import streamlit as st

a=pd.read_csv('E:\startegy\logs\mo_ch\stream/mo_ch1.csv')
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
