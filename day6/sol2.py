import argparse
from collections import Counter
from typing import List

import pytest


def sol(data: str) -> int:
    result = 0
    for datum in data.split("\n\n"):
        counter = Counter(datum)
        group_size = counter.pop("\n", 0) + 1

        for char, num in counter.most_common():
            if num == group_size:
                result += 1
            else:
                break
    return result


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
abc

a
b
c

ab
ac

a
a
a
a

b

"""


# @pytest.mark.parametrize("inp, out",
#                          ((INPUT, 6),
#                           )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
