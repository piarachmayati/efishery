import pandas as pd
import numpy as np
import uuid
import random
import datetime
from datetime import timezone
from datetime import datetime
from random import randrange
from datetime import timedelta
import xlsxwriter

username = ['Andi', 'Budi', 'Taja']
lokasi = ['Bandung', 'Jakarta']
start = datetime.strptime('1/1/2019 ', '%m/%d/%Y ')
end = datetime.strptime('12/31/2019 ', '%m/%d/%Y ')

def random_date(start, end, n):
    dates = pd.Series(np.zeros(n))
    timestamp = pd.Series(np.zeros(n))
    for i in range(n) :
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        dates = start + timedelta(seconds=random_second)
        timestamp[i] = (dates - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s') 
    return(round(timestamp)) 

n = 1100000
device = random.randrange(16,31)


df = pd.DataFrame({ 'id' : uuid.uuid4(),
                   'device_id': 0x10,
                   'username': np.random.choice(username, n, replace=True),
                   'lokasi': np.random.choice(lokasi, n, replace=True),
                    'amount': np.random.choice(range(10, 1000), n, replace=True),
                    'timestamp': random_date(start, end, n) })

import datetime



df['id'] = [uuid.uuid4() for _ in range(len(df.index))]
df['device_id'] = [ hex(random.randrange(16,31)) for _ in range(len(df.index))]


df.username = df.username.astype('category')
df.lokasi = df.lokasi.astype('category')
df.id = df.id.astype('category')
df.device_id = df.device_id.astype('category')
df.amount = df.amount.astype('uint32')
df.timestamp = df.timestamp.astype('float32')
"""
writer = pd.ExcelWriter('generateData.xlsx', engine='xlsxwriter')
print (df)
"""
print (df.dtypes)
print (df.memory_usage(deep=True) / 1024 ** 2)
def memory_usage(df):
    return(round(df.memory_usage(deep=True).sum() / 1024 ** 2, 2))
print('Memory used:', memory_usage(df), 'Mb')

df.to_csv(r'data.csv', index=False)
