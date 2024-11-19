# api_handler.apy

import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://app.zipcodebase.com/api/v1/search"

def fetch_zip_code(city):
    try:
        response = requests.get(BASE_URL, params={"apikey": API_KEY, "city": city})
        response.raise_for_status()
        data = response.json()
        if "results" in data and data["results"]:
            return data["results"][city][0]  # Use the first zip code
    except Exception as e:
        print(f"Error fetching zip code: {e}")
    return "00000"  # Default zip code if API fails

