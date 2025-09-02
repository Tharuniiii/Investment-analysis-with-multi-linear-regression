
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

dataset = pd.read_csv(r"C:\Users\Tharuni\Desktop\NIT\Aug month\20th-investment analysis\Investment.csv")

x = dataset.iloc[:,:-1]
y = dataset['Profit']

x = pd.get_dummies(x, columns=["State"], drop_first=True, dtype=int)

#split the data

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=0)


regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)# here regressor is model and LinearRegression is algorithm

print("R² Score:", r2_score(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))


#we add 1 as constant for equation because constant c is missing in dataset
#x = np.append(arr = np.ones((50,1)).astype(int), values = x,axis = 1)


filename = 'multilinear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor,file)
print("model has been pickled and saved as multilinear_regression_model.pkl")

print("Full path:", os.path.abspath(filename))