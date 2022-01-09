from dataclasses import dataclass

from src.domain.collection import Collection

@dataclass(frozen=True)
class Year:
    year: str
    positive: int
    recovered: int
    deaths: int
    active: int

@dataclass(frozen=True)
class Yearly(Collection[Year]):
    values: [Year]