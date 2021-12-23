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
	global rsi_pnl
	rsi=pd.read_csv('rsi.csv')
	# rsi=pd.read_csv('E:/startegy/logs/mo_ch/stream/rsi.csv')
	rsi=rsi.dropna()
	rsi=rsi.rename(columns={'Unnamed: 5':'Date','Unnamed: 10':'Strike','Unnamed: 8':'quantity','Unnamed: 6':'pnl'})
	rsi=rsi[['Date','Strike','quantity','pnl']]
	rsi=rsi.reset_index()
	rsi=rsi.drop('index',axis=1)
	st.subheader('2nd Strategy - Scalping')
	st.write(rsi)
	for i in rsi['pnl']:
		i=int(i)
		rsi_pnl+=i
	st.text(f'Total pnl in 2nd startegy is {rsi_pnl}')
	return rsi_pnl

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
	update=f"Total pnl of all strategies = {mother_child()}"


if __name__=="__main__":
	bnf300_pnl=0
	mother_child_pnl=0
	rsi_pnl=0
	# st.line_chart(rsi_data.rename(columns={'Date':'index'}).set_index('index'))
	bnf300()
	st.header(f"Total pnl of all strategies = {mother_child_pnl+rsi_pnl+bnf300_pnl}")


