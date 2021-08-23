from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Author:
    first_name: Optional[str]
    middle_names: List[str]
    last_name: str

    first_name_initial: Optional[str]
    middle_names_initials: List[str]
