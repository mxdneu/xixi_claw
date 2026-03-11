from .components import Collider, Health, Position, Velocity
from .config import GameConfig
from .entity import Entity
from .systems import InputState
from .world import GameWorld, WorldSnapshot


def create_default_player(cfg: GameConfig) -> Entity:
    return Entity(
        entity_id="player",
        position=Position(0.0, 0.0),
        velocity=Velocity(),
        collider=Collider(width=1.0, height=2.0, on_ground=True),
        health=Health(current=cfg.player.max_health, maximum=cfg.player.max_health),
    )


def run_simulation(inputs: list[InputState], cfg: GameConfig | None = None) -> list[WorldSnapshot]:
    cfg = cfg or GameConfig()
    world = GameWorld(cfg, create_default_player(cfg))
    return [world.step(i) for i in inputs]
