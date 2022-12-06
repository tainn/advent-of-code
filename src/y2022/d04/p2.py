#!/usr/bin/env python3

from src.ext import IN


def overlapping() -> int:
    counter: int = 0

    for pair in IN.splitlines():
        part1, part2 = pair.split(",")
        (part1s, part1e), (part2s, part2e) = (
            map(int, part1.split("-")),
            map(int, part2.split("-")),
        )

        linear1: bool = part1e < part2s and part1s < part2e
        linear2: bool = part1e > part2s and part1s > part2e

        if not linear1 and not linear2:
            counter += 1

    return counter


if __name__ == "__main__":
    print(overlapping())
