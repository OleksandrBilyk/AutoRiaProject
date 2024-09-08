import os
import uuid
from uuid import uuid1

from core.dataclasses.car_dataclass import CarDataClass


def upload_photo_car(instance: CarDataClass, filename: str) -> str:
    ext = filename.split('.')[-1]
    return os.path.join(instance.user.profile.surname, 'photos', f'{uuid.uuid1()}.{ext}')
