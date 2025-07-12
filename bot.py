from stock import get_stock_tweet
from united import get_united_tweet
from twitter import tweet
import random

def main():
    tickers = ["AAPL", "GOOGL", "TSLA", "MSFT"]
    ticker = random.choice(tickers)

    tweet(get_stock_tweet(ticker))
    tweet(get_united_tweet())

if __name__ == "__main__":
    main()
