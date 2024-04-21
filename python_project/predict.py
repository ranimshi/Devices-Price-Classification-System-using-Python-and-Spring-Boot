import pandas as pd
from sklearn.preprocessing import StandardScaler

# import the execl file
train_data = pd.read_csv('C:/Users/shmai/Downloads/train.csv')
test_data = pd.read_csv('C:/Users/shmai/Downloads/test.csv')
print(train_data.head())
# Get a summary of the training data
print(train_data.info())

# Statistical summary of the numerical columns
print(train_data.describe())
# Check if there are missing value as null
print(train_data.isnull().sum())
# Filling missing values with the mean of the column
train_data.fillna(train_data.mean(), inplace=True)
print(train_data.isnull().sum())


# Scale numerical features to the same range using methods like Min-Max scaling or standardization.
# Standardize the numerical features
scaler = StandardScaler()
numerical_columns = ['battery_power', 'clock_speed', 'fc', 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height', 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time']
train_data[numerical_columns] = scaler.fit_transform(train_data[numerical_columns])
print(train_data.head())
