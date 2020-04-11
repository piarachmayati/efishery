import pandas as pd
import numpy as np

dtypes = {
    "id": "category",
    "device_id": "category",
    "username": "category",
    "lokasi": "category"    
}

#df = pd.read_excel('pandas_simple1.xlsx')
df = pd.read_csv('data.csv',dtype=dtypes)
filt = df.filter(['amount','timestamp'])
head = filt[:10]
tail = filt[-10:]
filter_amount = pd.concat([head,tail])
print (filter_amount)

#group by device
device = df.filter(['device_id','amount','timestamp'])
percentile_device = device.groupby('device_id').quantile(.94)
percentile_device.sort_values("amount", axis = 0, ascending = True, inplace = True, na_position = 'first')
print (percentile_device)

#group by username
username = df.filter(['username','amount','timestamp'])
percentile_username = username.groupby('username').quantile(.94)
percentile_username.sort_values("amount", axis = 0, ascending = True, inplace = True, na_position = 'first')
print (percentile_username)

#group by lokasi
lokasi = df.filter(['lokasi','amount','timestamp'])
percentile_lokasi = lokasi.groupby('lokasi').quantile(.94)
percentile_lokasi.sort_values("amount", axis = 0, ascending = True, inplace = True, na_position = 'first')
print (percentile_lokasi)

#group by device
data = df.loc['1546300877':'1577748254']
data = data.groupby('device_id').agg({'amount':['max','min','sum','count']})
data.columns = ['max', 'min', 'sum', 'count']
agregasi_device = data.reset_index()
print (agregasi_device)

device = df.filter(['device_id','amount','timestamp']).loc['1546300877':'1577748254']
percentile_device2 = device.groupby('device_id').quantile([.25,.50,.75])
print(percentile_device2)

#group by lokasi
data = df.loc['1546300877':'1577748254']
data = data.groupby('lokasi').agg({'amount':['max','min','sum','count']})
data.columns = ['max', 'min', 'sum', 'count']
agregasi_lokasi = data.reset_index()
print (agregasi_lokasi)

lokasi = df.filter(['lokasi','amount','timestamp']).loc['1546300877':'1577748254']
percentile_lokasi2 = lokasi.groupby('lokasi').quantile([.25,.50,.75])
print(percentile_lokasi2)

#group by username
data = df.loc['1546300877':'1577748254']
data = data.groupby('username').agg({'amount':['max','min','sum','count']})
data.columns = ['max', 'min', 'sum', 'count']
agregasi_username = data.reset_index()
print (agregasi_username)

username = df.filter(['username','amount','timestamp']).loc['1546300877':'1577748254']
percentile_username2 = username.groupby('username').quantile([.25,.50,.75])
print(percentile_username2)

#group by all
data = df.loc['1546300877':'1577748254']
data = data.groupby(['device_id','lokasi','username']).agg({'amount':['max','min','sum','count']})
data.columns = ['max', 'min', 'sum', 'count']
agregasi_all= data.reset_index()
print (agregasi_all)

filter_amount.to_csv(r'filter_amount.csv')
percentile_device.to_csv(r'percentile_device.csv')
percentile_username.to_csv(r'percentile_username.csv')
percentile_lokasi.to_csv(r'percentile_lokasi.csv')
agregasi_device.to_csv(r'agregasi_device.csv')
percentile_device2.to_csv(r'agregasi_device_percentile.csv')
agregasi_lokasi.to_csv(r'agregasi_lokasi.csv')
percentile_lokasi2.to_csv(r'agregasi_lokasi_percentile.csv')
agregasi_username.to_csv(r'agregasi_username.csv')
percentile_username2.to_csv(r'agregasi_username_percentile.csv')
agregasi_all.to_csv(r'agregasi_all.csv')









