import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
data_day = pd.read_csv('../data/day.csv')

# Create a mapping for the 'weathersit' descriptions
weather_labels = {
    1: 'Clear, Few clouds, Partly cloudy',
    2: 'Mist + Cloudy, Broken clouds',
    3: 'Light Snow, Light Rain + Thunderstorm',
    4: 'Heavy Rain + Ice, Snow + Fog'
}
data_day['weathersit_desc'] = data_day['weathersit'].map(weather_labels)

# Set the style for the plot
sns.set(style="whitegrid")

st.subheader('Question 1: What is the relationship between different weather conditions and the demand for bike rentals?')
# Create the bar plot for weathersit vs bike rentals
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit_desc', y='cnt', data=data_day, palette='coolwarm')
plt.title('Weather Situation vs Bike Rentals')
plt.xlabel('Weather Situation')
plt.ylabel('Total Rentals')
plt.xticks(rotation=15)
st.pyplot(plt)

# Create a mapping for the 'season' descriptions
season_labels = {
    1: 'Spring',
    2: 'Summer',
    3: 'Fall',
    4: 'Winter'
}
data_day['season_desc'] = data_day['season'].map(season_labels)

st.subheader('Question 2: Which season experiences the highest demand for bike rentals, and how can this inform advertising strategies?')
# Create the bar plot for season vs bike rentals
plt.figure(figsize=(8, 6))
sns.barplot(x='season_desc', y='cnt', data=data_day, palette='magma')
plt.title('Bike Rentals by Season')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
st.pyplot(plt)

# Calculate total rentals grouped by season and weather situation
season_weather_data = data_day.groupby(['season', 'weathersit_desc'])['cnt'].sum().reset_index()

# Create the bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='season', y='cnt', hue='weathersit_desc', data=season_weather_data, palette='spring')
plt.title('Total Bike Rentals by Season and Weather Situation')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
plt.legend(title='Weather Situation')
st.pyplot(plt)

st.subheader('Question 3: To what extent do holidays influence the volume of bike rentals compared to regular days?')
# Holiday impact on bike rentals
plt.figure(figsize=(12, 5))
sns.barplot(x='holiday', y='cnt', data=data_day, palette='coolwarm')
plt.title('Bike Rentals on Holidays vs Non-Holidays')
plt.xlabel('Holiday (0 = No, 1 = Yes)')
plt.ylabel('Total Rentals')
st.pyplot(plt)

# Aggregate Rentals by Season
seasonal_rentals = data_day.groupby('season_desc')['cnt'].sum().reset_index()
seasonal_rentals.columns = ['Season', 'Total Rentals']

# Define rentals threshold
high_threshold = seasonal_rentals['Total Rentals'].quantile(0.75)  
low_threshold = seasonal_rentals['Total Rentals'].quantile(0.25) 

st.subheader('Advanced Analysis: Seasonal Clustering of Bike Rentals')
# Visualizing the clusters
plt.figure(figsize=(10, 6))
sns.barplot(x='Season', y='Total Rentals', data=seasonal_rentals, palette='Spectral')
plt.title('Seasonal Clustering of Bike Rentals')
plt.xlabel('Season')
plt.ylabel('Total Rentals')
st.pyplot(plt)

