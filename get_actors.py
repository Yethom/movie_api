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

def fetch_trending_people():
    url = config.PEOPLE_TRENDING
    response = requests.get(url, headers=get_auth())
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data["results"]
    logger.error(f"Failed to fetch data. Status code: {response.status_code}")
    return None
