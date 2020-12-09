import argparse
from itertools import permutations
from typing import List

import pytest


def find_all_sums(param: List[int]):
    sums = set()
    for perm in permutations(param, 2):
        sums.add(sum(perm))
    return sums


def sol(data: str) -> int:
    nums = []
    for line in data.splitlines():
        nums.append(int(line))
    for i, val in enumerate(nums[25:]):
        sums = find_all_sums(nums[i:i+25])
        if val not in sums:
            return val

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
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""


# @pytest.mark.parametrize("inp, out",
#                          ((INPUT, 127),
#                           )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out
#

if __name__ == '__main__':
    exit(main())
