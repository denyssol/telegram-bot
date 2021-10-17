from sqlalchemy import Column, Enum, Integer, String

from app.db.base_class import Base
from app.enums.user_sex import UserSexEnum
from app.enums.user_state import UserStateEnum


class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    age = Column(Integer)
    sex = Column(Enum(UserSexEnum))
    state = Column(Enum(UserStateEnum))
