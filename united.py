
import requests
import os

def get_united_tweet():
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return "⚠️ NEWS_API_KEY not found in environment variables."

    url = (
        "https://newsapi.org/v2/everything?"
        "q=manchester united&"
        "sortBy=publishedAt&"
        "language=en&"
        "pageSize=1&"
        f"apiKey={api_key}"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok" or not data.get("articles"):
            return "❌ Couldn't fetch United news at the moment."

        article = data["articles"][0]
        title = article.get("title", "No title available")
        url = article.get("url", "")

        tweet = f"🚨 {title}\n🔗 Read more: {url}\n#MUFC #ManUtd"
        return tweet

    except Exception as e:
        return f"❌ Error fetching United news: {str(e)}"
