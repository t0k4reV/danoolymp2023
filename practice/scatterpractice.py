import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('disney_plus_titles.csv')
data['duration'] = data['duration'].replace('min' or 'Season', '', regex=True).apply(pd.to_numeric, errors='coerce')
data2 = data[data['duration'] > 15]
plt.scatter(data2['release_year'], data2['duration'], alpha=0.5)
plt.show()