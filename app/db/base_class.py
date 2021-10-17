from typing import Any
import inflection

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative, declared_attr


convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata = MetaData(naming_convention=convention)


@as_declarative(metadata=metadata)
class Base:
    id: Any
    __name__: str

    # Generate __tablename__ automatically

    @declared_attr
    def __tablename__(cls) -> str:
        """Converts camelCase model name to snake_case table name"""
        return inflection.underscore(cls.__name__)
