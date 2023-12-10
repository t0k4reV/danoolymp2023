import pandas as pd
import matplotlib.pyplot as plt

# Предположим, что у вас есть DataFrame с данными, давайте назовем его df
df = pd.read_csv('users_with_population.csv')
# Группировка данных по городам и вычисление общей суммы потраченных денег на игры в каждом городе
total_spent_by_city = df.groupby('city_nm')['good_price'].sum()
print(total_spent_by_city)

# Получение численности населения городов
city_population = df.groupby('city_nm')['city_population'].max()
print(city_population)

# Расчет суммы на душу населения
spent_per_capita = total_spent_by_city / city_population

# Построение графика
plt.figure(figsize=(10, 6))
spent_per_capita.sort_values().plot(kind='bar', color='skyblue')
plt.title('Средняя сумма потраченных денег на игры на душу населения в каждом городе')
plt.xlabel('Город')
plt.ylabel('Средняя сумма потраченных денег на игры на душу населения')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
