import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pickle

st.markdown("<h1 class='title'>📈 Stock Price Forecasting Web App</h1>", unsafe_allow_html=True)
st.write("Predict future stock prices using Machine Learning")

stocks = ["AAPL", "GOOGL", "TSLA", "MSFT", "AMZN"]
option = st.selectbox("Choose Stock to Predict", stocks)

model = pickle.load(open("model.pkl", "rb"))

if st.button("Predict Future Prices"):
    try:
    data = yf.download(option, period="5y", interval="1d")
except:
    st.error("API limit reached. Please try again after 1 minute.")

    data["Day"] = range(len(data))
    future_days = 30
    future = pd.DataFrame({"Day": range(len(data), len(data)+future_days)})
    prediction = model.predict(future)

    st.subheader(f"Future 30-Day Forecast for {option}")

    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(data["Close"], label="History")
    ax.plot(range(len(data), len(data)+future_days), prediction, label="Forecast")
    ax.legend()
    st.pyplot(fig)

with open("assets/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
