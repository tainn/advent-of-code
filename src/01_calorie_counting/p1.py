#!/usr/bin/env python3

from collections import defaultdict


def elves_to_calories() -> defaultdict:
    with open("input", "r") as rf:
        data: str = rf.read().strip()

    elves: defaultdict = defaultdict(list)
    elf_no: int = 1

    for line in data.splitlines():
        if not line:
            elf_no += 1
            continue

        elves[f"elf{elf_no}"].append(int(line))

    return elves


def most_calories_carried(elves: defaultdict) -> int:
    return sum(max(elves.values(), key=sum))


if __name__ == "__main__":
    print(most_calories_carried(elves_to_calories()))
