import requests
from src.utils.s3_utils import upload_to_s3
from src.utils.config import TIKTOK_ACCESS_TOKEN

def fetch_tiktok_videos(brand_name, limit=10):
    # Replace with actual TikTok API endpoint if available
    url = "https://api.tiktok.com/mock/endpoint"  # Mock endpoint
    params = {
        "access_token": TIKTOK_ACCESS_TOKEN,
        "query": brand_name,
        "limit": limit
    }
    response = requests.get(url, params=params)
    videos = response.json().get("data", [])
    return videos

def save_tiktok_data_to_s3(brand_name):
    data = fetch_tiktok_videos(brand_name)
    file_name = f"{brand_name}/tiktok/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_tiktok_data_to_s3("Tesla")
