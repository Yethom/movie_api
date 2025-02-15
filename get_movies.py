from config import config
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_auth():
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {config.BEARER_TOKEN}"
    }
    return headers

def fetch_data(url: str):
    response = requests.get(url, headers=get_auth())
    if response.status_code == 200:
        data = response.json()
        # return data["results"]
        return data.json().get("results", [])
    logger.error(f"Failed to fetch data. Status code: {response.status_code}")
    return None

def fetch_popular_movies():
    return fetch_data(config.POPULAR_BASE_URL)

def fetch_trending_movies():
    return fetch_data(config.TRENDING_TODAY_URL)
