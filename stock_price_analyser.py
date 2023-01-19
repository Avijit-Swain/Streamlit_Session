import pandas as pd
import yfinance as yf
import streamlit as st
import datetime

st.write(
    """
    # Stock Price Analyser
    Shown are the stock prices of Apple.
    """
)

ticker_symbol = st.text_input('Enter Stock Symbol', 'AAPL')

col1, col2= st.columns(2)

with col1:
    start_date = st.date_input("Input Start Date",
        datetime.date(2018, 7, 6))

with col2:
    end_date = st.date_input("Input End Date",
        datetime.date(2020, 7, 6))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d",start=start_date,end=end_date)
st.write(f""" 
    ### {ticker_symbol}'s Prices
    """
)
st.dataframe(ticker_df)

st.write(
    """
    ## Daily Closing Price Chart
    """
)
st.line_chart(ticker_df.Close)

st.write(
    """
    ## Volume of Shares traded each day
    """
)
st.line_chart(ticker_df.Volume)







