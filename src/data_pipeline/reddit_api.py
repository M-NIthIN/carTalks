import praw
from src.utils.s3_utils import upload_to_s3
from src.utils.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)

def fetch_reddit_posts(brand_name, limit=10):
    posts = []
    for submission in reddit.subreddit("all").search(brand_name, limit=limit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "score": submission.score,
            "created_utc": submission.created_utc,
            "num_comments": submission.num_comments
        })
    return posts

def save_reddit_data_to_s3(brand_name):
    data = fetch_reddit_posts(brand_name)
    file_name = f"{brand_name}/reddit/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_reddit_data_to_s3("Tesla")
