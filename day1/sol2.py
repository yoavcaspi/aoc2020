import argparse
from typing import List
from itertools import  permutations
import pytest


def sol(data: List[str]) -> int:
    data_int: List[int] = [int(val) for val in data]
    data_int.sort()

    end = len(data_int) - 1
    while True:
        pre_sum_val = data_int[end -1] + data_int[end]
        if pre_sum_val >= 2020:
            end -= 1
            break
    for a, b, c in permutations(data_int[:end], 3):
        if a + b + c == 2020:
            return a*b*c


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
1721
979
366
299
675
1456
"""


@pytest.mark.parametrize("input_,output",
                         ((INPUT, 241861950),)
                         )
def test(input_, output):
    assert sol(input_.splitlines()) == output


if __name__ == '__main__':
    exit(main())

