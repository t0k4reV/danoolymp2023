import pandas as pd


df = pd.read_csv('fincome_only_clients.csv')
# Фильтрация строк с положительным или равным нулю значением 'monthly_income_amt'
df = df[df['monthly_income_amt'] >= 0]
df = df[df['age'] >= 16]

cities_parameters = pd.read_csv('cities_all_parameters.csv')

# Группировка данных по городам и вычисление среднего уровня образования
avg_monthly_income = df.groupby('city_nm')['monthly_income_amt'].mean()
avg_age = df.groupby('city_nm')['age'].mean()


cities_parameters['avg_monthly_income'] = cities_parameters['city_nm'].map(avg_monthly_income)
cities_parameters['avg_age'] = cities_parameters['city_nm'].map(avg_age)


cities_parameters.to_csv('cities_all_parameters.csv', index=False)
