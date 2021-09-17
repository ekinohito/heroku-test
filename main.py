import aiohttp
from aiohttp import ClientError
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from apartments import apartments_predict
from apartments_models import EstateModel, YModel
from cars_models import CarModel
from geo import get_distance, get_azimuth
from houses import houses_predict
from houses_models import HouseModel
from сars import cars_predict

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/estate")
def read_estate(params: EstateModel):
    prediction = apartments_predict(
        walls_material=params.material,
        floor_number=params.floor,
        floors_total=params.story,
        total_area=params.area_total,
        kitchen_area=params.area_kitchen,
        distance=get_distance(latitude=params.address.coords.lat, longitude=params.address.coords.lon),
        azimuth=get_azimuth(latitude=params.address.coords.lat, longitude=params.address.coords.lon))
    return {"prediction": prediction}


@app.post("/car")
def read_car(params: CarModel):
    try:
        prediction = cars_predict(
            brand=params.brand,
            fuel=params.fuel,
            asp=params.aspiration,
            carlen=params.car_length,
            cnum=params.cylinder_count,
            esz=params.engine_size * 100,
            hpw=params.horsepower,
            peakrpm=params.peak_rpm,
            hwmpg=235.21 / params.consumption_rate,
            symb=params.symbol,
            cbd=params.car_body_style,
            dvw=params.drive_wheel,
            et=params.engine,
            fs=params.fuel_system
        )
        print(prediction)
        return {"prediction": prediction[0] * 72}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Consumption rate cannot be zero")


@app.post("/house")
def read_car(params: HouseModel):
    prediction = houses_predict(
        bedrooms=params.house_bedrooms,
        bathrooms=params.house_bathrooms,
        living_square=params.house_area_living,
        total_square=params.house_area_total,
        floors=params.house_story,
        yr_built=params.house_year_built,
        yr_renovated=params.house_year_renovated
    )
    return {"prediction": prediction}


@app.get("/y-proxy", response_model=YModel)
async def get_suggestions(part: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('https://suggest-maps.yandex.com/suggest-geo', params={
                "fullpath": 1,
                "lang": "ru_RU",
                "outformat": "json",
                "v": 9,
                "part": "Москва, " + part
            }) as resp:
                return await resp.json()
        except ClientError:
            raise HTTPException(status_code=400, detail="Problems...")
    pass
