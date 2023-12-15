import pandas as pd

# Предполагаем, что ваш DataFrame называется df
df = pd.read_csv('dataset.csv')
# Группировка данных по 'Client_id' и подсчет количества заказов для каждого клиента
user_orders = df.groupby('client_id')['id'].count().reset_index()

# Вычисление стандартного отклонения количества заказов
std_dev = user_orders['id'].std()

# Определение порога для фильтрации (например, 2 стандартных отклонения от среднего)
threshold = 2 * std_dev

# Вычисление среднего количества заказов
mean_orders = user_orders['id'].mean()

# Фильтрация пользователей по стандартному отклонению их заказов
outlier_users = user_orders[user_orders['id'] > (mean_orders + threshold)]

# Фильтрация основного датасета, исключая пользователей-выбросы
filtered_df = df[~df['client_id'].isin(outlier_users['client_id'])]

filtered_df.to_csv('fdataset.csv', index=False)
