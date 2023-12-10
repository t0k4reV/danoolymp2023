import pandas as pd
import matplotlib.pyplot as plt

# Предположим, что у вас есть DataFrame с данными, давайте назовем его df
df = pd.read_csv('users_with_population.csv')
# Рассчитываем общую сумму каждого заказа
df['total_order_amount'] = df['good_price'] * df['good_cnt']

# Группируем данные по клиентам и городам, вычисляем общую сумму заказов для каждого клиента в каждом городе
total_spent_per_customer = df.groupby(['client_id', 'city_nm'])['total_order_amount'].sum()

# Получаем средний чек на одного покупателя в каждом городе
avg_spent_per_customer = total_spent_per_customer.groupby('city_nm').mean()
print(avg_spent_per_customer)
# Построение графика
plt.figure(figsize=(10, 6))
avg_spent_per_customer.sort_values().plot(kind='bar', color='salmon')
plt.title('Средний чек на одного покупателя в каждом городе')
plt.xlabel('Город')
plt.ylabel('Средний чек на одного покупателя')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
