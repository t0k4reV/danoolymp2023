import folium
import pandas as pd

# Чтение данных из CSV файла, предположим, что столбец с координатами называется 'Координаты', и они разделены запятой
data = pd.read_csv('avg_spent_per_order_coordinates.csv')

# Создание карты
map = folium.Map()

# Разделение столбца 'Координаты' на отдельные столбцы 'Широта' и 'Долгота'
data[['Широта', 'Долгота']] = data['Координаты'].str.split(',', expand=True)

# Преобразование типов данных в числовой формат
data['Широта'] = pd.to_numeric(data['Широта'])
data['Долгота'] = pd.to_numeric(data['Долгота'])

# Добавление точек на карту на основе данных из CSV
for index, row in data.iterrows():
    location = [row['Широта'], row['Долгота']]
    radius = row['Средний_чек_на_1_заказ'] / 30  # Предполагается, что столбец с показателем называется 'Показатель'

    folium.CircleMarker(
        location=location,
        radius=radius,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(map)

# Сохранение карты в HTML файл
map.save('map_order_sum.html')
