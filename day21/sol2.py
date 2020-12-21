import argparse
from collections import Counter


def sol(data: str) -> str:
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

    allergens_ingredients: dict[str, str] = {}
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
    allerg = sorted(
        list(val for key, val in allergens_ingredients.items()),
        key=lambda x: x[0])
    return ",".join(allerg)


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
#             (INPUT, "mxmxvkd,sqjhc,fvjkl"),
#     )
# )
# def test_sol1(inp, out):
#     assert sol(inp) == out


# 1835 is low
# 1902 is low
# 2037 is low
if __name__ == '__main__':
    exit(main())
