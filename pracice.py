import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('disney_plus_titles.csv')
film_year = pd.DataFrame(data['release_year'].value_counts().reset_index().values, columns=['Year', 'amount'])
film_year = film_year.sort_values('Year', ascending=True)
print(film_year)
plt.plot(film_year['Year'], film_year['amount'])
plt.show()

