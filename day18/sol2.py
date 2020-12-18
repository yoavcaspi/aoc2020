import argparse

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


def calculate_sum(exp: str, current_result=0, current_operand="+"):
    if current_result is None:
        result = 0
    else:
        result = current_result
    if current_operand is None:
        operand = "+"
    else:
        operand = current_operand
    i = 0
    while i < len(exp):
        if exp[i] == "(":
            bracket_size = find_closing_braket_index(exp[i:])
            val = calculate_sum(exp[i + 1:i + bracket_size])
            i += bracket_size
        else:
            val = int(exp[i])
        if operand == "+":
            result += val
        else:
            if i == len(exp) - 1:
                result *= val
            else:
                result *= calculate_sum(exp[i:])
                break
        if i + 1 >= len(exp):
            break
        operand = exp[i + 2]
        i += 4
        if operand == "*":
            result *= calculate_sum(exp[i:])
            break
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


@pytest.mark.parametrize(
    "inp, out",
    (
            ("1 + (2 * 3) + (4 * (5 + 6))", 51),
            ("2 * 3 + (4 * 5)", 46),
            ("5 + (8 * 3 + 9 + 3 * 4 * 3)", 1445),
            ("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", 669060),
            ("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", 23340),
    )
)
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
