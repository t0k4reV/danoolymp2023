import pandas as pd

# Загрузка данных из CSV файла с пользователями
users_data = pd.read_csv('../sources/T_games_dataset.csv')
cities_parameters = pd.read_csv('../parameters/cities_parameters.csv')

# Создание словаря для хранения данных о численности населения городов
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

# Добавление столбца с численностью населения в файл с пользователями
# users_data['city_population'] = users_data['city_nm'].map(population_data)
cities_parameters['city_population '] = cities_parameters['city_nm'].map(population_data)

# Сохранение результата в новый файл CSV
# users_data.to_csv('dataset.csv', index=False)
cities_parameters.to_csv('cities_pop.csv', index=False)

