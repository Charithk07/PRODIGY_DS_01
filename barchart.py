import pandas as pd
import matplotlib.pyplot as plt

# Loading the csv file which is stored in my local disk d
file_path = 'D:\prodigy_ds_01\Dataset\API_SP.POP.TOTL_DS2_en_csv_v2_315753.csv'
data = pd.read_csv(file_path, skiprows=4)

# Extracting the  population data for the year 2022
year = '2022'
population_2022 = data[['Country Name', year]].dropna()

# Converting the population data to integers for better visualization
population_2022[year] = population_2022[year].astype(int)

#selecting top 10  for the barchart 
top_10_countries = population_2022.sort_values(by=year, ascending=False).head(10)

# Bar Chart
plt.figure(figsize=(12, 8))
plt.bar(top_10_countries['Country Name'], top_10_countries[year], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Population in 2022')
plt.title('Top 10 Most Populous Countries in 2022')
plt.xticks(rotation=45)
plt.show()


