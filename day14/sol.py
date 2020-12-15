import argparse
from typing import List

import pytest


def calculate_val(raw_val: int, mask: int) -> int:
    unmasked_val = bin(raw_val)[2:].zfill(36)
    val = ["0"] * 36
    for i, (m, v) in enumerate(zip(mask, unmasked_val)):
        if m == "X":
            val[i] = v
        else:
            val[i] = m
    return int("".join(val), 2)


def sol(data: str) -> int:
    mem: dict[int, int] = {}
    mask = 0
    for datum in data.splitlines():
        if datum.startswith("mask"):
            mask = datum[7:]
            continue
        raw_address, raw_val = datum.split(" = ", 1)
        val = calculate_val(int(raw_val), mask)
        mem[raw_address] = val
    return sum(mem.values())


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
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
"""


# @pytest.mark.parametrize("inp, out",
#                          (
#                                  (INPUT, 165),
#                          )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
