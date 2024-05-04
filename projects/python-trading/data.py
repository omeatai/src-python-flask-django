import pytz  # Import the pytz library
from datetime import datetime
import json
import requests
import pandas as pd
api_connect = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=TkqXt2_BgGf2ITwYsreiU3xIXj2WZgPr"

api_key = "TkqXt2_BgGf2ITwYsreiU3xIXj2WZgPr"
symbol = "SPY"
start_date = "2024-01-17"
end_date = "2024-01-20"
candle = "1"
timeframe = "hour"

url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/range/{candle}/{
    timeframe}/{start_date}/{end_date}?apiKey={api_key}"

# response = requests.get(url)
# data = response.json()
# print(data)
# Process the data as needed


# Load JSON data
# with open('data.json', 'r') as json_file:
#     data = json_file.read()

# # Convert JSON to DataFrame
# df = pd.read_json(data)

# # Convert DataFrame to CSV
# df.to_csv('data.csv', index=False)

###############################################################
###############################################################
###############################################################
###############################################################


# # Define the time zone for Lethbridge, Alberta
# lethbridge_tz = pytz.timezone('America/Edmonton')

# # Load data from CSV
# data = pd.read_csv('data.csv')

# # Function to extract the 'c' (close price) from the JSON-like string in 'results'


# def extract_close_price(results):
#     results_json = json.loads(results.replace("'", '"'))
#     return results_json['c']

# # Function to extract and convert the timestamp to Lethbridge date and time


# def extract_lethbridge_date_time(results):
#     results_json = json.loads(results.replace("'", '"'))
#     # The provided timestamp is in milliseconds
#     timestamp = results_json['t'] / 1000
#     utc_dt = datetime.utcfromtimestamp(timestamp).replace(tzinfo=pytz.utc)
#     lethbridge_dt = utc_dt.astimezone(lethbridge_tz)
#     return lethbridge_dt.strftime('%d-%m-%Y'), lethbridge_dt.strftime('%-I:%M%p')


# # Extract the close price
# data['close_price'] = data['results'].apply(extract_close_price)

# # Extract the Lethbridge date and time and assign to new columns
# data[['date', 'time']] = pd.DataFrame(data['results'].apply(
#     extract_lethbridge_date_time).tolist(), index=data.index)

# # Initialize a list to keep track of the comparison result
# comparison_results = []
# result_column = []

# # Loop through the DataFrame and compare close prices
# previous_close_price = None
# for index, row in data.iterrows():
#     current_close_price = row['close_price']
#     if previous_close_price is not None:
#         if current_close_price > previous_close_price:
#             comparison = "Above previous candle"
#             result = 1
#         else:
#             comparison = "Below previous candle"
#             result = 0
#     else:
#         comparison = "No previous candle"
#         result = None
#     comparison_results.append(comparison)
#     result_column.append(result)
#     previous_close_price = current_close_price

# # Add the comparison result to the DataFrame as a new column
# data['comparison_to_prev_close'] = comparison_results
# data['result'] = result_column

# # Select and reorder columns for the output
# output_data = data[['date', 'time', 'close_price',
#                     'comparison_to_prev_close', 'result']]

# # Print the result
# print(output_data)

# # Save to a new CSV file
# output_data.to_csv('analyzed_data_lethbridge.csv', index=False)


###############################################################
###############################################################
###############################################################
###############################################################

# Load the previously saved 'analyzed_data_lethbridge.csv' into a DataFrame
# data = pd.read_csv('analyzed_data_lethbridge.csv')

# # Round the 'result' column and convert to integer for concatenation
# data['result'] = data['result'].fillna(0).astype(int)

# # Group by 'date' and concatenate the 'result' values into a single string per date
# patterns = data.groupby('date')['result'].apply(
#     lambda x: ''.join(x.astype(str)))

# # Create a new DataFrame with 'date' and 'pattern' columns
# output_df = patterns.reset_index(name='pattern')

# # Print the result
# print(output_df)

# # Save the new DataFrame to 'output.csv'
# output_df.to_csv('output.csv', index=False)

###############################################################
###############################################################
###############################################################
###############################################################

# Load the 'output.csv' into a DataFrame
data = pd.read_csv('output.csv')

# Ensuring all patterns are 16 characters long, padding with leading zeros if necessary
data['pattern'] = data['pattern'].apply(lambda x: str(x).zfill(16))


def search_pattern(search_string):
    # Check if patterns start with the search string
    data['occurrence'] = data['pattern'].apply(
        lambda x: x.startswith(search_string)).astype(int)

    # Filter data to only rows with at least one occurrence (when the pattern starts with the search string)
    results = data[data['occurrence'] > 0]

    # Print results
    for index, row in results.iterrows():
        print(f"{row['date']},{row['pattern']
                               } (occurrence: {row['occurrence']})")

    return results


# Replace '111101' with the string you would like to search for
search_string = "1"
search_results = search_pattern(search_string)

# Optional: Save the search results to a CSV file
# search_results.to_csv('search_results.csv', index=False)
