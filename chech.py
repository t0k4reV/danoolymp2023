import pandas as pd


data = pd.read_csv('dataset.csv')
fdata = pd.read_csv('fdataset.csv')

print('not filtered', data['id'].count())
print('filtered', fdata['id'].count())