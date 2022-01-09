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

@dataclass(frozen=True)
class Month:
    month: str
    positive: int
    recovered: int
    deaths: int
    active: int

@dataclass(frozen=True)
class Monthly(Collection[Month]):
    values: [Month]

@dataclass(frozen=True)
class Day:
    date: str
    positive: int
    recovered: int
    deaths: int
    active: int

@dataclass(frozen=True)
class Daily(Collection[Day]):
    values: [Day]