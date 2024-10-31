from dotenv import load_dotenv
import os

load_dotenv()

# Twitter API keys
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Instagram (Facebook Graph) API
INSTAGRAM_ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")

# YouTube API
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Reddit API keys
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# TikTok API (if accessible)
TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")

# CarGurus API
CARGURUS_API_KEY = os.getenv("CARGURUS_API_KEY")

# AutoTrader API
AUTOTRADER_API_KEY = os.getenv("AUTOTRADER_API_KEY")

# Edmunds API
EDMUNDS_API_KEY = os.getenv("EDMUNDS_API_KEY")

# S3 bucket settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
RAW_BUCKET =  os.getenv("RAW_BUCKET")
PROCESSED_BUCKET = os.getenv("PROCESSED_BUCKET")
