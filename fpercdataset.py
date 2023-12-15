import pandas as pd

# Загрузка общего датафрейма
total_data = pd.read_csv('dataset.csv')  # Замените на путь к вашему общему датафрейму

# Загрузка фильтрованного датафрейма с оставшимися клиентами
remaining_clients = pd.read_csv('client_spending_filtered.csv')  # Замените на путь к вашему фильтрованному датафрейму

# Получение списка оставшихся ID клиентов
remaining_ids = remaining_clients['client_id'].tolist()

# Фильтрация основного датафрейма по оставшимся клиентам
filtered_total_data = total_data[total_data['client_id'].isin(remaining_ids)]

# Сохранение отфильтрованных данных в новый CSV файл
filtered_total_data.to_csv('filtered_total_data.csv', index=False)
