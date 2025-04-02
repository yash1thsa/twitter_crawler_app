import tweepy
from app import BEARER_TOKEN

# Authenticate with Tweepy
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_search_tweets(query, max_results):
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results)
        tweets = [tweet.text for tweet in response.data]
        return {"tweets": tweets}
    except Exception as e:
        return {"error": str(e)}



