import json
import numpy as np
import pickle

_locations = None
_data_columns = None
_model = None


def get_estimated_price(location, total_sqft, bhk, bath):
    try:
        locindex = _data_columns.index(location.lower())
    except:
        locindex = -1
    x = np.zeros(len(_data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[1] = bhk
    if (locindex >= 0):
        x[locindex] = 1
    return round(_model.predict([x])[0],3)


def get_location_names():
    return _locations


def get_data_columns():
    return _data_columns


def load_artifacts():
    print("loading artifacts")
    global _locations
    global _data_columns
    global _model
    with open("E:/DataScience/ML/Benagaluruhouseprice/model/columns.json", "r") as f:
        _data_columns = json.load(f)['data_columns']
        _locations = _data_columns[3:]
    with open("E:/DataScience/ML/Benagaluruhouseprice/model/bangalore_house.pickle", 'rb') as fk:
        _model = pickle.load(fk)
    print("loaded saved model.....")


if __name__ == '__main__':
    load_artifacts()
    print(get_location_names())
