import pickle
import json
import numpy as np
import warnings

__locations = None
__data_columns = None
__model = None

warnings.filterwarnings("ignore")

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("C:/Users/mahir/OneDrive/Documents/GitHub/real-estate-price-prediction/website/artifacts/columns.json", "r") as f:#./artifacts/columns.json"
        __data_columns = json.load(f)['data_columns']
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@", __data_columns)
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('C:/Users/mahir/OneDrive/Documents/GitHub/real-estate-price-prediction/website/artifacts/banglore_home_prices_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")
    return __locations

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

def get_estimated_price(location,sqft,bhk,bath):
    #load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@", __data_columns)

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

#if __name__ == '__main__':
    #load_saved_artifacts()
    # print(get_location_names())
    # print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    # print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    # print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    # print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location