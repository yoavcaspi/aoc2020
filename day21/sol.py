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

    ing_counter = defaultdict(int)
    for val in allergens_data.values():
        for ing in val:
            ing_counter[ing] += 1
    ing_order = sorted([(k, v) for k, v in ing_counter.items()],
                       key=lambda x: x[1])
    allergens_ingredients_final = defaultdict(set)
    for ing, _ in ing_order:
        for key, val in allergens_data.items():
            if ing in val:
                allergens_data[key] = {ing}
                allergens_ingredients_final[key] = ing
                break
    return sum(c for ing, c in all_ingredients.items()
               if ing not in allergens_ingredients_final.values())


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


@pytest.mark.parametrize(
    "inp, out",
    (
            (INPUT, 5),
    )
)
def test_sol1(inp, out):
    assert sol(inp) == out


# answer is 2075
if __name__ == '__main__':
    exit(main())
