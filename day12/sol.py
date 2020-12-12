import argparse
from typing import List

import pytest


def sol(data: str) -> int:
    directions = ["E", "N", "W", "S"]
    directions_facing = {
        "E": (1, 0),
        "N": (0, 1),
        "W": (-1, 0),
        "S": (0, -1)
    }
    facing = "E"
    current_pos = [0, 0]
    for action in data.splitlines():
        if action[0] == "N":
            current_pos[1] += int(action[1:])
        elif action[0] == "S":
            current_pos[1] -= int(action[1:])
        elif action[0] == "E":
            current_pos[0] += int(action[1:])
        elif action[0] == "W":
            current_pos[0] -= int(action[1:])
        elif action[0] == "L":
            result = int(action[1:]) // 90
            facing = directions[(directions.index(facing) + result) % 4]
        elif action[0] == "R":
            result = int(action[1:]) // 90
            facing = directions[(directions.index(facing) - result) % 4]
        elif action[0] == "F":
            current_pos[0] += directions_facing[facing][0] * int(action[1:])
            current_pos[1] += directions_facing[facing][1] * int(action[1:])
        else:
            raise Exception(f"Weird action: {action}")
    return abs(current_pos[0]) + abs(current_pos[1])


def get_input(filename: str) -> List[str]:
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
                                 (INPUT, 17+8),
                         )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
