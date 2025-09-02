import pandas as pd

# Read the CSV file
df = pd.read_csv('boatos-br-corpus/boatos_br_processada_working.csv')

# Function to convert seconds to milliseconds
def convert_to_ms(timestamp):
    # Convert to string to check length
    ts_str = str(timestamp)
    # If it's a 10-digit timestamp (seconds), multiply by 1000
    if len(ts_str) == 12:
        return timestamp * 10
    return timestamp

# Apply the conversion to the 'data-publicacao' column
df['data-publicacao'] = df['data-publicacao'].apply(convert_to_ms)

# Save the cleaned DataFrame
df.to_csv('boatos-br-corpus/boatos_br_processada_working.csv', index=False)