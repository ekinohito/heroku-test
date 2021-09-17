from enum import Enum
from typing import Optional, List

from pydantic import BaseModel


class MaterialEnum(str, Enum):
    unset = "unset"
    brick = "brick"
    wood = "wood"
    monolith = "monolith"
    panel = "panel"
    block = "block"
    brick_monolith = "monolithBrick"
    stalin = "stalin"


class Coordinates(BaseModel):
    lon: float
    lat: float


class Address(BaseModel):
    label: str
    coords: Coordinates


class EstateModel(BaseModel):
    rooms: float
    floor: float
    material: MaterialEnum
    story: float
    area_total: float
    area_living: float
    address: Address
    year: float
    area_kitchen: float


class ResultModel(BaseModel):
    text: str
    uri: Optional[str]


class YModel(BaseModel):
    part: str
    results: List[ResultModel]
