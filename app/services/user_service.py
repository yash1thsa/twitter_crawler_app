from app import BEARER_TOKEN
import tweepy

# Authenticate with Tweepy
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# def get_user_by_username(username: str):
#     url = (f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url,"
#            f"location,public_metrics")
#     headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
#     response = requests.get(url, headers=headers)
#
#     if response.status_code == 200:
#         return response.json()
#     else:
#         return {"error": response.json()}


def get_user_by_username(username: str):
    try:
        user = client.get_user(screen_name=username)
        # user_data = {
        #     "username": user.screen_name,
        #     "name": user.name,
        #     "location": user.location,
        #     "followers_count": user.followers_count,
        #     "profile_image_url": user.profile_image_url_https
        # }
        return user.json()
    except tweepy.TweepError as e:
        return {"error": f"Failed to fetch user: {str(e)}"}