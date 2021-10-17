from telebot import types

from app.messages import *
from app.enums.user_sex import UserSexEnum
from app.enums.user_state import UserStateEnum


def get_sex_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons = [types.InlineKeyboardButton(text=sex, callback_data=sex) for sex in UserSexEnum]

    keyboard.row(*buttons)
    keyboard.add(BACK_MESSAGE)
    return keyboard


def get_main_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(UserStateEnum.ABOUT)
    keyboard.add(UserStateEnum.SETTINGS)
    return keyboard


def get_settings_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(UserStateEnum.EDIT_NAME)
    keyboard.add(UserStateEnum.EDIT_AGE)
    keyboard.add(UserStateEnum.EDIT_SEX)
    keyboard.add(BACK_MESSAGE)
    return keyboard


def get_back_menu_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(BACK_MESSAGE)
    return keyboard
