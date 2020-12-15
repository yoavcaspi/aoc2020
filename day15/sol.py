import argparse
from collections import defaultdict

import pytest


def sol(data: str) -> int:
    mem: dict[int, tuple[int, int]] = {}
    values: list[int] = []
    for i, x in enumerate(data.split(",")):
        values.append(int(x))
        mem[int(x)] = (i, i)
    for i in range(len(values) - 1, 2020):
        last = mem[values[i]]
        if last[0] == i:
            val = 0
        else:
            val = i - last[0]
        if val in mem:
            val_last = mem[val][1]
            mem[val] = (val_last, i + 1)
        else:
            mem[val] = (i + 1, i + 1)
        values.append(val)
    return values[2019]


def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = "8,13,1,0,18,9"
    print(sol(data))
    return 0


@pytest.mark.parametrize("inp, out",
                         (
                                 ("0,3,6", 436),
                                 ("1,3,2", 1),
                                 ("2,1,3", 10),
                                 ("1,2,3", 27),
                                 ("2,3,1", 78),
                                 ("3,2,1", 438),
                                 ("3,1,2", 1836),
                         )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
