import os

input_path = os.path.normpath(os.path.join(__file__, "..", "input.txt"))
# Includes each ticker number in the input file as an integer
data = []

with open(input_path) as file:
    for line in file.read().strip().split("\n"):
        line = int(line)

        # A 0 indicates the end of input, so stop reading input. Otherwise, 
        # add the ticker number to data
        if line == 0:
            break

        data.append(line)

# Each key is the ticker number and each value is the number of times the 
# ticker number appears in the input
ticker_counts = {}

# Count the number of appearances of each ticker number in the data
for ticker_number in data:
    if ticker_number in ticker_counts.keys():
        ticker_counts[ticker_number] += 1
    else:
        ticker_counts[ticker_number] = 1

# Contains ticker numbers sorted in descending order by the ticker count
top_tickers = []

for _ in range(2):
    # The ticker number with the highest count that is in ticker_counts but 
    # is not in top_tickers
    top_ticker = 0

    # Determine the ticker with the highest count that is not in top_tickers
    for ticker_number, ticker_count in ticker_counts.items():
        if ticker_number in top_tickers:
            continue

        if top_ticker == 0 or ticker_count > ticker_counts[top_ticker]:
            top_ticker = ticker_number
    
    top_tickers.append(top_ticker)

print(f"Trending: {top_tickers[0]} [{ticker_counts[top_tickers[0]]} count]")
print(f"Second Place: {top_tickers[1]} "
      + f"[{ticker_counts[top_tickers[1]]} count]")