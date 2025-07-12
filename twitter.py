import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

def tweet(message):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("CONSUMER_KEY"),
        os.getenv("CONSUMER_SECRET"),
        os.getenv("ACCESS_TOKEN"),
        os.getenv("ACCESS_TOKEN_SECRET"),
    )
    api = tweepy.API(auth)
    api.update_status(message)
