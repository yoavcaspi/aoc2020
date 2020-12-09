import argparse
from typing import List

import pytest


def nop(_acc, val):
    return _acc, 1


def acc(_acc, val):
    return _acc + val, 1


def jmp(_acc, val):
    return _acc, val


def sol(data: str) -> int:
    prog: list[tuple[str, int]] = []
    for line in data.splitlines():
        op, val = line.split()
        prog.append((op, int(val)))

    ops = {
        "nop": nop,
        "acc": acc,
        "jmp": jmp,
    }

    for i, (op, val) in enumerate(prog[:]):
        new_prog = prog[:]
        if op == "jmp":
            new_prog[i] = ("nop", val)
        elif op == "nop":
            new_prog[i] = ("jmp", val)
        else:
            continue
        acc_val = run_program(ops, new_prog)
        if acc_val != -1:
            return acc_val

    return -2


def run_program(ops, prog):
    global_acc = 0
    visited = set()
    index = 0
    while True:
        if index == len(prog):
            return global_acc
        if index in visited:
            return -1
        else:
            visited.add(index)

        op, val = prog[index]
        global_acc, new_index = ops[op](global_acc, val)
        index += new_index


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
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

@pytest.mark.parametrize("inp, out",
                         ((INPUT, 8),
                          )
                         )
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
