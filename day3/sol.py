import argparse
from typing import List

import pytest


def sol(data: List[str]) -> int:
    x = 0
    line_size = len(data[0]) - 1
    count = 0
    for line in data[1:]:
        x = (x + 3) % line_size
        if line[x] == "#":
            count += 1
    return count


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
#                          ((INPUT, 7),)
# )
# def test_sol1(inp, out):
#     assert sol(inp.splitlines()) == out



if __name__ == '__main__':
    exit(main())
