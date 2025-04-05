import tweepy
from config import BEARER_TOKEN


def create_tweepy_client():
    """
    Dependency function to create the Tweepy client.
    Can be reused across multiple route handlers.
    """
    return tweepy.Client(bearer_token=BEARER_TOKEN)