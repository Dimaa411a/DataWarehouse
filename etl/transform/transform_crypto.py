import pandas as pd
from datetime import datetime
from etl.extract.extract_crypto import connect_crypto_api


def transform_crypto(data):
    df = pd.DataFrame(data).T
    df = df.reset_index()

    df.columns = ['coin', 'price']
    df['currency'] = 'USD'
    df['date'] = datetime.now()

    return df   


df = transform_crypto(connect_crypto_api())
print(df)
