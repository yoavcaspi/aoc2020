import argparse
from collections import Counter
from typing import List, Dict, Tuple

import pytest


def count_occupied_seats(x, y, board):
    adjecents_places = (
        (x-1, y-1),
        (x-1, y),
        (x-1, y+1),
        (x, y-1),
        (x, y+1),
        (x+1, y-1),
        (x+1, y),
        (x+1, y+1),
    )
    count = 0
    for adj_x, adj_y in adjecents_places:
        adjecent_chair = board.get((adj_x, adj_y), ".")
        if adjecent_chair == "#":
            count+=1
    return count

def run_rules(board: Dict[Tuple[int, int], str]):
    new_board = {}
    for (x, y), chair in board.items():
        if chair == ".":
            new_board[(x, y)] = chair
        occupied_seats = count_occupied_seats(x, y, board)
        if chair == "L" and occupied_seats == 0:
            new_board[(x, y)] = "#"
        elif chair == "#" and occupied_seats >= 4:
            new_board[(x, y)] = "L"
        else:
            new_board[(x, y)] = chair
    return new_board


def sol(data: str) -> int:
    board: Dict[Tuple[int, int], str] = {}
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            board[x, y] = char

    while True:
        new_board = run_rules(board)
        if board == new_board:
            return Counter(board.values()).get("#")
        board = new_board

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
L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
"""


# @pytest.mark.parametrize("inp, out",
#                          (
#                                  (INPUT, 37),
#                          )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
