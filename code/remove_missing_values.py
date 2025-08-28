import pandas as pd

# Load the CSV file
df = pd.read_csv('base-fitness-trabalho-final/fitness_dataset-working.csv')

# Remove rows where 'sleep_hours' contains '?'
df_cleaned = df[df['sleep_hours'] != '?']

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('base-fitness-trabalho-final/fitness_dataset_working.csv', index=False)