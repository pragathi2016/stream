import datetime
from datetime import date
import pandas as pd 
from datetime import timedelta
from datetime import datetime as dt
import time

import streamlit as st


def data():
	newfile="./cars.xlsx"
	data=pd.read_excel(newfile)
	data=data[::-1]
	st.subheader('Cars Report')
	# st.text("Instrument is NSE Cash")
	st.write(data)

if __name__ == '__main__':
	count = 0
	st.text("Day in/out")
	data()
	st.write("Contact me @ [Instagram](https://www.instagram.com/bsyashwanth_/)")
	increment = st.button('Refresh')
	if increment:
	    count += 1