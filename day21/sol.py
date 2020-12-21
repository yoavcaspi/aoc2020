import argparse
from collections import defaultdict, Counter

import pytest


def sol(data: str) -> int:
    allergens_data: dict[str, set[str]] = {}
    all_ingredients: Counter[str, int] = Counter()
    for line in data.splitlines():
        line = line.strip(")")
        raw_ingredients, raw_allergens = line.split(" (contains ")
        allergens = frozenset(raw_allergens.split(", "))
        ingredients = set(raw_ingredients.split(" "))
        all_ingredients.update(ingredients)
        for allergen in allergens:
            if allergen not in allergens_data.keys():
                allergens_data[allergen] = set(ingredients)
            else:
                allergens_data[allergen] &= ingredients

    allergens_ingredients = defaultdict()
    while len([val for val in allergens_data.values() if len(val) > 1]):
        for key, val in list(allergens_data.items()):
            if len(val) == 1:
                real_val, = val
                allergens_ingredients[key] = real_val
                for key2, val2 in allergens_data.items():
                    if key2 == key:
                        continue
                    val2 -= val
                del allergens_data[key]
    res = sum(c for ing, c in all_ingredients.items()
              if ing not in allergens_ingredients.values())
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
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""


# @pytest.mark.parametrize(
#     "inp, out",
#     (
#             (INPUT, 5),
#     )
# )
# def test_sol1(inp, out):
#     assert sol(inp) == out


# answer is 2075
if __name__ == '__main__':
    exit(main())
