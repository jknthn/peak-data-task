import json
from dataclasses import dataclass
from itertools import zip_longest
from typing import List, Dict

from src.name import Name


@dataclass(eq=True, frozen=True)
class Author:
    names: List[Name]
    last_name: str

    def __repr__(self):
        return f"<{' '.join([repr(n) for n in self.names])} | {self.last_name}>"

    def __hash__(self):
        key = (tuple(self.names), self.last_name)
        return hash(key)

    @classmethod
    def from_string(cls, author_str: str) -> "Author":
        lower_str = author_str.lower()
        elements = lower_str.split(" ")
        names = [Name.from_raw(n) for n in elements[:-1]]
        last_name = elements[-1]
        return Author(names, last_name)

    def full_prct(self) -> float:
        return sum([n.is_full() for n in self.names]) / len(self.names)

    def similar_prct(self, other: "Author") -> float:
        if self.last_name == other.last_name and len(self.names) == len(other.names):
            return sum([t.initial == o.initial for t, o in zip(self.names, other.names)]) / len(self.names)
        return 0
    
    def dict(self) -> Dict[str, str]:
        return {
            "firstname": " ".join([n.element().capitalize() for n in self.names]),
            "lastname": self.last_name.capitalize()
        }
