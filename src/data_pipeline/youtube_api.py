from googleapiclient.discovery import build
from src.utils.s3_utils import upload_to_s3
from src.utils.config import YOUTUBE_API_KEY
from datetime import date

def fetch_youtube_videos(brand_name, max_results=10):
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=brand_name,
        part="snippet",
        maxResults=max_results,
        type="video"
    )
    response = request.execute()
    videos = [
        {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "published_at": item["snippet"]["publishedAt"],
            "channel_title": item["snippet"]["channelTitle"],
        }
        for item in response.get("items", [])
    ]
    return videos

def save_youtube_data_to_s3(brand_name):
    data = fetch_youtube_videos(brand_name)
    file_name = f"{brand_name}/youtube/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_youtube_data_to_s3("Tesla")
