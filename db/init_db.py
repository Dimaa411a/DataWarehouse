from db.connection import connect_db
from db.models import create_crypto_table, create_weather_table

engine = connect_db()

def init_database():
    create_crypto_table(engine)
    create_weather_table(engine)
    print("Tables created (if not exist)")

if __name__ == "__main__":
    init_database()
