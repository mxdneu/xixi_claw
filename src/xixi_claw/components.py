from dataclasses import dataclass


@dataclass
class Position:
    x: float
    y: float


@dataclass
class Velocity:
    x: float = 0.0
    y: float = 0.0


@dataclass
class Collider:
    width: float
    height: float
    on_ground: bool = False


@dataclass
class Health:
    current: int
    maximum: int

    def apply_damage(self, amount: int) -> None:
        self.current = max(0, self.current - max(0, amount))

    @property
    def alive(self) -> bool:
        return self.current > 0
