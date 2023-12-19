import pandas as pd
import matplotlib.pyplot as plt

# Предположим, что у вас есть DataFrame с данными, давайте назовем его df
df = pd.read_csv('../filtered_total_data.csv')
cities_parameters = pd.read_csv('../merges/cities_pop.csv')
# Группировка данных по городам и вычисление общей суммы потраченных денег на игры в каждом городе
total_spent_by_city = df.groupby('city_nm')['good_price'].sum()

# Получение численности населения городов
city_population = df.groupby('city_nm')['city_population'].max()

# Расчет суммы на душу населения
spent_per_capita = total_spent_by_city / city_population
print(spent_per_capita)

# # Построение графика
# plt.figure(figsize=(10, 6))
# spent_per_capita.sort_values().plot(kind='bar', color='gold')
# plt.title('Средняя сумма потраченных денег на игры на душу населения в каждом городе')
# plt.xlabel('Город')
# plt.ylabel('Средняя сумма потраченных денег на игры на душу населения')
# plt.xticks(rotation=90)
# plt.tight_layout()
# plt.show()


cities_parameters['spent_per_capita'] = cities_parameters['city_nm'].map(spent_per_capita)
cities_parameters.to_csv('cities_pp_sc.csv', index=False)

# ## Тут мы создаем отдельную таблицу с результатом
# print(spent_per_capita)
# spent_per_capita.to_csv('spent_per_capita.csv')

