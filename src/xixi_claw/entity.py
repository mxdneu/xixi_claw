from dataclasses import dataclass

from .components import Collider, Health, Position, Velocity


@dataclass
class Entity:
    entity_id: str
    position: Position
    velocity: Velocity
    collider: Collider
    health: Health
