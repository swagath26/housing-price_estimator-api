import json
import pickle
import numpy as np
import pandas as pd
import os

def get_estimated_price(bathrooms, bedrooms, area, area_type, location):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_directory, 'artifacts/columns.json'), 'r') as f:
        __columns = json.load(f)
        __data_columns = __columns["data_columns"]
    with open(os.path.join(current_directory, 'artifacts/price_estimator_model.pickle'), "rb") as f:
        __model = pickle.load(f)
    x = np.zeros(len(__data_columns))
    for i in range(0, len(x)):
        x[i] = ((__data_columns[i] == location) + area*(__data_columns[i] == area_type) + 
                bathrooms*(__data_columns[i] == "bath") + bedrooms*(__data_columns[i] == "bedrooms")
                + area*(__data_columns[i] == "total_sqft"))
    return 100000*round(__model.predict(pd.DataFrame([x], columns=__data_columns))[0], 2)

def get_location_names():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_directory, 'artifacts/columns.json'), 'r') as f:
        __columns = json.load(f)
    __locations = __columns["location_columns"]
    return __locations

def get_area_type_names():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(current_directory, 'artifacts/columns.json'), 'r') as f:
        __columns = json.load(f)
    __area_type = __columns["area_type_columns"]
    return __area_type