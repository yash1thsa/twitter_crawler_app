from fastapi import FastAPI, Depends
from app.services import search_service, user_service
from app.twitter_client import create_tweepy_client
import uvicorn
import tweepy

app = FastAPI()

def get_tweepy_client():
    return create_tweepy_client()

@app.get("/")
def home():
    return {"message": "Twitter Data Crawler is running!"}

@app.get("/search")
async def search_tweets(query: str,
                  max_results:int = 10,
                  client: tweepy.Client = Depends(create_tweepy_client)):
   return search_service.get_search_tweets(query, max_results, client)

@app.get("/user/{username}")
async def fetch_user(username: str, client: tweepy.Client = Depends(create_tweepy_client)):
    return user_service.get_user_by_username(username, client)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)