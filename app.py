import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Dashboard Pro", layout="wide")

st.title("📊 Interactive Financial Decision Dashboard")

# Sidebar controls
st.sidebar.header("User Controls")

stock = st.sidebar.selectbox(
    "Select Stock",
    ["TSLA", "AAPL", "AMZN", "GOOGL", "MSFT"]
)

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Load data
raw = yf.download(stock, start=start_date, end=end_date)

if raw.empty:
    st.error("No data available. Try different dates.")
    st.stop()

if raw.columns.nlevels > 1:
    raw.columns = [col[0] for col in raw.columns]

data = raw[['Close']].copy()

# KPIs
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Latest Price", f"${data['Close'].iloc[-1].item():.2f}")
col2.metric("Average Price", f"${data['Close'].mean().item():.2f}")
col3.metric("Volatility", f"{data['Returns'].std().item():.2f}")

# Indicators
data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()
data['Returns'] = data['Close'].pct_change()

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Price Trend")
    st.line_chart(data['Close'])

with col2:
    st.subheader("📊 Moving Averages")
    st.line_chart(data[['Close', 'MA50', 'MA200']])

st.subheader("📉 Daily Returns")
st.line_chart(data['Returns'])

# Risk Analysis
st.subheader("⚠️ Risk Analysis")

vol = data['Returns'].std()

if vol > 0.03:
    risk = "High"
elif vol > 0.015:
    risk = "Medium"
else:
    risk = "Low"

st.write(f"Risk Level: **{risk}**")

# Investment Signal
st.subheader("📊 Investment Signal")

if data['MA50'].iloc[-1] > data['MA200'].iloc[-1]:
    st.success("📈 Bullish Trend (Buy Signal)")
else:
    st.warning("📉 Bearish Trend (Sell Signal)")

# Raw data
if st.checkbox("Show Raw Data"):
    st.write(data.tail())