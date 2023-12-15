import pandas as pd

data = pd.read_csv('dataset.csv')

unique_rows_total = len(data.drop_duplicates())
print("Общее количество уникальных строк в DataFrame:", unique_rows_total)
