import argparse
from itertools import permutations, product
from typing import List

import pytest


def write_to_mem(address: int, mask: str, val: int, mem: dict[int, int]) -> None:
    unmasked_address = list(bin(address)[2:].zfill(36))
    x_indices = []
    vals = []
    for i, (m, v) in enumerate(zip(mask, unmasked_address[:])):
        if m == "X":
            x_indices.append(i)
            vals.append((0,1))
            unmasked_address[i] = "X"
        elif m == "1":
            unmasked_address[i] = "1"
    for prod in product(*vals):
        for i,x in enumerate(x_indices):
            unmasked_address[x] = str(prod[i])
        mem[int("".join(unmasked_address), 2)] = val


def sol(data: str) -> int:
    mem: dict[int, int] = {}
    mask = "0" * 36
    for datum in data.splitlines():
        if datum.startswith("mask"):
            mask = datum[7:]
            continue
        raw_address, raw_val = datum.split(" = ", 1)
        address = int(raw_address[4:-1])
        write_to_mem(address, mask, int(raw_val), mem)
    return sum(mem.values())


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
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
"""


# @pytest.mark.parametrize("inp, out",
#                          (
#                                  (INPUT, 208),
#                          )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
