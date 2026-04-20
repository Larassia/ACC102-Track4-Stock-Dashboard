# 📊 Interactive Financial Decision Dashboard

## 🔗 Live App
👉 https://stock-dashboard-dfafxamwjh7imqz2g7ho6t.streamlit.app/

---

## 1. Problem & Target User

This project aims to help beginner investors and finance students understand stock market trends, volatility, and basic investment signals using an interactive dashboard.

The tool is designed for:
- Beginner investors
- Finance and accounting students

---

## 2. Dataset

- Source: Yahoo Finance  
- Accessed: April 2026  
- Data collected using the Python `yfinance` library  
- Includes daily stock prices (Close price) for selected companies

---

## 3. Methods (Python Workflow)

The project follows a structured data analysis process:

- Data collection using `yfinance`
- Data cleaning (handling missing values)
- Feature engineering:
  - 50-day Moving Average (MA50)
  - 200-day Moving Average (MA200)
  - Daily Returns
- Descriptive statistics:
  - Average price
  - Volatility (standard deviation)
- Visualization using Streamlit charts
- Simple investment signal based on moving average crossover

---

## 4. Key Features

- 📈 Stock price visualization  
- 📊 Moving averages (MA50, MA200)  
- 📉 Daily returns analysis  
- ⚠️ Risk classification (Low / Medium / High)  
- 📊 Investment signal (Bullish / Bearish)  
- 🔄 Interactive stock and date selection  

---

## 5. Key Findings

- Technology stocks such as Tesla show high volatility, indicating higher risk.
- Moving averages help identify long-term trends.
- Stock prices fluctuate significantly over time.
- Simple indicators can support basic investment decisions.

---

## 6. How to Run the Project

### Install dependencies:

pip install -r requirements.txt

### Run app
py -m streamlit run app.py

## 7. Project Structure
tesla-stock-dashboard/
│
├── app.py
├── notebook.ipynb
├── README.md
├── requirements.txt 
