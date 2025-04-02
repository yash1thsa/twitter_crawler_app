import requests
from app.config import BEARER_TOKEN

def get_user_by_username(username: str):
    url = (f"https://api.twitter.com/2/users/by/username/{username}?user.fields=profile_image_url,"
           f"location,public_metrics")
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}