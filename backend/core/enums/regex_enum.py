from enum import Enum


class RegexEnum(Enum):
    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'First letter uppercase, min 2 max 20 ch'
    )

    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[^\w\d\s:])([^\s]){8,16}$',
        [
            'password must contain 1 number (0-9)',
            'password must contain 1 uppercase letters',
            'password must contain 1 lowercase letters',
            'password must contain 1 non-alpha numeric number',
            'password is 8-16 characters with no space'
        ]
    )
    MODEL_CAR = (
        r'^[a-zA-Z0-9\s]{2,49}$',
        'min 2 max 50 symbols'
    )
    INFORMATION = (
        r'^[A-Z][a-zA-Z\s\d]{2,349}$',
        'first letter uppercase min 3 max 350'
    )
    PHONE = (
        r'^(\+38)(\s|-)?(\()?[0-9]{3}(\))?(\s|-)?([0-9]{3})(\s|-)?([0-9]{2})(\s|-)?([0-9]{2})$',
        'Phone must start +380'
    )

    def __init__(self, pattern: str, msg: str|list[str]):
        self.pattern = pattern
        self.msg = msg

