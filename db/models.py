from sqlalchemy import text
from db.connection import connect_db

engine = connect_db()

def create_crypto_table(engine):
    with engine.begin() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS crypto_prices (
                coin VARCHAR(55),
                price FLOAT,
                currency VARCHAR(55),
                date TIMESTAMP
            )
        """))



def create_weather_table(engine):
    with engine.begin() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS weather (
                city VARCHAR(55),
                weather VARCHAR(55),
                temperature FLOAT,
                wind_speed FLOAT,
                currency VARCHAR(55),
                country VARCHAR(55),
                date TIMESTAMP
            )
        """))

