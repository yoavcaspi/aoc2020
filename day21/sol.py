import argparse
from collections import defaultdict

import pytest


def sol(data: str) -> int:
    allergens_data: dict[frozenset[str], set[str]] = {}
    foods_data: list[set[str]] = []
    all_ingredients: dict[str, int] = defaultdict(int)
    for line in data.splitlines():
        line = line.strip(")")
        raw_ingredients, raw_allergens = line.split(" (contains ")
        allergens = frozenset(raw_allergens.split(", "))
        ingredients = set(raw_ingredients.split(" "))
        foods_data.append(ingredients)
        for ing in ingredients:
            all_ingredients[ing] += 1

        if allergens not in allergens_data.keys():
            allergens_data[allergens] = ingredients
        else:
            allergens_data[allergens] &= ingredients

    allergens_ingredients: dict[str, set[str]] = defaultdict(set)
    keys_witn_one = [key for key in allergens_data.keys() if len(key) == 1]
    for key in keys_witn_one:
        real_key, = key
        allergens_ingredients[real_key] = set(allergens_data[key])
        relevant_ingrediants = [value for key2, value in allergens_data.items()
                                if
                                key.issubset(key2)]
        for value in relevant_ingrediants:
            allergens_ingredients[real_key] &= value

    ing_counter = defaultdict(int)
    for val in allergens_ingredients.values():
        for ing in val:
            ing_counter[ing] += 1
    ing_order = sorted([(k, v) for k, v in ing_counter.items()],
                       key=lambda x: x[1])
    allergens_ingredients_final = defaultdict(set)
    for ing, _ in ing_order:
        for key, val in allergens_ingredients.items():
            if ing in val:
                allergens_ingredients[key] = {ing}
                allergens_ingredients_final[key] = ing
                break
    count = 0
    for ing, c in all_ingredients.items():
        if ing not in allergens_ingredients_final.values():
            count += c
    return count


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
