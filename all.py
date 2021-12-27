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
		i=int(i)
		mother_child_pnl+=i
	st.subheader('1st strategy')
	st.write(mother_child)
	st.text(f"Total pnl in 1st strategy is {mother_child_pnl}")
	return mother_child_pnl

def rsi():
	global sbin_pnl
	sbin=pd.read_csv('sbin.csv')
	# sbin=pd.read_csv('E:/startegy/logs/mo_ch/stream/sbin.csv')
	sbin=sbin.dropna()
	sbin=sbin.rename(columns={'Unnamed: 5':'Date','Unnamed: 10':'Stock','Unnamed: 8':'quantity','Unnamed: 6':'pnl'})
	sbin=sbin[['Date','Stock','quantity','pnl']]
	sbin=sbin.reset_index()
	sbin=sbin.drop('index',axis=1)
	st.subheader('2nd Strategy')
	st.write(sbin)
	for i in sbin['pnl']:
		i=int(i)
		sbin_pnl+=i
	st.text(f'Total pnl in 2nd startegy is {sbin_pnl}')
	return sbin_pnl

def bnf300():
	mother_child()
	rsi()
	global bnf300_pnl
	bnf300=pd.read_csv('bnf300.csv')
	# bnf300=pd.read_csv('E:/startegy/logs/mo_ch/stream/bnf300.csv')
	bnf300=bnf300.dropna()
	bnf300=bnf300.rename(columns={'Unnamed: 6':'Date','Unnamed: 11':'Strike','Unnamed: 9':'quantity','Unnamed: 7':'pnl'})
	bnf300=bnf300[['Date','Strike','quantity','pnl']]
	bnf300=bnf300.reset_index()
	bnf300=bnf300.drop('index',axis=1)
	st.subheader('3rd Strategy')
	st.write(bnf300)
	bnf300_pnl=0
	for i in bnf300['pnl']:
		i=int(i)
		bnf300_pnl+=i
	bnf300_data=bnf300[['Date','pnl']]
	st.text(f'Total pnl in 3rd startegy is {bnf300_pnl}')
	return bnf300_pnl


def total_pnl():
	bnf300()
	update=f"Total pnl of all strategies = {mother_child()}"


if __name__=="__main__":
	bnf300_pnl=0
	mother_child_pnl=0
	sbin_pnl=0
	# st.line_chart(rsi_data.rename(columns={'Date':'index'}).set_index('index'))
	count = 0
	bnf300()
	st.header(f"Total pnl of all strategies = {mother_child_pnl+sbin_pnl+bnf300_pnl}")
	increment = st.button('Refresh')
	if increment:
	    count += 1

