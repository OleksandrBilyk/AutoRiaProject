from dataclasses import dataclass
from datetime import datetime

from .user_dataclass import UserDataClass


@dataclass
class CarDataClass:
    id: int
    brand: str
    price: int
    year: int
    car_model: str
    photo_car: str
    information: str
    currency: str
    region: str
    user: UserDataClass
    created_at: datetime
    updated_at: datetime


