from pydantic.dataclasses import dataclass
from typing import List
from src.domain.collection import Collection

@dataclass
class General:
    total_positive: int
    total_recovered: int
    total_deaths: int
    total_active: int
    new_positive: int
    new_recovered: int
    new_active: int
    new_deaths: int

@dataclass
class Year:
    year: str
    positive: int
    recovered: int
    deaths: int
    active: int

@dataclass
class Yearly(Collection[Year]):
    values: List[Year]

@dataclass
class Month:
    month: str
    positive: int
    recovered: int
    deaths: int
    active: int

@dataclass
class Monthly(Collection[Month]):
    values: List[Month]

@dataclass
class Day:
    date: str
    positive: int
    recovered: int
    deaths: int
    active: int

@dataclass
class Daily(Collection[Day]):
    values: List[Day]