from app.validator import is_valid_name, is_valid_age, is_valid_sex
from app.enums.user_state import UserStateEnum
from app.keyboards import (
    get_sex_keyboard,
    get_main_menu_keyboard,
    get_settings_keyboard,
    get_back_menu_keyboard,
)
from app.messages import *
from app.bot import bot


def start_state(message, user, is_entry=False):
    bot.send_message(message.chat.id, START_MESSAGE, reply_markup=None)
    return UserStateEnum.ENTER_NAME


def enter_name_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id, ENTER_NAME_MESSAGE, reply_markup=None)
    else:
        if is_valid_name(message.text):
            user.name = message.text
            return UserStateEnum.ENTER_AGE
        else:
            bot.send_message(message.chat.id, INVALID_NAME_MESSAGE)


def enter_age_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, ENTER_AGE_MESSAGE, reply_markup=get_back_menu_keyboard()
        )
    else:
        if message.text == BACK_MESSAGE:
            return UserStateEnum.ENTER_NAME
        elif is_valid_age(message.text):
            user.age = int(message.text)
            return UserStateEnum.ENTER_SEX
        else:
            bot.send_message(message.chat.id, INVALID_AGE_MESSAGE)


def enter_sex_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id, ENTER_SEX_MESSAGE, reply_markup=get_sex_keyboard())
    else:
        if message.text == BACK_MESSAGE:
            return UserStateEnum.ENTER_AGE
        if is_valid_sex(message.text):
            user.sex = message.text
            return UserStateEnum.MAIN_MENU
        else:
            bot.send_message(message.chat.id, INVALID_SEX_MESSAGE)


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, MAIN_MENU_MESSAGE, reply_markup=get_main_menu_keyboard()
        )
    else:
        if message.text == UserStateEnum.SETTINGS:
            return UserStateEnum.SETTINGS
        elif message.text == UserStateEnum.ABOUT:
            bot.send_message(message.chat.id, f'{user.name} | {user.age} | {user.sex}')


def settings_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, SETTINGS_MESSAGE, reply_markup=get_settings_keyboard()
        )
    else:
        commands = [UserStateEnum.EDIT_NAME, UserStateEnum.EDIT_AGE, UserStateEnum.EDIT_SEX]
        if message.text == BACK_MESSAGE:
            return UserStateEnum.MAIN_MENU
        elif message.text in commands:
            return UserStateEnum(message.text)


def edit_name_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, ENTER_NAME_MESSAGE, reply_markup=get_back_menu_keyboard()
        )
    else:
        if is_valid_name(message.text):
            user.name = message.text
            return UserStateEnum.SETTINGS
        else:
            bot.send_message(message.chat.id, INVALID_NAME_MESSAGE)


def edit_age_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(
            message.chat.id, ENTER_AGE_MESSAGE, reply_markup=get_back_menu_keyboard()
        )
    else:
        if message.text == BACK_MESSAGE:
            return UserStateEnum.SETTINGS
        elif is_valid_age(message.text):
            user.age = int(message.text)
            return UserStateEnum.SETTINGS
        else:
            bot.send_message(message.chat.id, INVALID_AGE_MESSAGE)


def edit_sex_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id, ENTER_SEX_MESSAGE, reply_markup=get_sex_keyboard())
    else:
        if message.text == BACK_MESSAGE:
            return UserStateEnum.SETTINGS
        elif is_valid_sex(message.text):
            user.sex = message.text
            return UserStateEnum.SETTINGS
        else:
            bot.send_message(message.chat.id, INVALID_SEX_MESSAGE)
