#pip install fbprophet yfinance plotly 

import streamlit as st 
from datetime import date 

import yfinance as yf 
from fbprophet import Prophet 
from fbprophet import plot_plotly 
from plotly import graph_objs as go 

START = '2015-01-01'
TODAY = date.today().strftime('%Y-%m-%d')

st.title('STOCKS FORECAST APP')

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
select_stock = st.selectbox('Select Stock for prediction',stocks)
