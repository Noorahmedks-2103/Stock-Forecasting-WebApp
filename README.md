📈 Stock Price Forecasting Web Application

A Machine Learning powered web application for forecasting stock market trends using real historical data, regression modeling, and live visualization through an interactive Streamlit interface.

🌐 Live Demo

🔗 https://stock-forecasting-webapp-z5odae5cyymerm4e895pch.streamlit.app

📦 GitHub Repository

🔗 https://github.com/Noorahmedks-2103/Stock-Forecasting-WebApp
🚀 Project Overview

This project predicts future stock prices using real-time financial market data collected via the yFinance API.
The application trains a regression model on 5 years of historical closing prices, forecasts the next 30 days, and visualizes results interactively with charts.

Designed with Streamlit UI, styled using custom CSS, and deployed on Streamlit Cloud.

🧠 Key Features

📉 Real historical stock price analysis

🔮 30-day future price forecasting using ML

💹 Visual dashboard comparing historical vs predicted values

🔽 Dropdown to choose from multiple stocks (AAPL, TSLA, MSFT, AMZN, GOOGL)

🌑 Dark-themed modern interface

☁ Fully deployed and accessible online

🛠 Tech Stack
Technology	Purpose
Python	Backend language
Pandas, NumPy	Data handling
yFinance	Stock data extraction
Scikit-Learn	ML model (Linear Regression)
Matplotlib	Data visualization
Streamlit	Web interface
GitHub + Streamlit Cloud	Deployment & CI/CD
📷 Application Preview
https://raw.githubusercontent.com/Noorahmedks-2103/Stock-Forecasting-WebApp/main/assets/Screenshot.png
📁 Project Structure
Stock-Forecasting-WebApp/
│
├── src/
│   └── model.py
│
├── assets/
│   └── style.css
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── LICENSE
⚙️ How to Run Locally
git clone https://github.com/Noorahmedks-2103/Stock-Forecasting-WebApp.git
cd Stock-Forecasting-WebApp
pip install -r requirements.txt
python src/model.py          # trains model and creates model.pkl
streamlit run app.py         # launches web app
📊 Results & Output

✔ Forecast graph clearly shows future trend continuation

✔ Interactive comparison between history & forecast

✔ Smooth real-time UI experience🔮 Future Enhancements

🧠 LSTM / Neural Network forecasting

🔎 User-typed stock search

🪙 Cryptocurrency or Forex support

📑 Downloadable analysis report

📊 Multiple stock comparison chart
👨‍💻 Author

K S NOOR AHAMAD
Final-Year Computer Science Student
Machine Learning & Data Science Enthusiast
📍 Tirupati, Andhra Pradesh
📧 nkurnipalli34@gmail.com
⭐ Support

If you find this useful, please ⭐ star the repository and share feedback







