import argparse
from collections import deque

import pytest


def calculate_sum(player_dec: deque[int]) -> int:
    res = 0
    player_dec.reverse()
    for i, card in enumerate(player_dec, 1):
        res += i * card
    return res


def play_game(player1_deck, player2_deck) -> tuple[int, int]:
    prev_rounds: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
    i = 1
    while len(player1_deck) > 0 and len(player2_deck) > 0:
        current_round = (tuple(player1_deck), tuple(player2_deck))
        if current_round in prev_rounds:
            return 1, calculate_sum(player1_deck)
        card1 = player1_deck.popleft()
        card2 = player2_deck.popleft()
        prev_rounds.add(current_round)
        if card1 <= len(player1_deck) and card2 <= len(player2_deck):
            new_player1_deck = deque(player1_deck)
            new_player2_deck = deque(player2_deck)
            while len(new_player1_deck) > card1:
                new_player1_deck.pop()
            while len(new_player2_deck) > card2:
                new_player2_deck.pop()

            winner, _ = play_game(new_player1_deck, new_player2_deck)
            if winner == 1:
                player1_deck.append(card1)
                player1_deck.append(card2)
            else:
                player2_deck.append(card2)
                player2_deck.append(card1)

        else:
            if card1 > card2:
                player1_deck.append(card1)
                player1_deck.append(card2)
            else:
                player2_deck.append(card2)
                player2_deck.append(card1)
        i += 1
    if len(player1_deck) > 0:
        return 1, calculate_sum(player1_deck)
    else:
        return 2, calculate_sum(player2_deck)


def sol(data: str) -> int:
    raw_player1, raw_player2 = data.split("\n\n", 2)
    player1_deck: deque[int] = deque()
    for card in raw_player1.splitlines()[1:]:
        player1_deck.append(int(card))
    player2_deck: deque[int] = deque()
    for card in raw_player2.splitlines()[1:]:
        player2_deck.append(int(card))
    _, res = play_game(deque(player1_deck), deque(player2_deck))
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
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
"""


@pytest.mark.parametrize(
    "inp, out",
    (
            (INPUT, 291),
    )
)
def test_sol1(inp, out):
    assert sol(inp) == out


if __name__ == '__main__':
    exit(main())
