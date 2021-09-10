import streamlit  as st  
import pandas as pd
import yfinance as yf

st.write('''simple stock price chart app''')

tickerSymbol = 'ETH'  

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='max', start='2019-12-12' , end='2021-6-6')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)