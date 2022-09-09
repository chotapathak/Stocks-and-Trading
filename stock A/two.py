
import streamlit  as st  
import pandas as pd
import yfinance as yf
from datetime import date,time
import matplotlib.pyplot as plt

st.write('''simple stock price chart app''')

tickerSymbol = 'BTC'  

tickerData = yf.Ticker(tickerSymbol)
tickerData = yf.download('BTC','2016-12-12','2022-03-01')
print(tickerData, ' <= data')

tickerDf = tickerData   
st.plotly_chart
# st.line_chart(tickerDf.Close)
# st.line_chart(tickerDf.Volume)
# st.experimental_show(tickerDf)
plt.show()
print('hello')

# # creating a simple chart
close = tickerDf.plot(y='Close', title='TSLA stock')
plt.show()