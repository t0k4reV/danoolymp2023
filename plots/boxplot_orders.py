import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
# Предполагаем, что данные хранятся в файле 'data.csv'
data = pd.read_csv('../dataset.csv')
# data = pd.read_csv('fdataset.csv')

# Группировка данных по городам и количеству заказов пользователя
city_user_orders = data.groupby(['city_nm', 'client_id']).size().reset_index(name='order_count')

# Создание боксплота
plt.figure(figsize=(10, 6))
boxplot = city_user_orders.boxplot(column='order_count', by='city_nm', figsize=(12, 8))

# Настройки диаграммы
plt.title('Количество заказов пользователя для каждого города')
plt.xlabel('Город')
plt.ylabel('Количество заказов пользователя')
plt.xticks(rotation=45)
plt.tight_layout()

# Отображение боксплота
plt.show()
