from sklearn.ensemble import RandomForestClassifier

# Fit a model
model = RandomForestClassifier()
model.fit(X, y)

# Get feature importances
feature_importances = model.feature_importances_
from sklearn.feature_selection import RFE

# Create an estimator (e.g., a classifier or regressor)
estimator = RandomForestClassifier()

# Create the RFE model and select the number of features to keep
rfe = RFE(estimator, n_features_to_select=5)
rfe.fit(X, y)
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# Select the top k features
k = 5
X_new = SelectKBest(chi2, k=k).fit_transform(X, y)
import pandas as pd

df = pd.get_dummies(df, columns=['categorical_column'])
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
df['categorical_column'] = le.fit_transform(df['categorical_column'])
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df['numerical_column'] = scaler.fit_transform(df['numerical_column'].values.reshape(-1, 1))
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
df['numerical_column'] = scaler.fit_transform(df['numerical_column'].values.reshape(-1, 1))
