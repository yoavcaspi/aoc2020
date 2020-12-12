import argparse
from collections import Counter
from typing import List, Dict, Tuple

import pytest


def count_occupied_seats(x, y, board):
    adjecents_places = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    )
    count = 0
    for vec_x, vec_y in adjecents_places:
        adj_x = x + vec_x
        adj_y = y + vec_y
        adjecent_chair = board.get((adj_x, adj_y), None)
        while adjecent_chair is not None:
            if adjecent_chair == "L":
                break
            if adjecent_chair == "#":
                count += 1
                break
            adj_x += vec_x
            adj_y += vec_y
            adjecent_chair = board.get((adj_x, adj_y), None)
    return count


def run_rules(board: Dict[Tuple[int, int], str]):
    new_board = {}
    for (x, y), chair in board.items():
        if chair == ".":
            new_board[(x, y)] = chair
            continue
        occupied_seats = count_occupied_seats(x, y, board)
        if chair == "L" and occupied_seats == 0:
            new_board[(x, y)] = "#"
        elif chair == "#" and occupied_seats >= 5:
            new_board[(x, y)] = "L"
        else:
            new_board[(x, y)] = chair
    return new_board


def print_board(board, x, y):
    print()
    for j in range(y+1):
        for i in range(x+1):
            print(board[(i, j)], end="")
        print()
    print("\n\n\n\n")


def sol(data: str) -> int:
    board: Dict[Tuple[int, int], str] = {}
    for y, line in enumerate(data.splitlines()):
        for x, char in enumerate(line):
            board[x, y] = char

    while True:
        # print_board(board, x, y)
        new_board = run_rules(board)
        if board == new_board:
            return Counter(board.values()).get("#")
        board = new_board.copy()


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
#                                  (INPUT, 26),
#                          )
#                          )
# def test_sol1(inp, out):
#     assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
