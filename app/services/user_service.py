import json

from app.config import BEARER_TOKEN
import tweepy
import json

# Authenticate with Tweepy
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def to_dict_safe(obj):
    return {
        key: getattr(obj, key)
        for key in dir(obj)
        if not key.startswith("_") and not callable(getattr(obj, key))
    }

def get_user_by_username(username: str):
    try:
        response = client.get_user(username=username,  user_fields=[
        "created_at", "description", "entities", "id", "location", "name",
        "pinned_tweet_id", "profile_image_url", "protected", "public_metrics",
        "url", "username", "verified", "withheld"
    ])
        user = response.data
        return json.dumps(to_dict_safe(user), indent=2, default=str)
    except Exception as e:
        return {"error": f"Failed to fetch user: {str(e)}"}