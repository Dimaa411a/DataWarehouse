def load_weather(df, engine):
    df.to_sql(
        name="weather",
        con=engine,
        if_exists="append",
        index=False
    )

