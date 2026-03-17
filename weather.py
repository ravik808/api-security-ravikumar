import os
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Please set API_KEY in .env file.")

def get_weather(city):
    # Do NOT log user-provided location data.
    # City names can be considered personal data when combined with other information.
    # Logging them may violate privacy principles like data minimization under GDPR.

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        response = requests.get(url)

        if response.status_code == 429:
            print("Too many requests. Please try again later.")
            return None

        if response.status_code != 200:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        print("Network error:", e)
        return None


if __name__ == "__main__":
    city = input("Enter city: ")
    weather = get_weather(city)

    if weather:
        print("Weather data retrieved successfully.")