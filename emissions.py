import pandas as pd
import matplotlib.pyplot as plt

# Предположим, что у вас есть DataFrame с данными, давайте назовем его df
df = pd.read_csv('users_with_population.csv')

# Предположим, что у вас есть DataFrame с данными, давайте назовем его df

# Рассчитываем общую сумму каждого заказа
df['Total_order_amount'] = df['good_price'] * df['good_cnt']

# Группируем данные по клиентам и вычисляем количество заказов для каждого клиента
orders_per_customer = df.groupby('client_id')['Total_order_amount'].count()

# Создаем гистограмму для отображения количества заказов на каждого пользователя
plt.figure(figsize=(12, 6))
plt.bar(orders_per_customer.index, orders_per_customer.values, color='skyblue')
plt.title('Количество заказов на каждого пользователя')
plt.xlabel('Пользователи')
plt.ylabel('Количество заказов')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
