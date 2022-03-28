import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def salary_model(years):
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
  
    y_pred = regressor.predict([[years]])
    return (f"${round(y_pred[0])} per year")
