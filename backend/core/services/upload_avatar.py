import os
import uuid
from uuid import uuid1

from core.dataclasses.user_dataclass import ProfileDataClass


def upload_avatar(instance: ProfileDataClass, filename: str)->str:
    """
    function for upload avatar foto
    """
    ext = filename.split('.')[-1]
    return os.path.join(instance.surname, 'avatars', f'{uuid.uuid1()}.{ext}')

