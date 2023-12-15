import pandas as pd


fdata = pd.read_csv('filtered_user_orders.csv')

data = pd.read_csv('user_and_orders.csv')


print(fdata.count())

print(data.count())