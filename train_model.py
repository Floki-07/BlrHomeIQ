import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

# Load your CSV file
df = pd.read_csv("Bengaluru_House_Data.csv")

# -------- Data Cleaning --------

# Drop rows with missing target
df.dropna(subset=['price'], inplace=True)

# Drop rows with missing or invalid total_sqft
df = df[df['total_sqft'].notnull()]

# Handle 'size' column → extract BHK number
df['BHK'] = df['size'].apply(lambda x: int(str(x).split(' ')[0]) if isinstance(x, str) and x.split(' ')[0].isdigit() else np.nan)
df.dropna(subset=['BHK'], inplace=True)

# Convert total_sqft ranges like '2100-2850' to average
def convert_sqft(x):
    try:
        tokens = str(x).split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        return float(x)
    except:
        return np.nan

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(subset=['total_sqft'], inplace=True)

# Fill missing balconies with 0
df['balcony'] = df['balcony'].fillna(0)

# Fill missing bath with median
df['bath'] = df['bath'].fillna(df['bath'].median())

# -------- Final Columns --------
features = ['location', 'total_sqft', 'bath', 'balcony', 'BHK']
X = df[features]
y = df['price']

# -------- Pipeline with OneHotEncoder for location --------
categorical = ['location']
numeric = ['total_sqft', 'bath', 'balcony', 'BHK']

preprocessor = ColumnTransformer([
    ('onehot', OneHotEncoder(handle_unknown='ignore'), categorical)
], remainder='passthrough')

pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('model', LinearRegression())
])

# -------- Train-Test Split --------
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# -------- Train --------
pipeline.fit(X_train, y_train)

# -------- Save Model --------
with open("model/model.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ Model trained and saved successfully!")
