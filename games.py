# import pandas as pd
# import matplotlib.pyplot as plt
#
# dd = pd.read_csv('T_games_dataset.csv')
# mask = ['Xbox подписка', 'Бестселлеры', 'Карты оплаты', "Предзаказы", 'Скидки', 'Классика от Deep Silver', 'Новинки']
#
# df = dd[~dd['category_name'].isin(mask)]
#
# genre_education_counts = df.groupby(['category_name', 'education_level']).size().unstack()
# print(dd.groupby('category_name').count().reset_index())
# genre_education_percent = genre_education_counts.div(genre_education_counts.sum(axis=1), axis=0) * 100
#
#
# genre_education_percent.plot(kind='bar', stacked=True, figsize=(12, 8))
# plt.title('Количество пользователей по уровням образования для каждого жанра')
# plt.xlabel('Жанр')
# plt.ylabel('Количество пользователей')
# plt.legend(title='Уровень образования')
# plt.xticks(rotation=30)
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

dd = pd.read_csv('sources/T_games_dataset.csv')
mask = ['Xbox подписка', 'Бестселлеры', 'Карты оплаты', "Предзаказы", 'Скидки', 'Классика от Deep Silver', 'Новинки']

df = dd[~dd['category_name'].isin(mask)]

genre_education_counts = df.groupby(['category_name', 'education_level']).size().unstack()

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.15
index = range(len(genre_education_counts))
education_levels = genre_education_counts.columns
colors = ['red', 'blue', 'green', 'orange', 'purple']  # список цветов для каждого уровня образования

for i, education_level in enumerate(education_levels):
    values = genre_education_counts[education_level] / genre_education_counts.sum(axis=1) * 100
    bar_position = [x + i * bar_width for x in index]
    ax.bar(bar_position, values, width=bar_width, label=education_level, color=colors[i])

ax.set_xticks([x + 0.5 for x in index])
ax.set_xticklabels(genre_education_counts.index, rotation=30)
plt.title('Процент пользователей по уровням образования для каждого жанра')
plt.xlabel('Жанр')
plt.ylabel('Процент пользователей')
plt.legend(title='Уровень образования')
plt.tight_layout()
plt.show()
