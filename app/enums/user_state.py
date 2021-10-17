from app.enums.base import EnumBase


class UserStateEnum(EnumBase):
    START = 'START'

    ENTER_NAME = 'ENTER_NAME'
    ENTER_AGE = 'ENTER_AGE'
    ENTER_SEX = 'ENTER_SEX'

    MAIN_MENU = 'MAIN_MENU'
    ABOUT = 'ABOUT'
    SETTINGS = 'SETTINGS'

    EDIT_NAME = 'EDIT_NAME'
    EDIT_AGE = 'EDIT_AGE'
    EDIT_SEX = 'EDIT_SEX'
