import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_united_tweet() -> str:
    """
    Fetches the latest Manchester United news.
    """
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return "⚠️ NEWS_API_KEY not found in environment variables."

    url = (
        "https://newsapi.org/v2/everything?"
        "q=\"manchester united\"&"
        "sortBy=publishedAt&"
        "language=en&"
        "pageSize=1&"
        f"apiKey={api_key}"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("status") != "ok" or not data.get("articles"):
            return "❌ Couldn't fetch United news at the moment."

        article = data["articles"][0]
        title = article.get("title", "No title available")
        article_url = article.get("url", "")

        tweet = f"🚨 {title}\n🔗 Read more: {article_url}\n#MUFC #ManUtd"
        return tweet

    except Exception as e:
        return f"❌ Error fetching United news: {str(e)}"
