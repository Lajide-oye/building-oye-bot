import yfinance as yf
from datetime import date

def get_stock_tweet(ticker="AAPL"):
    stock = yf.Ticker(ticker)
    today_data = stock.history(period="1d")

    close_price = today_data["Close"].iloc[-1]
    open_price = today_data["Open"].iloc[-1]
    change = close_price - open_price
    direction = "🔺" if change >= 0 else "🔻"
    pct_change = (change / open_price) * 100

    return (
        f"{direction} ${ticker.upper()} closed at ${close_price:.2f} "
        f"({pct_change:+.2f}%) on {date.today():%b %d, %Y}. "
        "#StockMarket #Trading #Finance"
    )
