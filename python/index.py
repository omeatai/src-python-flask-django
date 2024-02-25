# firstName = "Dave"
# lastName = "Benson"
# age = 42
# ssn = "AE1002345"
# height = "180cm"
# weight = "120kg"

# print(firstName, lastName, age, ssn, height, weight)

import pandas as pd

# Load the trading data from the CSV file
data = pd.read_csv('1min_SPY.csv')

# Initialize variables
buy_price = 0
profit = 0
max_drawdown = 0
max_profit = 0

# Iterate over each row in the trading data
for index, row in data.iterrows():
    current_price = row['close']

    # Rule 6: If there is no buys, buy a contract
    if buy_price == 0:
        buy_price = current_price
        continue

    # Rule 4: If the price goes up 0.2% after a buy, sell the contract for a profit
    if current_price >= buy_price * 1.02:
        profit += current_price - buy_price
        if profit > max_profit:
            max_profit = profit
        buy_price = 0
    # Rule 5: If the price goes 0.2% below the previous buy price, buy another contract
    elif current_price <= buy_price * 0.98:
        profit -= buy_price - current_price
        if profit < max_drawdown:
            max_drawdown = profit
        buy_price = current_price

    # Rule 3: If the buy on Call expires after 7 days, lose the amount used to buy the contract
    # We assume each row represents 1 minute, so 7 days is 7 * 24 * 60 minutes
    if index % (7 * 24 * 60) == 0:
        if buy_price != 0:
            profit -= buy_price
            buy_price = 0

# Calculate total profit
total_profit = profit

print("Total profit:", total_profit)
print("Maximum drawdown:", max_drawdown)
