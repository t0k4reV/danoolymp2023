import pandas as pd

# Предположим, что у вас есть DataFrame с колонкой 'Education_level', например:
df = pd.read_csv('only_clients.csv')

# Создание словаря для замены значений
education_mapping = {
    'SCH': 1,
    'GRD': 3,
    'UGR': 2,
    'PGR': 4,
    'ACD': 5
}

# Замена значений в колонке 'Education_level' с помощью метода replace()
df['education_level_num'] = df['education_level'].replace(education_mapping)

# Отображение нового датасета с числовыми значениями уровня образования
df.to_csv('dataset_edlvl.csv', index=False)