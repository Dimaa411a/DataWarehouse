from etl.extract.extract_crypto import connect_crypto_api
from etl.transform.transform_crypto import transform_crypto
from etl.load.load_cryto import load_crypto
from db.connection import connect_db

def crypto_pipeline():
    engine = connect_db()
    data = connect_crypto_api()
    df = transform_crypto(data)
    load_crypto(df,engine)
