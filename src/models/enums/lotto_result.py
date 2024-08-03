from enum import Enum


class LottoResult(Enum):
    FIRST = 1,
    SECOND = 2,
    THIRD = 3,
    FOURTH = 4,
    FIFTH = 5,
    NONE = 0

    def __eq__(self, other: object):
        if isinstance(other, LottoResult):
            return self.name == other.name
        return NotImplemented
