import requests
from src.utils.s3_utils import upload_to_s3
from src.utils.config import INSTAGRAM_ACCESS_TOKEN
from datetime import date

def fetch_instagram_posts(brand_name, limit=10):
    url = f"https://graph.facebook.com/v11.0/{INSTAGRAM_USER_ID}/media"
    params = {
        "access_token": INSTAGRAM_ACCESS_TOKEN,
        "fields": "id,caption,media_url,timestamp,like_count,comments_count",
        "limit": limit
    }
    response = requests.get(url, params=params)
    posts = response.json().get("data", [])
    return posts

def save_instagram_data_to_s3(brand_name):
    data = fetch_instagram_posts(brand_name)
    file_name = f"{brand_name}/instagram/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_instagram_data_to_s3("Tesla")
