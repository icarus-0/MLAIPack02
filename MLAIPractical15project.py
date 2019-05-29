import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model




def get_data(file_name):
    df = pd.read_csv(file_name)
    print(df)
    x_parameter = []
    y_parameter = []

    for single_square_feet, single_price_value in zip(df['square_feet'], df['price']):
        x_parameter.append([float(single_square_feet)])
        y_parameter.append(float(single_price_value))


    return x_parameter,y_parameter




def liner_madel_main(x_parameter,y_parameter,predict_value) :
    regr = linear_model.LinearRegression()
    print("Area", x_parameter)
    print("price", y_parameter)
    regr.fit(x_parameter, y_parameter)
    predict_outcome = regr.predict([[predict_value]])

    prediction = {}

    prediction['coefficient'] = regr.coef_
    prediction['intercept'] = regr.intercept_
    prediction['prediction_value'] = predict_outcome
    print("output from machine=",predict_outcome)
    plt.scatter(x_parameter, y_parameter, color="m", marker="o", s=30)
    all_predicated_Y = regr.predict(x_parameter)

    plt.scatter(x_parameter, all_predicated_Y, color="b")
    plt.plot(x_parameter,all_predicated_Y,color="r")
    plt.scatter(predict_value,predict_outcome,color="g")

    plt.show()

    return prediction


if __name__=="__main__":
    x,y = get_data('LR_House_price.csv')

    predict_value = 700
    result = liner_madel_main(x,y,predict_value)

    print("intercept value",result['intercept'])
    print("coefficient",result['coefficient'])

    print("preidcted value",result['prediction_value'])













