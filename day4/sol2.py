import argparse
from typing import List

import pytest


def sol(data: List[str]) -> int:
    slopes = ((1, 1),
              (3, 1),
              (5, 1),
              (7, 1),
              (1, 2))
    result = 1
    for x, y in slopes:
        index = 0
        line_size = len(data[0]) - 1
        count = 0

        for line in data[y::y]:
            line = line.strip()
            index = (index + x) % line_size
            if line[index] == "#":
                count += 1
        result *= count
    return result


def get_input(filename: str) -> List[str]:
    with open(filename) as f:
        lines = f.readlines()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data))
    return 0


INPUT = """\
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""


# @pytest.mark.parametrize("inp, out",
#                          ((INPUT, 336),)
#                          )
# def test_sol1(inp, out):
#     assert sol(inp.splitlines()) == out


if __name__ == '__main__':
    exit(main())
