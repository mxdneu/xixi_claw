from xixi_claw.game import run_simulation
from xixi_claw.systems import InputState


def test_move_right_and_land_on_ground() -> None:
    snapshots = run_simulation([
        InputState(right=True),
        InputState(right=True),
        InputState(right=True),
    ])
    assert snapshots[-1].x > 0
    assert snapshots[-1].y == 0
    assert snapshots[-1].hp == 100


def test_jump_then_fall() -> None:
    snapshots = run_simulation([
        InputState(jump=True),
        InputState(),
        InputState(),
        InputState(),
        InputState(),
    ])
    assert min(s.y for s in snapshots) < 0
