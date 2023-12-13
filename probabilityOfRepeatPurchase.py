import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sources/T_games_dataset.csv')
# mask = ['Xbox подписка', 'Бестселлеры', 'Карты оплаты', "Предзаказы", 'Скидки', 'Классика от Deep Silver', 'Новинки']



# Группировка данных по категориям и пользователям для подсчета повторных покупок
# category_counts = data[~data['category_name'].isin(mask)]
category_counts = data.groupby(['category_name', 'client_id', 'good_name']).size().reset_index(name='purchase_count')

category_repeats = category_counts[category_counts['purchase_count'] > 1]

# Группировка для подсчета уникальных повторных покупок в каждой категории
repeat_purchases = category_repeats.groupby('category_name').size().reset_index(name='repeat_purchase_count')

# Общее количество покупок по каждой категории
total_purchases = data.groupby('category_name').size().reset_index(name='total_purchase_count')

# Объединение данных для вычисления вероятности повторной покупки
category_probabilities = pd.merge(total_purchases, repeat_purchases, on='category_name', how='left')
category_probabilities['repeat_purchase_probability'] = category_probabilities['repeat_purchase_count'] / category_probabilities['total_purchase_count']

# Визуализация результатов
plt.figure(figsize=(10, 6))
plt.bar(category_probabilities['category_name'], category_probabilities['repeat_purchase_probability'])
plt.xlabel('Категория игр')
plt.ylabel('Вероятность повторной покупки')
plt.title('Вероятность повторной покупки игр в каждой категории')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
