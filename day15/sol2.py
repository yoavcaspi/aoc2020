import argparse
import time

import pytest


def sol(data: str) -> int:
    start = time.time()
    mem: dict[int, tuple[int, int]] = {}
    last_value = -1
    for i, x in enumerate(data.split(",")):
        last_value = int(x)
        mem[last_value] = (i, i)
    for i in range(len(mem) - 1, 30_000_000 - 1):
        last = mem[last_value]
        if last[0] == i:
            val = 0
        else:
            val = i - last[0]
        if val in mem:
            val_last = mem[val][1]
            mem[val] = (val_last, i + 1)
        else:
            mem[val] = (i + 1, i + 1)
        last_value = val
    print(f"Took {time.time() - start}")
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
