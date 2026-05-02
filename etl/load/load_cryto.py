from sqlalchemy import text

def load_crypto(df, engine):
    records = df.to_dict("records")

    with engine.begin() as conn:
        conn.execute(
            text("""
                INSERT INTO crypto_prices (coin, price, currency, date)
                VALUES (:coin, :price, :currency, :date)
            """),
            records
        )
