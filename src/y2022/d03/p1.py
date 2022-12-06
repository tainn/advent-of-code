#!/usr/bin/env python3

import string

from src.ext import IN


def shared_item_per_rucksack() -> list[str]:
    shared_items: list[str] = []

    for rucksack in IN.splitlines():
        compart1, compart2 = (
            rucksack[: len(rucksack) // 2],
            rucksack[len(rucksack) // 2 :],
        )
        shared_item: str = set(compart1).intersection(set(compart2)).pop()
        shared_items.append(shared_item)

    return shared_items


def priority_sum(shared_items: list[str]) -> int:
    total: int = 0

    for item in shared_items:
        total += string.ascii_letters.index(item) + 1

    return total


if __name__ == "__main__":
    print(priority_sum(shared_item_per_rucksack()))
