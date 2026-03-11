from dataclasses import dataclass

from .config import GameConfig
from .entity import Entity


@dataclass(frozen=True)
class InputState:
    left: bool = False
    right: bool = False
    jump: bool = False


class InputSystem:
    def __init__(self, cfg: GameConfig) -> None:
        self._cfg = cfg

    def apply(self, player: Entity, input_state: InputState) -> None:
        if input_state.left == input_state.right:
            player.velocity.x = 0.0
        elif input_state.left:
            player.velocity.x = -self._cfg.player.move_speed
        else:
            player.velocity.x = self._cfg.player.move_speed

        if input_state.jump and player.collider.on_ground:
            player.velocity.y = -self._cfg.player.jump_speed
            player.collider.on_ground = False


class GravitySystem:
    def __init__(self, cfg: GameConfig) -> None:
        self._cfg = cfg

    def apply(self, player: Entity) -> None:
        player.velocity.y += self._cfg.physics.gravity * self._cfg.physics.dt
        player.velocity.y = min(player.velocity.y, self._cfg.physics.max_fall_speed)


class MovementSystem:
    def __init__(self, cfg: GameConfig) -> None:
        self._cfg = cfg

    def apply(self, player: Entity) -> None:
        dt = self._cfg.physics.dt
        player.position.x += player.velocity.x * dt
        player.position.y += player.velocity.y * dt

        # 简化地面碰撞：y >= 0 视为地面
        if player.position.y >= 0:
            player.position.y = 0
            player.velocity.y = 0
            player.collider.on_ground = True


class HealthSystem:
    def apply_hazard_damage(self, player: Entity) -> None:
        # 示例：当玩家越界到左侧危险区时扣血
        if player.position.x < -5:
            player.health.apply_damage(1)
