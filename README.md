# 📈 Stock Price Forecasting Web App

Predict future stock prices using machine learning in a fully interactive web app.

[🌐 Live Demo](https://stock-forecasting-webapp-z5odae5cyymerm4e895pch.streamlit.app/) | [💻 Repository](https://github.com/Noorahmedks-2103/Stock-Forecasting-WebApp)

---

## 🔧 Features
- Fetches 5-year historical data from stock market using :contentReference[oaicite:1]{index=1}  
- Trains a regression model to forecast future 30-day closing price  
- Interactive web interface built with :contentReference[oaicite:2]{index=2}  
- Visualization of history vs. forecast to compare trends  

---

## 🧰 Tech Stack & Libraries

| Library / Tool | Purpose |
|----------------|---------|
| Python 3.12 | Backend language |
| pandas, numpy | Data handling & manipulation |
| scikit-learn | Training regression model |
| yfinance | Fetching real-world stock data |
| matplotlib | Plotting charts & graphs |
| Streamlit | Web UI framework |
| GitHub | Version control & code repository |
| Streamlit Cloud | Deployment & hosting |

---

## 🧠 How It Works
1. The app fetches historical data (5 years) of the selected stock.  
2. It converts dates into numerical feature (“Day index”) and trains a Linear Regression model on closing prices.  
3. On user request, the app predicts closing prices for the next 30 days.  
4. Results are shown via interactive chart comparing history vs. forecast.

---

## 🚀 Quick Start (Run Locally)

```bash
git clone https://github.com/Noorahmedks-2103/Stock-Forecasting-WebApp.git
cd Stock-Forecasting-WebApp
pip install -r requirements.txt
python src/model.py          # Train the model (generates model.pkl)
streamlit run app.py         # Start the web app
📦 Project Structure
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
📊 Example Output

Use the live demo link above to view interactive charts.
(See screenshot preview below)

📝 License

MIT License — see LICENSE
 for details.

👨‍💻 Author

K S Noor Ahamad — Final-Year CSE Student
📧 nkurnipalli34@gmail.com

📍 Tirupati, Andhra Pradesh, India
