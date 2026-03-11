from dataclasses import dataclass

from .config import GameConfig
from .entity import Entity
from .systems import GravitySystem, HealthSystem, InputState, InputSystem, MovementSystem


@dataclass
class WorldSnapshot:
    tick: int
    x: float
    y: float
    vx: float
    vy: float
    hp: int


class GameWorld:
    def __init__(self, cfg: GameConfig, player: Entity) -> None:
        self.cfg = cfg
        self.player = player
        self.tick = 0

        self.input_system = InputSystem(cfg)
        self.gravity_system = GravitySystem(cfg)
        self.movement_system = MovementSystem(cfg)
        self.health_system = HealthSystem()

    def step(self, input_state: InputState) -> WorldSnapshot:
        self.input_system.apply(self.player, input_state)
        self.gravity_system.apply(self.player)
        self.movement_system.apply(self.player)
        self.health_system.apply_hazard_damage(self.player)

        self.tick += 1
        return WorldSnapshot(
            tick=self.tick,
            x=self.player.position.x,
            y=self.player.position.y,
            vx=self.player.velocity.x,
            vy=self.player.velocity.y,
            hp=self.player.health.current,
        )
