import pandas as pd

# Загрузка данных из нового файла
client_spending_with_city = pd.read_csv('client_spending_with_city.csv')

# Определение 5-го и 95-го персентиля
percentile_5 = client_spending_with_city['Total_spent'].quantile(0.05)
percentile_95 = client_spending_with_city['Total_spent'].quantile(0.95)

# Фильтрация данных без выбросов
filtered_data = client_spending_with_city[
    (client_spending_with_city['Total_spent'] >= percentile_5) &
    (client_spending_with_city['Total_spent'] <= percentile_95)
]

# Сохранение отфильтрованных данных в новый CSV файл
filtered_data.to_csv('client_spending_filtered.csv', index=False)
