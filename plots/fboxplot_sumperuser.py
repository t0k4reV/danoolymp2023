import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из нового файла
client_spending_with_city = pd.read_csv('../client_spending_filtered.csv')

# Создание боксплота
plt.figure(figsize=(10, 6))
boxplot = client_spending_with_city.boxplot(column='Total_spent', by='city_nm', figsize=(12, 8))

# Настройки диаграммы
plt.title('Распределение общих трат клиентов из разных городов на игры')
plt.xlabel('Город')
plt.ylabel('Общие траты на игры')
plt.xticks(rotation=45)
plt.tight_layout()

# Отображение боксплота
plt.show()
