from fastapi import FastAPI
import tweepy
import os
from services import user_service, search_service
from app.config import BEARER_TOKEN

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Twitter Data Crawler is running!"}

@app.get("/search")
def search_tweets(query: str, max_results:int = 10):
   return search_service.get_search_tweets(query, max_results)

@app.get("/user/{username}")
def fetch_user(username: str):
    return user_service.get_user_by_username(username)