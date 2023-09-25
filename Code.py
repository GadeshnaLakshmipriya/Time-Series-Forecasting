# Importing the required libraries
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Read the doctor's visit dataset
df = pd.read_csv('doctors_visit_data.csv')

# Convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Set the date column as the index
df.set_index('date', inplace=True)

# Split the data into training and testing sets
train_data = df[:'2022-12-31']
test_data = df['2023-01-01':]

# Create the ARIMA model
model = ARIMA(train_data, order=(1, 1, 1))
model_fit = model.fit()

# Make predictions on the test data
predictions = model_fit.predict(start=len(train_data), end=len(train_data)+len(test_data)-1)

# Visualize the results
plt.plot(test_data.index, test_data['visits'], label='Actual')
plt.plot(test_data.index, predictions, label='Predicted')
plt.xlabel('Date')
plt.ylabel('Number of Visits')
plt.title("Time Series Forecasting in Doctor's Visit Analysis")
plt.legend()
plt.show()
