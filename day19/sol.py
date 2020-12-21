import argparse
from collections import defaultdict
from itertools import product

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
            val = calculate_sum(exp[i + 1:i + bracket_size])
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
    raw_rules, raw_messages = data.split("\n\n", 2)
    accepted_messages: dict[int, set[str]] = defaultdict(set)
    rules: dict[int, list[list[int]]] = defaultdict(list)
    for raw_rule in raw_rules.splitlines():
        raw_id, raw_values = raw_rule.split(": ", 2)
        rule_id = int(raw_id)
        if raw_values.startswith('"'):
            accepted_messages[rule_id].add(raw_values[1:-1])
        else:
            for raw_value in raw_values.split(" | "):
                rules[rule_id].append(
                    [int(val) for val in raw_value.split(" ")])
    print(rules)
    while len([rule for rule in rules.values() if rule]) > 0:
        accepted_ids = set(accepted_messages.keys())
        temp_rules = dict(rules)
        for rule_id, values in temp_rules.items():
            if not all(accepted_ids.issuperset(val) for val in values):
                continue
            del rules[rule_id]
            for temp_values in values:
                if len(temp_values) == 1:
                    accepted_messages[rule_id]|=accepted_messages[temp_values[0]]
                    continue
                results = set()
                for val in product(
                        *[accepted_messages[v] for v in temp_values]):
                    results.add("".join(val))
                accepted_messages[rule_id] |= results
    res = 0
    for message in raw_messages.splitlines():
        if message in accepted_messages[0]:
            res += 1
    return res


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
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""


# @pytest.mark.parametrize(
#     "inp, out",
#     (
#             (INPUT, 2),
#     )
# )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
