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

    def __init__(self, full: Optional[str], initial: Optional[str] = None, parse_dash: bool = False):
        if not full and not initial:
            raise ValueError

        if full and initial and not Name.is_dash_equal(full, initial):
            raise ValueError

        self.full = full
        if full and not initial:
            self.initial = Name.to_initial(full)
        else:
            self.initial = initial

    @staticmethod
    def is_dash_equal(full: str, initial: str) -> bool:
        for f, i in zip_longest(full.split("-"), initial.split("-")):
            if f[0] != i:
                return False
        return True

    @staticmethod
    def to_initial(full: str) -> str:
        return "-".join([f[0] for f in full.split("-")])
