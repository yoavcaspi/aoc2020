import argparse
from collections import defaultdict

import pytest


def sol(data: str) -> int:
    ticket_vals: dict[str, set[int]] = {}
    not_valid_values = set(range(1000))
    rules, my_ticket, nearby_tickets_raw = data.split("\n\n", 3)
    for rule in rules.splitlines():
        name, rule_description = rule.split(":", 2)
        first, second = rule_description.split(" or ", 2)
        s_first, e_first = first.split("-")
        s_second, e_second = second.split("-")
        ticket_vals[name] = (
                set(range(int(s_first), int(e_first) + 1)) |
                set(range(int(s_second), int(e_second) + 1))
        )
        not_valid_values -= ticket_vals[name]

    nearby_tickets: dict[int, set[int]] = defaultdict(set)
    for ticket in nearby_tickets_raw.splitlines()[1:]:
        vals = ticket.split(",")
        for s_val in vals:
            val = int(s_val)
            if val in not_valid_values:
                break
        else:
            for i, val in enumerate(vals):
                nearby_tickets[i].add(int(val))
    my_ticket_vals = [int(val) for val in my_ticket.splitlines()[1].split(",")]
    possible_values = defaultdict(set)
    for i in range(len(nearby_tickets)):
        for rule_name, values in ticket_vals.items():
            if nearby_tickets[i].issubset(values):
                possible_values[i].add(rule_name)
    real_order = {}
    my_ticket_size = len(my_ticket_vals)
    res=1
    while len(real_order) < my_ticket_size:
        chosen_value = None
        for i, values in possible_values.items():
            if len(values) == 1:
                chosen_value = values.pop()
                if chosen_value.startswith("departure"):
                    res*=my_ticket_vals[i]
                real_order[i] = chosen_value
                break
        for values in possible_values.values():
            try:
                values.remove(chosen_value)
            except KeyError:
                pass

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
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
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
