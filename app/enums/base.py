import enum


class EnumBase(str, enum.Enum):
    def __str__(self):
        return self.value
