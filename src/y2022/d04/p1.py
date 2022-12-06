#!/usr/bin/env python3

from src.ext import IN


def fully_overlapping() -> int:
    counter: int = 0

    for pair in IN.splitlines():
        part1, part2 = pair.split(",")
        (part1s, part1e), (part2s, part2e) = (
            map(int, part1.split("-")),
            map(int, part2.split("-")),
        )

        contain1: bool = part1s <= part2s and part1e >= part2e
        contain2: bool = part1s >= part2s and part1e <= part2e

        if contain1 or contain2:
            counter += 1

    return counter


if __name__ == "__main__":
    print(fully_overlapping())
