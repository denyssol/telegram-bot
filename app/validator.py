from app.enums.user_sex import UserSexEnum


def is_valid_name(message: str) -> bool:
    """
        Checks is name length >=2 symbols and <=20 symbols
    """
    return 2 <= len(message) <= 20


def is_valid_age(message: str) -> bool:
    """
        Checks is age int and is age >=2 and <=102 years
    """
    if message.startswith('0') or not message.isdigit():
        return False
    age = int(message)
    return 2 <= age <= 102


def is_valid_sex(message: str) -> bool:
    """
        Checks is sex in UserSexEnum
    """
    return any([message == str(sex) for sex in UserSexEnum])
