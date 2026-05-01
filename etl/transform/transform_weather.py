import pandas as pd
from datetime import datetime

def transform_weather(data):
    rows = []
    for item in data:
        rows.append({
            "city" : item['name'],
            "weather": item['weather'][0]['main'],
            "temperature" : item['main']['temp'],
            "wind_speed" :item['wind']['speed'],
            "currency" : item['weather'][0]['description'],
            "country" : item['sys']['country'],
            "date" : datetime.now()
        })

    df = pd.DataFrame(rows)
    return df

