import pandas as pd

# Загрузка данных
# Замените 'file.csv' на имя вашего файла с данными
df = pd.read_csv('only_clients.csv')

cities_parameters = pd.read_csv('parameters/cities_pp_sc_so_ou.csv')

# Группировка данных по городам и вычисление среднего уровня образования
avg_ed_lvl = df.groupby('city_nm')['education_level_num'].mean()

cities_parameters['avg_ed_level'] = cities_parameters['city_nm'].map(avg_ed_lvl)
cities_parameters.to_csv('cities_all_parameters.csv', index=False)

print(avg_ed_lvl)
