import argparse
from typing import List

import pytest


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0
    q, r = divmod(a, b)
    gcd, x, y = egcd(b, r)
    return gcd, y, x - q * y


def sol2(data: str) -> int:
    bus_times: list[tuple[int, int]] = []
    r = 0
    val = 1
    for bus_id_str in data.split(","):
        if bus_id_str == "x":
            r += 1
            continue
        bus_id = int(bus_id_str)
        bus_times.append((bus_id, (bus_id - r) % bus_id))
        r += 1
        val *= bus_id
    res = []
    for bus_id, r in bus_times:
        gcd, y, x = egcd(val // bus_id, bus_id)
        res.append((val // bus_id * y * r) % val)
    return sum(res) % val


def sol(data: str) -> int:
    new_data = data.splitlines()
    return sol2(new_data[1])


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


INPUT1 = "7,13,x,x,59,x,31,19"
INPUT2 = "17,x,13,19"
INPUT3 = "67,7,59,61"
INPUT4 = "67,x,7,59,61"
INPUT5 = "67,7,x,59,61"
INPUT6 = "1789,37,47,1889"


@pytest.mark.parametrize("inp, out",
                         (
                                 (INPUT1, 1068781),
                                 (INPUT2, 3417),
                                 (INPUT3, 754018),
                                 (INPUT4, 779210),
                                 (INPUT5, 1261476),
                                 (INPUT6, 1202161486),
                         )
                         )
def test_sol1(inp, out):
    assert sol2(inp) == out


# 90x =(11) 1
# extended_gcd(90,11)
# = extended_gcd(11, 2)
# = extended_gcd(2,1
if __name__ == '__main__':
    exit(main())
