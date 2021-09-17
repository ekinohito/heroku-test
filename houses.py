from catboost import CatBoostRegressor
import pandas as pd


def houses_predict(bedrooms, bathrooms, living_square, total_square, floors, yr_built, yr_renovated):
    model = CatBoostRegressor()
    model.load_model('houses_model')
    data = {
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'living_square': [living_square],
        'total_square': [total_square],
        'floors': [floors],
        'yr_built': [yr_built],
        'yr_renovated': [yr_renovated]
    }
    df = pd.DataFrame(data)
    return model.predict(df)[0]
