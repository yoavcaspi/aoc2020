import argparse
from itertools import permutations
from typing import List

import pytest


def sol(data: str) -> int:
    nums = [0]
    for line in data.splitlines():
        nums.append(int(line))
    nums.sort()
    diffs_1 = 0
    diffs_3 = 1
    for num1,num2 in zip(nums, nums[1:]):
        if num2-num1 == 1:
            diffs_1+=1
        elif num2-num1 == 3:
            diffs_3+=1
    return diffs_1 * diffs_3

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
16
10
15
5
1
11
7
19
6
12
4
"""


INPUT2 = """\
28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3
"""

# @pytest.mark.parametrize("inp, out",
#                          (
#                                  (INPUT, 7*5),
#                                  (INPUT2, 22*10),
#                           )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
