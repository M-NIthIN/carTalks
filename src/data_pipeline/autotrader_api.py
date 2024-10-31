 
import requests
from src.utils.s3_utils import upload_to_s3
from src.utils.config import AUTOTRADER_API_KEY
from datetime import date

def fetch_autotrader_reviews(brand_name, limit=10):
    url = "https://api.autotrader.com/v1/reviews"  # Hypothetical endpoint
    headers = {"Authorization": f"Bearer {AUTOTRADER_API_KEY}"}
    params = {"brand": brand_name, "limit": limit}
    response = requests.get(url, headers=headers, params=params)
    return response.json().get("data", [])

def save_autotrader_data_to_s3(brand_name):
    data = fetch_autotrader_reviews(brand_name)
    file_name = f"{brand_name}/autotrader/{date.today()}/raw_data.json"
    upload_to_s3(data, "car-talks-raw", file_name)

if __name__ == "__main__":
    save_autotrader_data_to_s3("Tesla")
