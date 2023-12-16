import pandas as pd


data = pd.read_csv('T_games_dataset.csv')['id'].count()
fdata = pd.read_csv('../filtered_total_data.csv')['id'].count()

print(data)
print('фильтр')
print(fdata)

print(data-fdata)

