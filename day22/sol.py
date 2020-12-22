import argparse
from collections import deque


def calculate_sum(player_dec: deque[int]) -> int:
    res = 0
    player_dec.reverse()
    for i, card in enumerate(player_dec, 1):
        res += i * card
    return res


def sol(data: str) -> int:
    raw_player1, raw_player2 = data.split("\n\n", 2)
    player1_deck: deque[int] = deque()
    for card in raw_player1.splitlines()[1:]:
        player1_deck.append(int(card))
    player2_deck: deque[int] = deque()
    for card in raw_player2.splitlines()[1:]:
        player2_deck.append(int(card))

    while len(player1_deck) > 0 and len(player2_deck) > 0:
        card1 = player1_deck.popleft()
        card2 = player2_deck.popleft()
        if card1 > card2:
            player1_deck.append(card1)
            player1_deck.append(card2)
        else:
            player2_deck.append(card2)
            player2_deck.append(card1)
    return calculate_sum(player1_deck) + calculate_sum(player2_deck)


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

# @pytest.mark.parametrize(
#     "inp, out",
#     (
#             (INPUT, 306),
#     )
# )
# def test_sol1(inp, out):
#     assert sol(inp) == out


# answer is 2075
if __name__ == '__main__':
    exit(main())
