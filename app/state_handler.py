from app.db.models import User
from app.enums.user_state import UserStateEnum
from app.states import (
    start_state,
    enter_name_state,
    enter_age_state,
    enter_sex_state,
    main_menu_state,
    settings_state,
    edit_name_state,
    edit_age_state,
    edit_sex_state,
)

states = {
    UserStateEnum.START: start_state,
    UserStateEnum.ENTER_NAME: enter_name_state,
    UserStateEnum.ENTER_AGE: enter_age_state,
    UserStateEnum.ENTER_SEX: enter_sex_state,
    UserStateEnum.MAIN_MENU: main_menu_state,
    UserStateEnum.SETTINGS: settings_state,
    UserStateEnum.EDIT_NAME: edit_name_state,
    UserStateEnum.EDIT_AGE: edit_age_state,
    UserStateEnum.EDIT_SEX: edit_sex_state,
}


def get_state_and_process(db, message, user, is_entry=False):
    if user.state not in states:
        user.state = UserStateEnum.START
    state_to_change_name = states[user.state](message, user, is_entry)

    if state_to_change_name:
        go_to_state(db, message, user, state_to_change_name)
        db.commit()


def go_to_state(db, message, user: User, state_name: UserStateEnum):
    user.state = state_name
    get_state_and_process(db, message, user, is_entry=True)
