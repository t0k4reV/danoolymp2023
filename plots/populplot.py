import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.colors as mcolors

# Ваш словарь с данными о городах и населении
population_data = {
    'Москва': 21696177,
    'Санкт-Петербург': 7600000,
    'Екатеринбург': 4239161,
    'Новосибирск': 2794266,
    'Самара': 3142683,
    'Казань': 4001625,
    'Краснодар': 5819345,
    'Челябинск': 3407145,
    'Уфа': 4077600,
    'Пермь': 2508352,
    'Воронеж': 2285282,
    'Омск': 1832000,
    'Волгоград': 2470057,
    'Нижний Новгород': 3081817,
    'Ростов-на-Дону': 4153800,
    'Красноярск': 2845545
}

# Создание DataFrame из словаря
city_population = pd.DataFrame(list(population_data.items()), columns=['Город', 'Население'])

# Сортировка по населению в порядке возрастания
city_population = pd.DataFrame(list(population_data.items()), columns=['Город', 'Население'])

# Сортировка по населению в порядке возрастания
city_population = city_population.sort_values(by='Население', ascending=True)

# Построение гистограммы
plt.figure(figsize=(10, 6))
plt.bar(city_population['Город'], city_population['Население'] / 1e6, color='gold')  # Делим на миллион
plt.xlabel('Город')
plt.ylabel('Население (млн. человек)')
plt.title('Население в различных регионах России ')
plt.xticks(rotation=90)
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.1f}'.format(x)))  # Форматирование оси y
plt.tight_layout()

# Отображение гистограммы
plt.show()
