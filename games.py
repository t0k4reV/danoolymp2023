import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('T_games_dataset.csv')
mask = ['Xbox подписка', 'Б24'
                         '1":LKJHgfdsaестселлеры', 'Карты оплаты', "Предзаказы", 'Скидки']

genre_education_counts = df.groupby(['category_name', 'education_level']).size().unstack()

genre_education_counts.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Количество пользователей по уровням образования для каждого жанра')
plt.xlabel('Жанр')
plt.ylabel('Количество пользователей')
plt.legend(title='Уровень образования')
plt.xticks(rotation=30)
plt.show()
