import argparse
from collections import Counter
from typing import List




def sol(data: str) -> int:
    result = 0
    for datum in data.split("\n\n"):
        counter = Counter(datum.replace("\n", ""))
        result += len(counter.keys())
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


if __name__ == '__main__':
    exit(main())
