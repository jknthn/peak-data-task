from dataclasses import dataclass
from typing import Optional
from itertools import zip_longest


@dataclass
class Name:
    """
    Handles lowercase as an input
    """
    full: Optional[str]
    initial: str

    def __init__(self, full: Optional[str], initial: Optional[str] = None):
        if not full and not initial:
            raise ValueError

        if full and initial and not Name.is_dash_equal(full, initial):
            raise ValueError

        self.full = full
        if full and not initial:
            self.initial = Name.to_initial(full)
        else:
            self.initial = initial

    def __repr__(self):
        return f"{self.full} [{self.initial}]"

    def __hash__(self):
        key = (self.full, self.initial)
        return hash(key)

    def element(self) -> str:
        return self.full or self.initial

    @classmethod
    def from_raw(cls, text: str) -> "Name":
        initial_threshold = text.count("-") + 1
        if len(text) > initial_threshold:
            return cls(text)
        else:
            return cls(None, text)

    @staticmethod
    def is_dash_equal(full: str, initial: str) -> bool:
        for f, i in zip_longest(full.split("-"), initial.split("-")):
            if f[0] != i:
                return False
        return True

    @staticmethod
    def to_initial(full: str) -> str:
        return "-".join([f[0] for f in full.split("-")])

    def is_full(self) -> bool:
        return self.full is not None and self.initial is not None


