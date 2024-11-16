import requests
from django.conf import settings

API_BASE_URL = "https://api.spoonacular.com"

def get_random_recipes(number=1):
    """Fetch random recipes from Spoonacular API."""
    url = f"{API_BASE_URL}/recipes/random"
    params = {
        "apiKey": settings.SPOONACULAR_API_KEY,
        "number": number
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Returns the JSON response
    else:
        response.raise_for_status()  # Raises an exception for errors
