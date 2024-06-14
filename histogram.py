import pandas as pd
import matplotlib.pyplot as plt

# Loading the CSV file which is stored in local disk d
file_path = 'D:\prodigy_ds_01\Dataset\API_SP.POP.TOTL_DS2_en_csv_v2_315753.csv'
data = pd.read_csv(file_path, skiprows=4)

# Extracting the  population data for the year 2022
year = '2022'
population_2022 = data[['Country Name', year]].dropna()

# Converting  the population data to integers for better visualization
population_2022[year] = population_2022[year].astype(int)


# Histogram
plt.figure(figsize=(12, 8))
plt.hist(population_2022[year], bins=30, color='lightgreen', edgecolor='black')
plt.xlabel('Population in 2022')
plt.ylabel('Number of Countries')
plt.title('Distribution of Population Sizes Across Countries in 2022')
plt.show()
