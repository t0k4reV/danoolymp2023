import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Предположим, что у вас есть DataFrame df с нужными данными
df = pd.read_csv('cities_all_parameters.csv')
# Исключение столбцов 'city_nm' и 'coordinates'
columns_to_exclude = ['city_nm', 'coordinates']
columns_for_correlation = [col for col in df.columns if col not in columns_to_exclude]

# Создание корреляционной матрицы
correlation_matrix = df[columns_for_correlation].corr()

# Построение тепловой карты
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
