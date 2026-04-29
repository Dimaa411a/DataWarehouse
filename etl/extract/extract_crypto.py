from etl.extract.api_client import APIClient
from dotenv import load_dotenv
import os

load_dotenv() # Loads variables from .env
crypto_api_key = os.getenv("CRYPTO_API")

def connect_crypto_api():
    crypto_client = APIClient(base_url=f"https://api.coingecko.com/api/v3/",headers={"x-cg-demo-api-key": crypto_api_key})

    crypto_result = crypto_client.get(endpoint='/simple/price',params={"ids": "bitcoin,ethereum,dogecoin",
            "vs_currencies": "usd"})

    return crypto_result
