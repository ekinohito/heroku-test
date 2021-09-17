from enum import Enum, IntEnum

from pydantic import BaseModel


class BrandEnum(str, Enum):
    other = 'other'
    chevrolet = 'chevrolet'
    dodge = 'dodge'
    plymouth = 'plymouth'
    honda = 'honda'
    subaru = 'subaru'
    isuzu = 'isuzu'
    mitsubishi = 'mitsubishi'
    renault = 'renault'
    toyota = 'toyota'
    volkswagen = 'volkswagen'
    nissan = 'nissan'
    mazda = 'mazda'
    saab = 'saab'
    peugeout = 'peugeot'
    alfa_romero = 'alfa-romero'
    mercury = 'mercury'
    audi = 'audi'
    volvo = 'volvo'
    bmw = 'bmw'
    porsche = 'porsche'
    buick = 'buick'
    jaguar = 'jaguar'


class FuelEnum(str, Enum):
    gas = 'gas'
    diesel = 'diesel'


class AspirationEnum(str, Enum):
    std = 'std'
    turbo = 'turbo'


class SymbolEnum(IntEnum):
    very_safe = -2
    moderately_safe = -1
    safe = 0
    neutral = 1
    moderately_risky = 2
    very_risky = 3


class CarBodyEnum(str, Enum):
    sedan = 'sedan'
    hatchback = 'hatchback'
    convertible = 'convertible'
    hardtop = 'hardtop'
    wagon = 'wagon'


class DriveWheelEnum(str, Enum):
    four_wd = '4wd'
    fwd = 'fwd'
    rwd = 'rwd'


class EngineEnum(str, Enum):
    dohc = 'dohc'
    dohcv = 'dohcv'
    l = 'l'
    ohc = 'ohc'
    ohcf = 'ohcf'
    rotor = 'rotor'


class FuelSystemEnum(str, Enum):
    one_bbl = '1bbl'
    two_bbl = '2bbl'
    four_bbl = '4bbl'
    idi = 'idi'
    mfi = 'mfi'
    mpfi = 'mpfi'
    spdi = 'spdi'
    spfi = 'spfi'


class CarModel(BaseModel):
    brand: BrandEnum
    fuel: FuelEnum
    aspiration: AspirationEnum
    car_length: float
    cylinder_count: float
    engine_size: float
    horsepower: float
    peak_rpm: float
    consumption_rate: float
    symbol: SymbolEnum
    car_body_style: CarBodyEnum
    drive_wheel: DriveWheelEnum
    engine: EngineEnum
    fuel_system: FuelSystemEnum


