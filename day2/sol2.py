import argparse
import re
from typing import List


def sol(data: List[str]) -> int:
    regex = re.compile("(\d+)[-](\d+) (\w): (\w+)")
    count = 0
    for line in data:
        match = regex.match(line)
        first, second = int(match.group(1)), int(match.group(2))
        letter = match.group(3)
        s = match.group(4)
        if ((s[first - 1] == letter and s[second - 1] != letter) or
                (s[first - 1] != letter and s[second - 1] == letter)):
            count += 1
    return count


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


if __name__ == '__main__':
    exit(main())
