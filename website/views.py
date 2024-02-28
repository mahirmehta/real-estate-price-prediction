from flask import Blueprint, render_template, request, flash, jsonify
from os import path
from flask import Flask, request, jsonify

import website.util as util
import numpy as np
import warnings
from website.util import load_saved_artifacts

views = Blueprint('views', __name__)



# __locations = None
# __data_columns = None
# __model = None

# warnings.filterwarnings("ignore")

# def load_saved_artifacts():
#     print("loading saved artifacts...start")
#     global  __data_columns
#     global __locations

#     with open("./artifacts/columns.json", "r") as f:
#         __data_columns = json.load(f)['data_columns']
#         __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

#     global __model
#     if __model is None:
#         with open('./artifacts/banglore_home_prices_model.pickle', 'rb') as f:
#             __model = pickle.load(f)
#     print("loading saved artifacts...done")

# def get_location_names():
#     return __locations

# def get_data_columns():
#     return __data_columns

# def get_estimated_price(location,sqft,bhk,bath):
#     try:
#         loc_index = __data_columns.index(location.lower())
#     except:
#         loc_index = -1

#     x = np.zeros(len(__data_columns))
#     x[0] = sqft
#     x[1] = bath
#     x[2] = bhk
#     if loc_index>=0:
#         x[loc_index] = 1

#     return round(__model.predict([x])[0],2)

# if __name__ == '__main__':
#     load_saved_artifacts()
#     print(get_location_names())
#     print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
#     print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
#     print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
#     print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location


@views.route('/', methods=['GET', 'POST'])
def get_location_names():
    response = jsonify({"locations": util.get_location_names()}) #util.get_location_names()}
    response.headers.add("Access-Control-Allow-Origin", "*")
    print(response)
    new_res = load_saved_artifacts()
    #return response

    return render_template("app.html", response=new_res)

@views.route('/get_location_names', methods=['GET', 'POST'])
def get_location_names_1():
    response = jsonify({"locations": util.get_location_names()}) #util.get_location_names()}
    response.headers.add("Access-Control-Allow-Origin", "*")
    print(response)
    #return response

    return render_template("app.html", response=response)

@views.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk = int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify(
        {"estimated_price": util.get_estimated_price(location,total_sqft,bhk,bath)}
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

    ##util.get_estimated_price(location,total_sqft,bhk,bath)}