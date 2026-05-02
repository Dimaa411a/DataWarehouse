from etl.extract.extract_weather import connect_weather_api
from etl.transform.transform_weather import transform_weather
from etl.load.load_weather import load_weather
from db.connection import connect_db

def weather_pipeline():
    engine = connect_db()
    data = connect_weather_api(['Ivano-Frankivsk','Kyiv','Lviv','Donetsk','Dnipro','Warsaw','Prague','Berlin','Chicago','Toronto'])
    df = transform_weather(data)
    load_weather(df,engine)
