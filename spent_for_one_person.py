import pandas as pd

# Загрузка данных о заказах игр
games_orders = pd.read_csv('users_with_population.csv')

# Здесь предполагается, что у вас уже есть столбец с численностью населения в каждом городе
# Добавим столбец с общей суммой потраченных денег на игры
games_orders['total_spent'] = games_orders['good_price'] * games_orders['good_cnt']

# Группировка по городу и вычисление общей потраченной суммы на игры в каждом городе
total_spent_per_city = games_orders.groupby('city_nm')['total_spent'].sum()

# Объединение данных о потраченной сумме на игры и численности населения по городам
data = pd.merge(total_spent_per_city, games_orders[['city_nm', 'city_population']], on='city_nm')

# Вычисление среднего количества денег, потраченного на игры на душу населения
data['spent_per_person'] = data['total_spent'] / data['city_population']

# Вывод первых строк для проверки
print(data.head())

import matplotlib.pyplot as plt

# Сортировка данных для более наглядного отображения
data = data.sort_values('spent_per_person', ascending=False)

# Построение графика
plt.figure(figsize=(10, 6))
plt.bar(data['city_nm'], data['spent_per_person'])
plt.xlabel('Город')
plt.ylabel('Средние затраты на игры на душу населения')
plt.title('Средние затраты на игры на душу населения в каждом городе')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
