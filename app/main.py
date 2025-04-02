from fastapi import FastAPI
import tweepy
import os
import requests
from app.config import BEARER_TOKEN

app = FastAPI()


# Authenticate with Tweepy
client = tweepy.Client(bearer_token=BEARER_TOKEN)

@app.get("/")
def home():
    return {"message": "Twitter Data Crawler is running!"}

@app.get("/search")
def search_tweets(query: str, max_results: int = 10):
    """
    Search recent tweets with a given query.
    """
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results)
        tweets = [tweet.text for tweet in response.data]
        return {"tweets": tweets}
    except Exception as e:
        return {"error": str(e)}


def get_user_by_username(username: str):
    url = f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url,location,public_metrics"
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}


@app.get("/user/{username}")
def fetch_user(username: str):
    return get_user_by_username(username)