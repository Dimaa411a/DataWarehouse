import pandas as pd
from datetime import datetime

def transform_crypto(data):
    df = pd.DataFrame(data).T
    df = df.reset_index()

    df.columns = ['coin', 'price']
    df['currency'] = 'USD'
    df['date'] = datetime.now()

    return df
