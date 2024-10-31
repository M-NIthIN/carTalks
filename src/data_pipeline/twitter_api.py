
import tweepy
from src.utils.s3_utils import upload_to_s3
from src.utils.config import TWITTER_BEARER_TOKEN
from datetime import date

# Set up Twitter API client
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_tweets(brand_name, max_results=10):
    query = f"{brand_name} -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=["created_at", "text", "public_metrics"])
    data = [{"text": tweet.text, "created_at": tweet.created_at, "metrics": tweet.public_metrics} for tweet in tweets.data]
    return data

def save_tweets_to_s3(brand_name):
    data = fetch_tweets(brand_name)
    file_name = f"{brand_name}/twitter/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_tweets_to_s3("Tesla")  # Example usage
