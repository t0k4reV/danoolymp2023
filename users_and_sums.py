import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
# Предполагаем, что данные хранятся в файле 'data.csv'
data = pd.read_csv('dataset.csv')

# Создание нового DataFrame с суммарными тратами каждого клиента
client_spending = data.assign(Total_spent=data['good_price'] * data['good_cnt']).groupby(['client_id', 'city_nm'])['Total_spent'].sum().reset_index()

# Сохранение данных в CSV файл
client_spending.to_csv('client_spending_with_city.csv', index=False)

# Отображение первых нескольких строк созданного DataFrame для проверки
print(client_spending.head())
