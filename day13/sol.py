import argparse
from typing import List

import pytest


def sol(data: str) -> int:
    new_data = data.splitlines()
    time_arrievd = int(new_data[0])
    bus_ids = []
    earliest = time_arrievd*2
    chosen = -1
    for bus_id_str in new_data[1].split(","):
        if bus_id_str == "x":
            continue
        bus_id = int(bus_id_str)
        bus_ids.append(bus_id)
        div, mod = divmod(time_arrievd, bus_id)
        if mod == 0:
            print("Wow")
        elif time_arrievd + (bus_id - mod) < earliest:
            earliest = time_arrievd + (bus_id - mod)
            chosen = bus_id
    return (earliest - time_arrievd) * chosen

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
939
7,13,x,x,59,x,31,19
"""

@pytest.mark.parametrize("inp, out",
                         (
                                 (INPUT, 295),
                         )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
