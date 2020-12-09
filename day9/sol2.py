import argparse
from itertools import permutations
from typing import List

import pytest


def find_all_sums(param: List[int]):
    sums = set()
    for perm in permutations(param, 2):
        sums.add(sum(perm))
    return sums


def check_if_applicable(nums, i, invalid_num) -> int:
    result = 0
    smallest = nums[i]
    largest = nums[i]
    for val in nums[i:]:
        result += val
        if val > largest:
            largest = val
        if smallest > val:
            smallest = val
        if result > invalid_num:
            return -1
        if result == invalid_num:
            return largest + smallest


def sol(data: str, xmas_val: int) -> int:
    nums = []
    for line in data.splitlines():
        nums.append(int(line))
    invalid_num = -1
    for i, val in enumerate(nums[xmas_val:]):
        sums = find_all_sums(nums[i:i+xmas_val])
        if val not in sums:
            invalid_num = val
    for i in range(len(nums)):
        result = check_if_applicable(nums, i, invalid_num)
        if result != -1:
            return result

def get_input(filename: str) -> str:
    with open(filename) as f:
        lines = f.read()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data, 25))
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


# @pytest.mark.parametrize("inp, xmas_val, out",
#                          ((INPUT, 5, 15+47),
#                           )
#                          )
# def test_sol1(inp, xmas_val, out):
#     assert sol(inp, 5) == out


if __name__ == '__main__':
    exit(main())
