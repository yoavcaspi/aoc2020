import argparse
from typing import List

import pytest


def sol(data: List[str]) -> int:
    data_int: List[int] = [int(val) for val in data]
    data_int.sort()
    start, end = 0, len(data_int) - 1
    while start < end:
        sum_val = data_int[start] + data_int[end]
        if sum_val == 2020:
            return data_int[start]*data_int[end]
        elif sum_val < 2020:
            start += 1
        else:
            end -= 1


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
                         ((INPUT, 514579),)
                         )
def test(input_, output):
    assert sol(input_.splitlines()) == output


if __name__ == '__main__':
    exit(main())
