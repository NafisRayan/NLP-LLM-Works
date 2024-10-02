import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('Housing Price.csv')
print("Initial shape:", df.shape)
df.head()

# 1. Handling Missing Values
print("\nMissing values per column:")
print(df.isnull().sum())

df = df.dropna()
print("\nAfter removing rows with null values:", df.shape)

# 2. Removing Duplicate Rows
print("\nNumber of duplicate rows before dropping:", df.duplicated().sum())
df = df.drop_duplicates()
print("After removing duplicates:", df.shape)

# 3. Handling Categorical Variables
binary_cols = ['mainroad', 'guestroom', 'basement', 'hotwaterheating', 'airconditioning', 'prefarea']

df = pd.get_dummies(df, columns=binary_cols, drop_first=True)
print("\nAfter encoding binary columns:", df.shape)

label_encoder = LabelEncoder()
df['furnishingstatus'] = label_encoder.fit_transform(df['furnishingstatus'])
print("Unique values for 'furnishingstatus' after Label Encoding:", df['furnishingstatus'].unique())
df.head()

# 4. Feature Scaling
scaler = StandardScaler()
numerical_cols = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking']

df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
print("\nAfter scaling numerical columns:", df.shape)
df.head()

# 5. Feature Selection using Correlation
corr_matrix = df.corr().abs()

upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))


to_drop = []
for column in upper.columns:
  if any(upper[column] > 0.5):
    to_drop.append(column)

print("Columns to be dropped (high correlation):", to_drop)

df = df.drop(columns=to_drop)
print("\nAfter dropping highly correlated columns:", df.shape)

df.to_csv('preprocessed_house_price.csv', index=False)
print("Final dataset saved as 'preprocessed_house_price.csv'")
df.head()