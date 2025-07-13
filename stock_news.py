import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_stock_news_tweet(ticker: str) -> str:
    """
    Fetches the latest relevant business news for the stock market.
    """
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return "⚠️ NEWS_API_KEY not found in environment variables."

    url = (
        "https://newsapi.org/v2/top-headlines?"
        "category=business&"
        "language=en&"
        "pageSize=1&"
        f"apiKey={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") != "ok" or not data.get("articles"):
            return "❌ Couldn't fetch stock market news at the moment."

        article = data["articles"][0]
        title = article.get("title", "No title available")
        article_url = article.get("url", "")

        tweet = (
            f"📈 Stock Market Update:\n{title}\n"
            f"🔗 Read more: {article_url}\n#StockMarket #Investing"
        )
        return tweet

    except Exception as e:
        return f"❌ Error fetching stock market news: {str(e)}"
