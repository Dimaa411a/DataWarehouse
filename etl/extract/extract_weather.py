from etl.extract.api_client import APIClient
from dotenv import load_dotenv
import os

load_dotenv() # Loads variables from .env
weather_api_key = os.getenv("WEATHER_API")


#Extracting weather data
def connect_weather_api(cities: list) -> list:
    weather_client = APIClient(base_url="http://api.openweathermap.org/data/2.5",headers={})
    result = []
    for city in cities:
        weather_data = weather_client.get('/weather',params={"q": city,"appid":weather_api_key,"units":"metric"})
        result.append(weather_data)

    return result






