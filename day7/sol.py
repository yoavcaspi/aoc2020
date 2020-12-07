import argparse
import re
from typing import List, Dict

import pytest


class Bag:

    def __init__(self, name: str):
        self.name = name
        self.bags = []


bag_regex = re.compile("(\d+) (\w+ \w+) bags?")


def sol(data: str) -> int:
    our_bag_name = "shiny gold"
    bags: Dict[str, Bag] = {}
    for line in data.splitlines():
        bag_name, content = line.split(" bags contain ")
        bag = bags.get(bag_name, Bag(bag_name))
        bags[bag_name] = bag
        if content == "no other bags.":
            continue
        for contained_bag_raw in content.split(", "):
            match = bag_regex.match(contained_bag_raw)
            num = match.group(1)
            contained_bag_name = match.group(2)
            if contained_bag_name in bags:
                contained_bag = bags[contained_bag_name]
            else:
                contained_bag = Bag(contained_bag_name)
                bags[contained_bag_name] = contained_bag
            contained_bag.bags.append(bag_name)

    relevant_bags = set()
    q = bags[our_bag_name].bags[:]
    for bag_name in q:
        relevant_bags.add(bag_name)
        q.extend(bags[bag_name].bags)

    return len(relevant_bags)


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
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


@pytest.mark.parametrize("inp, out",
                         ((INPUT, 4),
                          )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
