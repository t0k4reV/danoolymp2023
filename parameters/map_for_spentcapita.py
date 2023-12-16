import folium
import pandas as pd

# Чтение данных из CSV файла, предположим, что столбец с координатами называется 'Координаты', и они разделены запятой
data = pd.read_csv('spent_with_coordinates.csv')

# Создание карты
map = folium.Map()

# Разделение столбца 'Координаты' на отдельные столбцы 'Широта' и 'Долгота'
data[['Широта', 'Долгота']] = data['city_coordinates'].str.split(',', expand=True)

# Преобразование типов данных в числовой формат
data['Широта'] = pd.to_numeric(data['Широта'])
data['Долгота'] = pd.to_numeric(data['Долгота'])

# Добавление точек на карту на основе данных из CSV
for index, row in data.iterrows():
    location = [row['Широта'], row['Долгота']]
    radius = row['0'] * 30  # Предполагается, что столбец с показателем называется 'Показатель'

    folium.CircleMarker(
        location=location,
        radius=radius,
        color='gold',
        fill=True,
        fill_color='blue'
    ).add_to(map)

# Сохранение карты в HTML файл
map.save('map_capita_sum.html')
