import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data
X_full = pd.read_csv("./data/train.csv", index_col="Id")
X_test_full = pd.read_csv("./data/test.csv", index_col="Id")

# Obtain target and predictors
y = X_full.SalePrice
features = [
    "LotArea",
    "YearBuilt",
    "1stFlrSF",
    "2ndFlrSF",
    "FullBath",
    "BedroomAbvGr",
    "TotRmsAbvGrd",
]

X = X_full[features].copy()
X_test = X_test_full[features].copy()

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, train_size=0.8, test_size=0.2, random_state=42
)
