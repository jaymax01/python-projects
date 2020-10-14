# Reading the dataset
import pandas as pd
from datetime import datetime

stock_data = pd.read_csv('sphist.csv')
print(stock_data.head(3))

# Converting the Date column to date type
stock_data['Date'] = pd.to_datetime(stock_data['Date'])
print(stock_data.info())

# Performing date comparisons
date_data = stock_data['Date'] > datetime(year = 2015, month = 4, day = 1)
print(date_data.head(3))

# Sorting the data by the Date column
stock_data = stock_data.sort_values(by = 'Date', ascending = True)
print(stock_data.head(5))

# Calculating 3 indicators for each row of the stock market date
# min_index = 0
# min_index_1 = 0

# for row in stock_data.iterrows():
#     # if (row[0] - 5) <= 0:
#     #     min_index = 0
#     # else:
#     #     min_index = row[0] - 5
#     prev_five = stock_data['Close'].iloc[0:row[0]]
    
# #     if (row[0] - 365) <= 0:
# #         min_index_1 = 0
# #     else:
# #         min_index_1 = row[0] - 365
#     dev_prev_365 = stock_data['Close'].iloc[0:row[0]].std()
    
    # stock_data['Avg_day_5'] = prev_five.mean()
    # stock_data['Sdev_day_5'] = prev_five.std()
    # stock_data['Ratio_past5_365'] = stock_data['Avg_day_5']/dev_prev_365
    
# Calculating 3 indicators for each row of the stock market date
stock_data['Avg_day_5'] = stock_data['Close'].rolling(window = 5, min_periods = 2).mean()
stock_data['Sdev_day_5'] = stock_data['Close'].rolling(window = 5, min_periods = 2).std()
dev_prev_365 = stock_data['Close'].rolling(window = 365, min_periods = 2).std()
stock_data['Ratio_past5_365'] = stock_data['Avg_day_5'] / dev_prev_365

# Shifting the indexes of the dataframe by 1 period
stock_data.shift()
print(stock_data.head(10)) 
print(stock_data.tail(10)) 

# Removing rows from the dataset with dates before 1951-10-03
stock_data = stock_data[stock_data['Date'] > datetime(year = 1951, month = 1, day = 2)]
print(stock_data.head(5))

# Removing NAN values from the dataset
stock_data = stock_data.dropna(axis=0)
print(pd.isnull(stock_data).sum())

# Splitting the dataset into train and test data
train = stock_data[stock_data['Date'] < datetime(year = 2013, month = 1, day = 1)]
test = stock_data[stock_data['Date'] > datetime(year = 2013, month = 1, day = 1)]
print(train.tail(3))
print(test.head(3))

# Training a linear regression model to predict the Close stock prices
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

linear_model = LinearRegression()
model_fit = linear_model.fit(train[['Avg_day_5', 'Sdev_day_5', 'Ratio_past5_365']], train['Close'])
predict_train = model_fit.predict(train[['Avg_day_5', 'Sdev_day_5', 'Ratio_past5_365']])
predict_test = model_fit.predict(test[['Avg_day_5', 'Sdev_day_5', 'Ratio_past5_365']])
mean_absolute_error_train = mean_absolute_error(train['Close'], predict_train)

mean_absolute_error_test = mean_absolute_error(test['Close'], predict_test)

# Mean absolute error for the predicted values
print(mean_absolute_error_train)
print(mean_absolute_error_test)    
    