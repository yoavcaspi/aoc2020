import argparse

import pytest


def sol(data: str) -> int:
    waypoint: dict[str, int] = {
        "E": 10,
        "N": 1,
    }
    directions: list[str] = ["E", "N", "W", "S"]
    directions_facing: dict[str, tuple[int, int]] = {
        "E": (1, 0),
        "N": (0, 1),
        "W": (-1, 0),
        "S": (0, -1)
    }
    current_pos = [0, 0]
    for action in data.splitlines():
        if action[0] == "N":
            waypoint["N"] += int(action[1:])
        elif action[0] == "S":
            waypoint["N"] -= int(action[1:])
        elif action[0] == "E":
            waypoint["E"] += int(action[1:])
        elif action[0] == "W":
            waypoint["E"] -= int(action[1:])
        elif action[0] == "R":
            result = int(action[1:]) // 90
            direction_e = directions_facing[directions[(directions.index("E") - result) % 4]]
            direction_n = directions_facing[directions[(directions.index("N") - result) % 4]]
            new_waypoint = {
                "E": waypoint["E"] * direction_e[0] + waypoint["N"] * direction_n[0],
                "N": waypoint["E"] * direction_e[1] + waypoint["N"] * direction_n[1],
            }
            waypoint = new_waypoint
        elif action[0] == "L":
            result = int(action[1:]) // 90
            direction_e = directions_facing[directions[(directions.index("E") + result) % 4]]
            direction_n = directions_facing[directions[(directions.index("N") + result) % 4]]
            new_waypoint = {
                "E": waypoint["E"] * direction_e[0] + waypoint["N"] * direction_n[0],
                "N": waypoint["E"] * direction_e[1] + waypoint["N"] * direction_n[1],
            }
            waypoint = new_waypoint

        elif action[0] == "F":
            current_pos[0] += waypoint["E"] * int(action[1:])
            current_pos[1] += waypoint["N"] * int(action[1:])
        else:
            raise Exception(f"Weird action: {action}")
    return abs(current_pos[0]) + abs(current_pos[1])


def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data))
    return 0


INPUT = """\
F10
N3
F7
R90
F11
"""


@pytest.mark.parametrize("inp, out",
                         (
                                 (INPUT, 286),
                         )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
