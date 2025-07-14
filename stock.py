import yfinance as yf
import random
import requests
from bs4 import BeautifulSoup
from datetime import date

def get_most_active_tickers(limit=5):
    url = "https://finance.yahoo.com/most-active"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        symbols = soup.select("td[aria-label='Symbol']")
        tickers = [s.text.strip() for s in symbols[:limit]]
        return tickers
    except Exception:
        return ["AAPL", "MSFT", "TSLA", "GOOGL"]  # fallback

def get_stock_tweet():
    tickers = get_most_active_tickers()
    ticker = random.choice(tickers)
    stock = yf.Ticker(ticker)
    hist = stock.history(period="2d")
    if len(hist) < 2:
        return f"⚠️ Not enough data for ${ticker.upper()}"

    close_price = hist['Close'].iloc[-1]
    prev_price = hist['Close'].iloc[-2]
    pct_change = ((close_price - prev_price) / prev_price) * 100

    direction = "🔺" if pct_change > 0 else "🔻"

    return (
        f"{direction} ${ticker.upper()} closed at ${close_price:.2f} "
        f"({pct_change:+.2f}%) on {date.today():%b %d, %Y}. "
    
    )

