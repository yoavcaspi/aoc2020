import argparse
from collections import defaultdict
from itertools import product

import pytest


def check_message(message: str, accepted_messages, sub_message_len: int) -> bool:
    """
    :param message: The message to check
    :param accepted_messages: the dict with all the message values
    :param sub_message_len: the size to check, should be the size of all the messages of type 42 and 31
    :return: True if size 0 otherwise check that:
        either starts with 42
        or starts with 42 and ends with 31
        and call with the middle message to check that this process proceed.
    """
    if len(message) == 0:
        return True
    return (
        (message[:sub_message_len] in accepted_messages[42] and check_message(message[sub_message_len:], accepted_messages, sub_message_len))
        or
        (message[:sub_message_len] in accepted_messages[42] and message[-sub_message_len:] in accepted_messages[31]
         and check_message(message[sub_message_len:-sub_message_len], accepted_messages, sub_message_len))
    )


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
                    accepted_messages[rule_id] |= accepted_messages[
                        temp_values[0]]
                    continue
                results = set()
                for val in product(
                        *[accepted_messages[v] for v in temp_values]):
                    results.add("".join(val))
                accepted_messages[rule_id] |= results

    # I assume that the size of all the messages acceptable by 31 and 42
    # are the same (In the test scenario it's 5 and in prod it's 8)
    all_length_of_message_42 = set(len(val) for val in accepted_messages[42])
    all_length_of_message_31 = set(len(val) for val in accepted_messages[31])
    assert len(all_length_of_message_42) == 1
    assert len(all_length_of_message_31) == 1
    len_42 = all_length_of_message_42.pop()
    len_31 = all_length_of_message_31.pop()
    assert len_31 == len_42
    res = 0
    # Assumption all the messages which are legit start with message type 42 at least twice
    # and ends with 31.
    for message in raw_messages.splitlines():
        if (message[:len_42] in accepted_messages[42] and message[len_42:len_42*2] in accepted_messages[42] and message[-len_31:] in accepted_messages[31]
            and check_message(message[len_42*2:-len_42], accepted_messages, len_42)
        ):
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
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
"""


@pytest.mark.parametrize(
    "inp, out",
    (
            (INPUT, 12),
    )
)
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
