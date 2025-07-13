"""Bot for tweeting stock and united news."""

import random
from typing import List

from stock_news import get_stock_news_tweet
from united import get_united_tweet
from twitter import tweet

def get_stock_tweet(ticker: str) -> str:
    """
    Try to get a real news tweet, fallback to generic if not available.

    Args:
        ticker (str): Stock ticker symbol.

    Returns:
        str: Tweet text.
    """
    news_tweet = get_stock_news_tweet(ticker)
    if news_tweet:
        return news_tweet
    return f"{ticker} stock is up today!"

def main() -> None:
    """
    Main function to tweet a random stock update and a united update.
    """
    tickers: List[str] = ["AAPL", "GOOGL", "TSLA", "MSFT"]
    if not tickers:
        print("No tickers available.")
        return
    ticker: str = random.choice(tickers)
    try:
        stock_tweet: str = get_stock_tweet(ticker)
        united_tweet: str = get_united_tweet()
        tweet(stock_tweet)
        tweet(united_tweet)
    except Exception as e:
        print(f"Error tweeting: {e}")

if __name__ == "__main__":
    main()