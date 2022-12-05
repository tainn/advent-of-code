#!/usr/bin/env python3

from p1 import priority_sum


def group_badge_items() -> list[str]:
    with open("input", "r") as rf:
        data: str = rf.read().strip()

    badge_items: list[str] = []
    curr_rucksacks: list[set] = []

    for rucksack in data.splitlines():
        curr_rucksacks.append(set(rucksack))

        if len(curr_rucksacks) == 3:
            badge_items.append(curr_rucksacks[0].intersection(*curr_rucksacks[1:]).pop())
            curr_rucksacks.clear()

    return badge_items


if __name__ == "__main__":
    print(priority_sum(group_badge_items()))
