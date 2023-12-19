import pandas as pd

# Загрузка данных
# Замените 'file.csv' на имя вашего файла с данными
df = pd.read_csv('dataset.csv')

# Оставить только одну строку для каждого client_id
unique_clients = df.drop_duplicates(subset='client_id', keep='first')

# Вывод первых нескольких строк для проверки
unique_clients.to_csv('only_clients.csv', index=False)