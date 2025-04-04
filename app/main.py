from fastapi import FastAPI
from app.services import search_service, user_service
import uvicorn

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

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)