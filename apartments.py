from catboost import CatBoostRegressor
import pandas as pd


def apartments_predict(walls_material, floor_number, floors_total, total_area,
                       kitchen_area, distance, azimuth) -> float:
    model = CatBoostRegressor()
    model.load_model('apartments_model')
    data = {
        'wallsMaterial': [walls_material],
        'floorNumber': [floor_number],
        'floorsTotal': [floors_total],
        'totalArea': [total_area],
        'kitchenArea': [kitchen_area],
        'distance': [distance],
        'azimuth': [azimuth]
    }
    df = pd.DataFrame(data)
    return model.predict(df)[0]
