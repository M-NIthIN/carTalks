import requests
from src.utils.s3_utils import upload_to_s3
from src.utils.config import EDMUNDS_API_KEY
from datetime import date

def fetch_edmunds_reviews(brand_name, limit=10):
    url = f"https://api.edmunds.com/v1/reviews/{brand_name}"
    headers = {"Authorization": f"Bearer {EDMUNDS_API_KEY}"}
    params = {"limit": limit}
    response = requests.get(url, headers=headers, params=params)
    return response.json().get("data", [])

def save_edmunds_data_to_s3(brand_name):
    data = fetch_edmunds_reviews(brand_name)
    file_name = f"{brand_name}/edmunds/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_edmunds_data_to_s3("Tesla")
