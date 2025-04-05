def get_search_tweets(query, max_results, client):
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results)
        tweets = [tweet.text for tweet in response.data]
        return {"tweets": tweets}
    except Exception as e:
        return {"error": str(e)}



