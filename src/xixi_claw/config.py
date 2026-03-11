from dataclasses import dataclass


@dataclass(frozen=True)
class PhysicsConfig:
    gravity: float = 40.0
    max_fall_speed: float = 60.0
    dt: float = 1 / 30


@dataclass(frozen=True)
class PlayerConfig:
    move_speed: float = 12.0
    jump_speed: float = 22.0
    max_health: int = 100


@dataclass(frozen=True)
class GameConfig:
    physics: PhysicsConfig = PhysicsConfig()
    player: PlayerConfig = PlayerConfig()
