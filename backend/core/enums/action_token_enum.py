from datetime import timedelta
from enum import Enum


class ActionTokenEnum(Enum):
    ACTIVATE = (
        'activate',
        timedelta(hours=2)
    )
    RECOVERY = (
        'recovery',
        timedelta(hours=3)
    )
    SOCKET = (
        'socket',
        timedelta(seconds=60)
    )

    def __init__(self, token_type, life_time):
        self.life_time = life_time
        self.token_type = token_type
