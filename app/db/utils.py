from sqlalchemy.orm import Session

from app.db.models import User
from app.enums.user_state import UserStateEnum


def create_or_get_user(db: Session, chat_id):
    """
        Creates or gets user with id=chat_id state=START
    """
    user = db.query(User).filter_by(id=chat_id).first()

    if user is None:
        user = User(id=chat_id, state=UserStateEnum.START)  # type: ignore
        db.add(user)

    return user


def create_or_default_user(db: Session, chat_id):
    """
        Creates or sets user with id=chat_id state=START
    """
    user = db.query(User).filter_by(id=chat_id).first()

    if user is None:
        user = User(id=chat_id, state=UserStateEnum.START)  # type: ignore
        db.add(user)
    else:
        user.state = UserStateEnum.START
    return user
