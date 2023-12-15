import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../users_with_population.csv')
# Группируем данные по клиентам и городам, вычисляем общую количество заказов для каждого клиента в каждом городе
total_orders = df.groupby(['client_id', 'city_nm'])['good_cnt'].count()

# Получаем среднее количество заказов на одного покупателя в каждом городе
avg_orders_per_user = total_orders.groupby('city_nm').mean()
print(avg_orders_per_user)
# Построение графика
plt.figure(figsize=(10, 6))
avg_orders_per_user.sort_values().plot(kind='bar', color='salmon')
plt.title('Среднее количество заказов на одного покупателя в каждом городе')
plt.xlabel('Город')
plt.ylabel('Средний количество заказов на одного покупателя')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

city_coordinates = {
    'Москва': '55.755829, 37.617627',
    'Санкт-Петербург': '59.938670, 30.314350',
    'Екатеринбург': '56.838011, 60.597474',
    'Новосибирск': '55.030280, 82.920383',
    'Самара': '53.195878, 50.100202',
    'Казань': '55.796125, 49.106400',
    'Краснодар': '45.035470, 38.975313',
    'Челябинск': '55.159902, 61.402554',
    'Уфа': '54.735148, 55.958596',
    'Пермь': '58.010400, 56.229486',
    'Воронеж': '51.660782, 39.200286',
    'Омск': '54.989362, 73.368037',
    'Волгоград': '48.707070, 44.516952',
    'Нижний Новгород': '56.326793, 44.006437',
    'Ростов-на-Дону': '47.222104,  39.720179',
    'Красноярск': '56.010552, 92.852531'
}
### Здесь мы создаем новую таблицу, которая содержит только информацию о городе, его координатах  и показателя avg_spent_per_customer ###
# Создание нового DataFrame с данными для сохранения в CSV
new_df = pd.DataFrame({
    'Город': avg_orders_per_user.index,  # Названия городов из индекса avg_spent_per_customer
    'Координаты': [city_coordinates[city] for city in avg_orders_per_user.index],  # Координаты из словаря city_coordinates
    'Среднее количество заказов на пользователя': avg_orders_per_user.values  # Параметр avg_spent_per_customer
})

# Сохранение нового DataFrame в CSV файл
new_df.to_csv('avg_orders_per_customer_coordinates.csv', index=False)
