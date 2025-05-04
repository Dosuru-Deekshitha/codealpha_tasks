# Try in a separate test.py file:
import yfinance as yf
print(yf.Ticker("AAPL").history(period="1d")['Close'])
