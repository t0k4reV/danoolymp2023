import pandas as pd

# Предполагаем, что у вас есть DataFrame df с данными из вашего описания
df = pd.read_csv('users_with_population.csv')
# Группировка данных по идентификатору клиента и подсчет количества его заказов
user_orders = df.groupby('client_id')['id'].count().reset_index()
user_orders.columns = ['client_id', 'order_cnt']  # Переименование колонок для ясности

# Сохранение результатов в CSV-файл
user_orders.to_csv('user_and_orders.csv', index=False)
