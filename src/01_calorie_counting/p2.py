#!/usr/bin/env python3

from collections import defaultdict

from p1 import elves_to_calories


def n_most_calories_carried(elves: defaultdict, n: int) -> int:
    collect: list = []

    for idx in range(n):
        curr_max_elf: str = max(elves, key=lambda x: sum(elves[x]))
        curr_max: int = sum(elves[curr_max_elf])
        collect.append(curr_max)
        del elves[curr_max_elf]

    return sum(collect)


if __name__ == "__main__":
    print(n_most_calories_carried(elves_to_calories(), 3))
