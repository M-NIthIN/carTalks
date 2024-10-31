import streamlit as st
from src.data_pipeline.youtube_api import save_youtube_data_to_s3
from src.data_pipeline.instagram_api import save_instagram_data_to_s3
from src.data_pipeline.reddit_api import save_reddit_data_to_s3
from src.data_pipeline.twitter_api import save_tweets_to_s3
from src.data_pipeline.tiktok_api import save_tiktok_data_to_s3
from src.data_pipeline.cargurus_api import save_cargurus_data_to_s3
from src.data_pipeline.autotrader_api import save_autotrader_data_to_s3
from src.data_pipeline.edmunds_api import save_edmunds_data_to_s3

# Define available brands
brands = ["Tesla", "Toyota", "BMW"]

st.title("CarTalks Data Pulling Dashboard")

selected_brand = st.selectbox("Select a car brand:", brands)

if st.button("Fetch Data"):
    # Pull data for the selected brand
    save_youtube_data_to_s3(selected_brand)
    save_instagram_data_to_s3(selected_brand)
    save_reddit_data_to_s3(selected_brand)
    save_tweets_to_s3(selected_brand)
    save_tiktok_data_to_s3(selected_brand)
    save_cargurus_data_to_s3(selected_brand)
    save_autotrader_data_to_s3(selected_brand)
    save_edmunds_data_to_s3(selected_brand)
    
    st.success(f"Data fetched and stored for {selected_brand} successfully!")
