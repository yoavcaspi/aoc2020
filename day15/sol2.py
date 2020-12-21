import argparse
import time
from collections import defaultdict

import pytest


def sol(data: str) -> int:
    mem: dict[int, int] = defaultdict(lambda: -1)
    last_value = None
    for i, x in enumerate(data.split(",")):
        last_value = int(x)
        mem[last_value] = i
    for i in range(len(mem) - 1, 30_000_000 - 1):
        last = mem[last_value]
        if last == -1:
            val = 0
        else:
            val = i - last
        mem[last_value] = i
        last_value = val
    return last_value


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
                                 ("0,3,6", 175594),
                                 # ("1,3,2", 2578),
                                 # ("2,1,3", 3544142),
                                 # ("1,2,3", 261214),
                                 # ("2,3,1", 6895259),
                                 # ("3,2,1", 18),
                                 # ("3,1,2", 362),
                         )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
