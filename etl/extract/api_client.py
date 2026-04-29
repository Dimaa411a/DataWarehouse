import requests

class APIClient:
    def __init__(self,base_url,headers):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self,endpoint,params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url,headers=self.headers,params=params)

        if response.status_code != 200:
            raise Exception(f"API Error {response.status_code}: {response.text}")

        return response.json()





