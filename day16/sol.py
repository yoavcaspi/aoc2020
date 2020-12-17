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
    not_valid_values = set(range(1000))
    rules, my_ticket, nearby_tickets = data.split("\n\n", 3)
    for rule in rules.splitlines():
        first, second = rule.split(":", 2)[1].split(" or ", 2)
        s_first, e_first = first.split("-")
        for i in range(int(s_first), int(e_first) + 1):
            try:
                not_valid_values.remove(i)
            except KeyError:
                pass
        s_second, e_second = second.split("-")

        for i in range(int(s_second), int(e_second) + 1):
            try:
                not_valid_values.remove(i)
            except KeyError:
                pass
    res = 0
    for ticket in nearby_tickets.splitlines()[1:]:
        vals = ticket.split(",")
        for s_val in vals:
            val = int(s_val)
            if val in not_valid_values:
                res += val
    return res


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
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""


# @pytest.mark.parametrize("inp, out",
#                          (
#                                  (INPUT, 71),
#                          )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
