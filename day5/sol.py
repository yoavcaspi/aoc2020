import argparse
from typing import List


def find_row(val):
    start = 0
    end = 128
    for c in val[:6]:
        mid = (start + end) // 2
        if c == "F":
            end = mid
        else:
            start = mid
    if val[6] == "F":
        return start
    else:
        return end - 1


def find_col(val):
    start = 0
    end = 8
    for c in val[-3:]:
        mid = (start + end) // 2
        if c == "L":
            end = mid
        else:
            start = mid
    if val[-1] == "L":
        return start
    else:
        return end - 1


def seat_id(row, col):
    return row * 8 + col


def sol(data: List[str]) -> int:
    max_id = 0
    for line in data:
        val = line.strip("\n")
        row = find_row(val)
        col = find_col(val)
        sid = seat_id(row, col)
        if sid > max_id:
            max_id = sid

    return max_id


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
