from pydantic import BaseModel


class HouseModel(BaseModel):
    house_bedrooms: float
    house_bathrooms: float
    house_area_living: float
    house_area_total: float
    house_story: float
    house_year_built: float
    house_year_renovated: float
