import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('danogames.csv')

revenuegroups = data.groupby('group')['revenue_per_user'].sum().reset_index()
print(revenuegroups)
order_group = data.groupby('group')['orders_cnt_per_user'].sum().reset_index()
print(order_group,'\n....')
cardscreen = data.groupby('group')['converted_from_main_screen_to_item_card_screen'].sum().reset_index()
print(cardscreen, '\n....')
a = data[data['group'] == "A"]
print('a\n', a.groupby('period')['revenue_per_user'].sum().reset_index())
b = data[data['group'] == "B"]
print('b\n', b.groupby('period')['revenue_per_user'].sum().reset_index())
print('a\n', a.groupby('period')['orders_cnt_per_user'].sum().reset_index())
print('b\n', b.groupby('period')['orders_cnt_per_user'].sum().reset_index())
print('a\n', a.groupby('period')['converted_from_main_screen_to_item_card_screen'].sum().reset_index())
print('b\n', b.groupby('period')['converted_from_main_screen_to_item_card_screen'].sum().reset_index())
print(data.groupby('group').count())


