import pandas as pd
import matplotlib.pyplot as plt

# Код для первого графика
df = pd.read_csv('../filtered_total_data.csv')
total_spent_by_city = df.groupby('city_nm')['good_price'].sum()
city_population = df.groupby('city_nm')['city_population'].max()
spent_per_capita = total_spent_by_city / city_population * 1500
# Код для второго графика
df['total_order_amount'] = df['good_price'] * df['good_cnt']
total_spent_per_customer = df.groupby(['client_id', 'city_nm'])['total_order_amount'].sum()
avg_spent_per_customer = total_spent_per_customer.groupby('city_nm').mean()

# Построение графика
plt.figure(figsize=(10, 6))

# Первый график
spent_per_capita.sort_values().plot(kind='bar', color='gold', label='Средняя сумма потраченных денег на игры на душу населения')

# Второй график, наложенный на первый
avg_spent_per_customer.sort_values().plot(kind='bar', color='blue', alpha=0.5, label='Средний чек на одного покупателя')

plt.title('Сравнение средней суммы потраченных денег на игры и среднего чека на покупателя в каждом городе')
plt.xlabel('Город')
plt.ylabel('Сумма / Чек')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()
