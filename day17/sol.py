import argparse
from collections import defaultdict, Counter

import pytest


def count_active(x, y, z, space):
    adjecents_places = (
        (x - 1, y - 1, z - 1),
        (x - 1, y - 1, z),
        (x - 1, y - 1, z + 1),
        (x - 1, y, z - 1),
        (x - 1, y, z),
        (x - 1, y, z + 1),
        (x - 1, y + 1, z - 1),
        (x - 1, y + 1, z),
        (x - 1, y + 1, z + 1),
        (x, y - 1, z - 1),
        (x, y - 1, z),
        (x, y - 1, z + 1),
        (x, y, z - 1),
        (x, y, z + 1),
        (x, y + 1, z - 1),
        (x, y + 1, z),
        (x, y + 1, z + 1),
        (x + 1, y - 1, z - 1),
        (x + 1, y - 1, z),
        (x + 1, y - 1, z + 1),
        (x + 1, y, z - 1),
        (x + 1, y, z),
        (x + 1, y, z + 1),
        (x + 1, y + 1, z - 1),
        (x + 1, y + 1, z),
        (x + 1, y + 1, z + 1),
    )
    count = 0
    for adj_x, adj_y, adj_z in adjecents_places:
        adjecent_place = space.get((adj_x, adj_y, adj_z), ".")
        if adjecent_place == "#":
            count += 1
    return count


def run_space_rules(space: dict[tuple[int, int, int], str],
                    max_x: int,
                    max_y: int,
                    max_z: int) -> dict[tuple[int, int, int], str]:
    new_space: dict[tuple[int, int, int], str] = defaultdict(lambda: ".")
    for z in range(-max_z + 1, max_z + 1):
        for y in range(-max_y, max_y + 1):
            for x in range(-max_x, max_x + 1):
                active = count_active(x, y, z, space)
                if space[x, y, z] == "#" and active in (2, 3):
                    new_space[x, y, z] = "#"
                elif space[x, y, z] == "." and active == 3:
                    new_space[x, y, z] = "#"
                else:
                    new_space[x, y, z] = "."

    return new_space


def print_space(space, max_x, max_y, max_z):
    for z in range(-max_z + 1, max_z):
        print(f"{z=}")
        for y in range(-max_y, max_y + 1):
            for x in range(-max_x, max_x + 1):
                print(space[x, y, z], end="")
            print()
        print("\n\n")


def sol(data: str) -> int:
    space: dict[tuple[int, int, int], str] = defaultdict(lambda: ".")
    max_y = len(data.splitlines()) // 2
    max_x = len(data.splitlines()[0]) // 2
    max_z = 1
    for y, row in enumerate(data.splitlines(), -max_y):
        for x, c in enumerate(row, -max_x):
            print(c, end="")
            space[x, y, 0] = c
        print()
    print()
    print(Counter(space.values()).get("#"))

    for i in range(6):
        max_x += 1
        max_y += 1
        max_z += 1
        space = run_space_rules(space, max_x, max_y, max_z)
        print(f"After {i+1} cycles")
        print(Counter(space.values()).get("#"))
        print_space(space, max_x, max_y, max_z)

    return Counter(space.values()).get("#")


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
.#.
..#
###
"""


# @pytest.mark.parametrize("inp, out",
#                          (
#                                  (INPUT, 112),
#                          )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
