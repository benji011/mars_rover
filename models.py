from typing import NamedTuple


class RoverPosition(NamedTuple):
    x: int
    y: int
    direction: str

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.direction})"


class Coordinates(NamedTuple):
    x: int
    y: int

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
