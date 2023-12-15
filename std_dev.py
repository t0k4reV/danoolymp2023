import pandas as pd

# Загрузка общего датафрейма
total_data = pd.read_csv('dataset.csv')  # Замените на путь к вашему общему датафрейму

# Загрузка отфильтрованного датафрейма с ранее исключенными клиентами
excluded_clients = pd.read_csv('client_spending_filtered.csv')  # Замените на путь к вашему фильтрованному датафрейму

# Получение списка исключенных ID клиентов
excluded_ids = excluded_clients['client_id'].tolist()

# Исключение строк с исключенными клиентами из общего датафрейма
filtered_total_data = total_data[~total_data['client_id'].isin(excluded_ids)]

# Сохранение отфильтрованных данных в новый CSV файл
filtered_total_data.to_csv('filtered_total_data.csv', index=False)
