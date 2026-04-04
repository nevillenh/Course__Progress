import pandas as pd
data = [10, 20, 30]
series = pd.Series(data)

print(series)

data = {
    "Name": ["John", "Jane", "Mike"],
    "Age": [23, 25, 22]
}

df = pd.DataFrame(data)

print(df)

import pandas as pd

data = {
    "Product": ["Phone", "Laptop", "Tablet"],
    "Price": [300, 800, 200]
}

df = pd.DataFrame(data)

# Find expensive products
expensive = df[df["Price"] > 250]

print(expensive)


# Load a dataset
df = pd.read_csv("teslastockdata.csv")

# Show first rows
print(df.head())
# Show summary statistics
print(df.describe())
# Show column names
print(df.columns)   

print(df.columns)   # column names
print(df.info())    # structure
print(df.describe()) # statistics

#Filter data (e.g., high price days)
high_prices = df[df["Close"] > 150]
print(high_prices)

# Group by month and calculate average closing price
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month
monthly_avg = df.groupby("Month")["Close"].mean()
print(monthly_avg)

# Sort data
sorted_df = df.sort_values(by="Close", ascending=False)
print(sorted_df.head())

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

import matplotlib.pyplot as plt

df["Close"].plot()
plt.title("Tesla Stock Closing Price")
plt.show()
 
     # SOME GRAPHICAL ANALYSIS
# Convert Date column to datetime and sort by date
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(by="Date")
# highest and lowest closing price
print("Highest Price:", df["Close"].max())
print("Lowest Price:", df["Close"].min())
# average closing price
print("Average Close:", df["Close"].mean())
# daily returns
df["Daily Return"] = df["Close"].pct_change()
print(df[["Date", "Close", "Daily Return"]].head())