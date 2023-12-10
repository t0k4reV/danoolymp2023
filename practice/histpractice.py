import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('disney_plus_titles.csv')

vis1 = data.groupby('type')['rating'].value_counts()
vis1.unstack(0).plot(kind='bar', ylabel='freq')
plt.show()