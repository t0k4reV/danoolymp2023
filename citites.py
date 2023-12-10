import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('T_games_dataset.csv')

orders_cities = data.groupby('city_nm')['good_cnt'].count().sort_values(ascending=False)
print(orders_cities)