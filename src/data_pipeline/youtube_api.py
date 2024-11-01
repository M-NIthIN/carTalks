import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi
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
    videos = []

    for item in response.get("items", []):
        video_data = {
            "title": item["snippet"]["title"],
            "description": item["snippet"]["description"],
            "published_at": item["snippet"]["publishedAt"],
            "channel_title": item["snippet"]["channelTitle"],
            "video_id": item["id"]["videoId"]
        }
        try:
            transcript_data = YouTubeTranscriptApi.get_transcript(video_data["video_id"])
            transcript_text = " ".join([entry['text'] for entry in transcript_data])
            video_data["transcript"] = transcript_text
        except Exception as e:
            video_data["transcript"] = f"Error: Could not retrieve transcript. Reason: {str(e)}"

        videos.append(video_data)
    return videos

def save_youtube_data_to_s3(brand_name):
    data = fetch_youtube_videos(brand_name)
    file_name = f"{brand_name}/youtube/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    #save_youtube_data_to_s3("Tesla")
    vid = fetch_youtube_videos('Tesla')
    sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(vid, ensure_ascii=False,indent=4))

