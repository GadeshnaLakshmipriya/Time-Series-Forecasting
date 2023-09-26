import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# reading the dataset using read_csv
df = pd.read_csv("stock_data.csv",
				parse_dates=True,
				index_col="Date")

# displaying the first five rows of dataset
df.head()
# deleting column
df.drop(columns='Unnamed: 0')
df['Volume'].plot()
df.plot(subplots=True, figsize=(4, 4))
# Resampling the time series data based on monthly 'M' frequency
df_month = df.resample("M").mean()

# using subplot
fig, ax = plt.subplots(figsize=(6, 6))

# plotting bar graph
ax.bar(df_month['2016':].index,
	df_month.loc['2016':, "Volume"],
	width=25, align='center')
df.Low.diff(2).plot(figsize=(6, 6))
df.High.diff(2).plot(figsize=(10, 6))
# Finding the trend in the "Open"
# column using moving average method
window_size = 50
rolling_mean = df['Open'].rolling\
			(window_size).mean()
rolling_mean.plot()
df['Change'] = df.Close.div(df.Close.shift())
df['Change'].plot(figsize=(10, 8), fontsize=16)
df['2017']['Change'].plot(figsize=(10, 6))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading the dataset using read_csv
df = pd.read_csv("stock_data.csv", parse_dates=True)
df.drop(columns='Unnamed: 0', inplace=True)

df['Date']= pd.to_datetime(df['Date'])

# extract year from date column
df["Year"] = df["Date"].dt.year

# box plot grouped by year
sns.boxplot(data=df, x="Year", y="Open")
