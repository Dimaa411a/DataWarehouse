from sqlalchemy import text

def load_weather(df, engine):
    records = df.to_dict("records")

    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO weather
                (city, weather, temperature, wind_speed, currency, country, date)
                VALUES
                (:city, :weather, :temperature, :wind_speed, :currency, :country, :date)
            """),
            records
        )
