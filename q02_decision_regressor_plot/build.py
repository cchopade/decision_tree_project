# default imports
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("./data/house_pricing.csv")
X = data.iloc[:, :-1]
y = data.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

depth_list = [2, 8, 10, 15, 20, 25, 30, 35, 45, 50, 80]
def decision_regressor_plot(X_train, X_test,y_train, y_test, depths):

    mse_train = []
    mse_test = []

    for d in depths:
        clf = DecisionTreeRegressor(random_state = 9, max_depth = d)
        clf.fit(X_train, y_train)
        mse_test.append(mean_squared_error(y_test, clf.predict(X_test)))
        mse_train.append(mean_squared_error(y_train, clf.predict(X_train)))


    fig, ax = plt.subplots()
    ax.plot(depths, mse_train, label = 'Train Set')
    ax.plot(depths, mse_test, label = 'Test Set')
    ax.legend()
    plt.xlabel('Depth')
    plt.ylabel('MSE')
# Write your solution here :
