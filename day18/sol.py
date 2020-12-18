import argparse
from collections import defaultdict, Counter

import pytest


def find_closing_braket_index(exp: str) -> int:
    num_brakets = 0
    for i, c in enumerate(exp):
        if c == "(":
            num_brakets += 1
        elif c == ")":
            num_brakets -= 1
            if num_brakets == 0:
                return i



def calculate_sum(exp: str):
    result = 0
    operand = "+"
    i = 0
    while i < len(exp):
        if exp[i] == "(":
            bracket_size = find_closing_braket_index(exp[i:])
            val = calculate_sum(exp[i+1:i+bracket_size])
            if operand == "+":
                result += val
            else:
                result *= val
            i += bracket_size
        else:
            if operand == "+":
                result += int(exp[i])
            else:
                result *= int(exp[i])
        if i + 1 >= len(exp):
            break
        operand = exp[i + 2]
        i += 4
    return result

def sol(data: str) -> int:
    result = 0
    for line in data.splitlines():
        result += calculate_sum(line)
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
    print(sol(data))
    return 0


# @pytest.mark.parametrize(
#     "inp, out",
#     (
#             ("2 * 3 + (4 * 5)", 26),
#             ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 437),
#             ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 12240),
#             ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 13632),
#     )
# )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
