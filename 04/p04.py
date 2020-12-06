import re

with open("data.txt") as f:
    lines = [line.strip() for line in f.readlines()]


passports: list[dict[str, str]] = []
curr_passport: dict[str, str] = {}
for line in lines:
    if line == "":
        passports.append(curr_passport)
        curr_passport = {}
        continue

    kvs = line.split(" ")
    kvs = [kv.split(":") for kv in kvs]
    curr_passport.update({k: v for k, v in kvs})

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""
PASSPORT_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def _all_keys_cid_optional(passport: dict[str, str]) -> bool:
    return set(passport.keys()).issuperset(PASSPORT_KEYS)


def _byr_valid(passport: dict[str, str]) -> bool:
    try:
        return 1920 <= int(passport["byr"]) <= 2002
    except ValueError:
        return False


def _eyr_valid(passport: dict[str, str]) -> bool:
    try:
        return 2020 <= int(passport["eyr"]) <= 2030
    except ValueError:
        return False


def _iyr_valid(passport: dict[str, str]) -> bool:
    try:
        return 2010 <= int(passport["iyr"]) <= 2020
    except ValueError:
        return False


def _hgt_valid(passport: dict[str, str]) -> bool:
    hgt = passport["hgt"]
    value, unit = hgt[:-2], hgt[-2:]
    try:
        if unit == "cm":
            return 150 <= int(value) <= 193
        elif unit == "in":
            return 59 <= int(value) <= 76
        else:
            return False
    except ValueError:
        return False


def _hcl_valid(passport: dict[str, str]) -> bool:
    """a # followed by exactly six characters 0-9 or a-f."""
    hcl = passport["hcl"]
    return re.match(r"^#[0-9,a-f]{6}$", hcl) is not None


def _ecl_valid(passport: dict[str, str]) -> bool:
    valid_ecls = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    return passport["ecl"] in valid_ecls


def _pid_valid(passport: dict[str, str]) -> bool:
    try:
        return len(passport["pid"]) == 9 and int(passport["pid"]) >= 0
    except ValueError:
        return False


def valid_passport(passport: dict[str, str]) -> bool:
    rules = [
        _all_keys_cid_optional,
        _byr_valid,
        _eyr_valid,
        _iyr_valid,
        _hgt_valid,
        _hcl_valid,
        _ecl_valid,
        _pid_valid,
    ]

    return all(rule(passport) for rule in rules)


valid_passports = sum(1 for passport in passports if valid_passport(passport))
print(valid_passports)
