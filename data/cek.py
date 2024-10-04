import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_day = pd.read_csv('data/day.csv')
data_day.head(15)

print("Checking if there's missing value on data_day: ")
data_day.isnull().sum()

# Check the type of the data
data_types = data_day.dtypes
print("\nData Types:\n", data_types)

# Convert 'dteday' to Datetime
data_day['dteday'] = pd.to_datetime(data_day['dteday'])
print("Data Types after conversion:\n", data_day.dtypes)

# Display summary statistics
data_day.describe()
# Create a mapping for the 'weathersit' descriptions
weather_labels = {
    1: 'Clear, Few clouds, Partly cloudy',
    2: 'Mist + Cloudy, Broken clouds',
    3: 'Light Snow, Light Rain + Thunderstorm',
    4: 'Heavy Rain + Ice, Snow + Fog'
}

# Map the weathersit column to these labels
data_day['weathersit_desc'] = data_day['weathersit'].map(weather_labels)

# Set the style for the plot
sns.set(style="whitegrid")

# Create the bar plot for weathersit vs bike rentals
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit_desc', y='cnt', data=data_day, palette='coolwarm')

# Add labels and title
plt.title('Weather Situation vs Bike Rentals')
plt.xlabel('Weather Situation')
plt.ylabel('Total Rentals')

# Rotate x labels for better readability
plt.xticks(rotation=15)

# Display the plot
plt.show()

# Create a mapping for the 'season' descriptions
season_labels = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}

# Map the season column to these labels
data_day['season_desc'] = data_day['season'].map(season_labels)

# Set the style for the plot
sns.set(style="whitegrid")

# Create the bar plot for season vs bike rentals
plt.figure(figsize=(8, 6))
sns.barplot(x='season_desc', y='cnt', data=data_day, palette='magma')

# Add labels and title
plt.title('Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Total Rentals')

# Display the plot
plt.show()

# Set the style for the plot
sns.set(style="whitegrid")

# Calculate total rentals grouped by season and weather situation
season_weather_data = data_day.groupby(['season', 'weathersit_desc'])['cnt'].sum().reset_index()

# Create the bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='cnt', hue='weathersit_desc', data=season_weather_data, palette='spring')

# Add labels and title
plt.title('Total Bike Rentals by Season and Weather Situation')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
plt.legend(title='Weather Situation')

# Display the plot
plt.show()
# Set plot style
sns.set(style="whitegrid")

# Step 2: Holiday impact on bike rentals
plt.figure(figsize=(12, 5))

# Holiday vs Non-holiday
plt.subplot(1, 2, 1)
sns.barplot(x='holiday', y='cnt', data=data_day, palette='coolwarm')
plt.title('Bike Rentals on Holidays vs Non-Holidays')
plt.xlabel('Holiday (0 = No, 1 = Yes)')
plt.ylabel('Total Rentals')


#Aggregate Rentals by Season
seasonal_rentals = data_day.groupby('season_desc')['cnt'].sum().reset_index()
seasonal_rentals.columns = ['Season', 'Total Rentals']

#Define rentals treshold
high_threshold = seasonal_rentals['Total Rentals'].quantile(0.75)  
low_threshold = seasonal_rentals['Total Rentals'].quantile(0.25) 

#Visualizing the clusters
plt.figure(figsize=(10, 6))  # Optional: Set figure size
sns.barplot(x='Season', y='Total Rentals', hue='Rental Category', data=seasonal_rentals, palette='Spectral')
plt.title('Seasonal Clustering of Bike Rentals')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
plt.legend(title='Rental Category')
plt.show()
