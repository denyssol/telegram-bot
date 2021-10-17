from sqlalchemy.engine import Engine

from app.db import base  # noqa: F401


def init_db(engine: Engine) -> None:
    base.Base.metadata.drop_all(bind=engine)
    base.Base.metadata.create_all(bind=engine)
