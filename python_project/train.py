import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Convert categorical columns (e.g., blue, dual_sim, four_g, three_g, touch_screen, wifi) to numerical format using one-hot encoding.
# One-hot encode categorical columns
train_data = pd.get_dummies(train_data, columns=['blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi'])

# Separate features and target variable
X = train_data.drop('price_range', axis=1)
y = train_data['price_range']
# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Exploratory Data Analysis (EDA)
# Pairplot to visualize relationships between features and target variable
sns.pairplot(train_data, hue='price_range')
plt.show()
# Correlation heatmap
correlation_matrix = train_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
