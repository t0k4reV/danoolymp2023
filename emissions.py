import pandas as pd
import numpy as np

data = pd.read_csv('user_and_orders.csv')

mean = np.mean(data['order_cnt'])
std_dev = np.std(data['order_cnt'])

threshold = 2 * std_dev
lower_bound, upper_bound = mean - threshold, mean + threshold

# Фильтрация данных по границам
filtered_data = data[(data['order_cnt'] >= lower_bound) & (data['order_cnt'] <= upper_bound)]

# Сохранение отфильтрованных данных в файл
filtered_data.to_csv('filtered_user_orders.csv', index=False)
