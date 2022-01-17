import datetime
from datetime import date
import pandas as pd 
from datetime import timedelta
from datetime import datetime as dt
import time

import streamlit as st

def mother_child():
	global mother_child_pnl
	mother_child=pd.read_csv('moch.csv')
	# mother_child=pd.read_csv('E:/startegy/logs/mo_ch/stream/moch.csv')
	mother_child=mother_child.dropna()
	mother_child=mother_child.rename(columns={'Unnamed: 6':'Date','Unnamed: 12':'Strike','Unnamed: 10':'quantity','Unnamed: 8':'pnl'})
	mother_child=mother_child[['Date','Strike','quantity','pnl']]
	mother_child=mother_child.reset_index()
	mother_child=mother_child.drop('index',axis=1)
	for i in mother_child['pnl']:
		i=float(i)
		mother_child_pnl+=i
	st.subheader('1st strategy')
	# mother_child['Monthly']=int(float(mother_child_pnl))
	st.write(mother_child)
	st.text(f"Total pnl in 1st strategy is {mother_child_pnl}")
	return round(mother_child_pnl,2)

def rsi():
	global sbin_pnl
	sbin=pd.read_csv('sbin.csv')
	# sbin=pd.read_csv('E:/startegy/logs/mo_ch/stream/sbin.csv')
	sbin=sbin.dropna()
	sbin=sbin.rename(columns={'Unnamed: 5':'Date','Unnamed: 10':'Stock','Unnamed: 8':'quantity','Unnamed: 6':'pnl'})
	sbin=sbin[['Date','pnl']]
	sbin=sbin.reset_index()
	sbin=sbin.drop('index',axis=1)
	st.subheader('Equity - Deployed')
	st.text("Instrument is NSE Cash")
	st.write(sbin)
	for i in sbin['pnl']:
		i=float(i)
		sbin_pnl+=i
	st.text(f'Total pnl in Equity is {sbin_pnl}')
	return round(sbin_pnl,2)

def bnf300():
	global bnf300_pnl
	bnf300=pd.read_csv('bnf300.csv')
	# bnf300=pd.read_csv('E:/startegy/logs/mo_ch/stream/bnf300.csv')
	bnf300=bnf300.dropna()
	bnf300=bnf300.rename(columns={'Unnamed: 6':'Date','Unnamed: 11':'Strike','Unnamed: 9':'quantity','Unnamed: 7':'pnl'})
	bnf300=bnf300[['Date','Strike','quantity','pnl']]
	bnf300=bnf300.reset_index()
	bnf300=bnf300.drop('index',axis=1)
	st.subheader('2nd Strategy - Testing')
	st.write(bnf300)
	bnf300_pnl=0
	for i in bnf300['pnl']:
		i=float(i)
		bnf300_pnl+=i
	bnf300_data=bnf300[['Date','pnl']]
	st.text(f'Total pnl in 2nd startegy is {bnf300_pnl}')
	return round(bnf300_pnl,2)

def straddle():
	# mother_child()
	rsi()
	bnf300()
	global straddle_pnl
	straddle=pd.read_csv('straddle.csv')
	straddle=straddle.dropna()
	straddle=straddle.rename(columns={'Unnamed: 10':'Date',"Unnamed: 14":'Strikes(PE,CE)','Unnamed: 11':'PE pnl','Unnamed: 8':'CE pnl','Unnamed: 15':'pnl'})
	straddle=straddle[['Date','Strikes(PE,CE)','PE pnl','CE pnl','pnl']]
	straddle=straddle.reset_index()
	straddle=straddle.drop('index',axis=1)
	straddle.drop(index=straddle.index[0],axis=0,inplace=True)
	st.subheader('Straddle - Deployed')
	st.text("BANKNIFTY")
	st.write(straddle)
	for i in straddle['pnl']:
		i=float(i)
		straddle_pnl+=i
	st.text(f'Total pnl in Straddle is {straddle_pnl}')
	return round(straddle_pnl,2)
def total_pnl():
	bnf300()
	update=f"Total pnl of all strategies = {mother_child()}"


if __name__=="__main__":
	bnf300_pnl=0
	mother_child_pnl=0
	sbin_pnl=0
	straddle_pnl=0
	# st.line_chart(rsi_data.rename(columns={'Date':'index'}).set_index('index'))
	count = 0
	st.text("Hi all ,below are my startegies running.")
	st.text("I Have considered charges of 50rs per trade in options,500rs in Futures and \n50rs in Equity.")
	st.text("Pnl is after all deductions.Scroll to the bottom for total pnl of all strategies.")
	straddle()
	st.header(f"Total pnl of all strategies = {mother_child_pnl+sbin_pnl+straddle_pnl}")
	st.write("Contact me @ [Twitter](https://twitter.com/yashwanthb_s)")
	increment = st.button('Refresh')
	if increment:
	    count += 1


