import argparse
import re
from typing import List, Dict

import pytest

ALL_KEYS = {
    "byr",  # (Birth Year)
    "iyr",  # (Issue Year)
    "eyr",  # (Expiration Year)
    "hgt",  # (Height)
    "hcl",  # (Hair Color)
    "ecl",  # (Eye Color)
    "pid",  # (Passport ID)
    # "cid", # (Country ID)
}

hcl_regex = re.compile("^#[0-9a-f]{6}$")
pid_regex = re.compile("^[0-9]{9}$")
ecl_colors = {*"amb blu brn gry grn hzl oth".split(" ")}


def byr_is_valid(value):
    return 1920 <= int(value) <= 2002


def iyr_is_valid(value):
    return 2002 <= int(value) <= 2020


def eyr_is_valid(value):
    return 2020 <= int(value) <= 2030


def hgt_is_valid(value):
    if value.endswith("cm"):
        height = int(value[:-2])
        return 150 <= height <= 193
    elif value.endswith("in"):
        height = int(value[:-2])
        return 59 <= height <= 76
    else:
        return False


def hcl_is_valid(value):
    return hcl_regex.match(value) is not None


def ecl_is_valid(value):
    return value in ecl_colors


def pid_is_valid(value):
    return pid_regex.match(value) is not None


def passport_valid(passport):
    return \
        (byr_is_valid(passport["byr"]) and  # (Birth Year)
         iyr_is_valid(passport["iyr"]) and  # (Issue Year)
         eyr_is_valid(passport["eyr"]) and  # (Expiration Year)
         hgt_is_valid(passport["hgt"]) and  # (Height)
         hcl_is_valid(passport["hcl"]) and  # (Hair Color)
         ecl_is_valid(passport["ecl"]) and  # (Eye Color)
         pid_is_valid(passport["pid"]) # (Passport ID)
         )


def sol(data: List[str]) -> int:
    passport: Dict[str, str] = {}
    count: int = 0
    for line in data:
        line = line.strip("\n")
        if line in ["\n", ""]:
            if set(passport.keys()).issuperset(ALL_KEYS):
                if passport_valid(passport):
                    count += 1
            passport = {}

        else:
            passport.update({pair.split(":")[0]: pair.split(":")[1] for pair in
                             line.split(" ")})
    return count


def get_input(filename: str) -> List[str]:
    with open(filename) as f:
        lines = f.readlines()
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--filename', default='input.txt')
    args = parser.parse_args()
    data = get_input(args.filename)
    print(sol(data))
    return 0


INPUT_BAD = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""

INPUT_GOOD = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


# @pytest.mark.parametrize("inp, out",
#                          ((INPUT_BAD, 0),
#                          (INPUT_GOOD, 4),
#                           )
# )
# def test_sol1(inp, out):
#     assert sol(inp.splitlines()) == out


if __name__ == '__main__':
    exit(main())
