📈 Stock Price Forecasting Web App

Predict future stock prices using Machine Learning with a modern interactive interface.

🔗 Live Demo:
https://stock-forecasting-webapp-z5odae5cyymerm4e895pch.streamlit.app/

💻 GitHub Repository:
https://github.com/Noorahmedks-2103/Stock-Forecasting-WebApp
🚀 Features

Fetches real 5-year stock market price data using yfinance

ML model predicts 30-day future stock price trend

Interactive UI with stock selection dropdown

Graph visualization comparing history vs forecast

Deployed on Streamlit Cloud

Custom dark theme UI with CSS
🧠 Tech Stack
Tool / Library	Purpose
Python	Core programming
Pandas / NumPy	Data manipulation
yFinance	Financial data API
Scikit-Learn	ML regression model
Matplotlib	Visualization
Streamlit	Web app development
GitHub + Streamlit Cloud	Deployment
📷 App Preview
https://raw.githubusercontent.com/Noorahmedks-2103/Stock-Forecasting-WebApp/main/assets/Screenshot.png
🧾 Project Architecture
Stock-Forecasting-WebApp/
├── src/
│   └── model.py
├── assets/
│   └── style.css
├── model.pkl
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
⚙️ Run the Project Locally
git clone https://github.com/Noorahmedks-2103/Stock-Forecasting-WebApp.git
cd Stock-Forecasting-WebApp
pip install -r requirements.txt
python src/model.py          # Train & generate model.pkl
streamlit run app.py         # Run the app
📊 Output Example

Historical closing prices shown on chart

Predicted values visualized clearly against actual

Supports multiple stocks: AAPL, TSLA, GOOGL, MSFT, AMZN

🔥 Future Improvements

Add Prophet / LSTM deep learning model

Add user-typed stock search instead of dropdown

Compare multiple models

Add exportable downloadable report

👨‍💻 Author

K S Noor Ahamad
Final-Year CSE Student | ML & Data Science
📍 Tirupati, Andhra Pradesh
📧 nkurnipalli34@gmail.com

📝 License

MIT License — see LICENSE for details.

⭐ Support

If you like this project, please ⭐ star the repository 🙌

