#!/usr/bin/env python3

from collections import defaultdict

from src.ext import IN


def elves_to_calories() -> defaultdict:
    elves: defaultdict = defaultdict(list)
    elf_no: int = 1

    for line in IN.splitlines():
        if not line:
            elf_no += 1
            continue

        elves[f"elf{elf_no}"].append(int(line))

    return elves


def most_calories_carried(elves: defaultdict) -> int:
    return sum(max(elves.values(), key=sum))


if __name__ == "__main__":
    print(most_calories_carried(elves_to_calories()))
