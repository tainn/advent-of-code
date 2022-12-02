#!/usr/bin/env python3

OUTCOMES: dict = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}


def rps_score_if_followed(outcomes: dict) -> int:
    with open("input", "r") as rf:
        data: str = rf.read().strip()

    total: int = 0

    for play in data.splitlines():
        total += outcomes[play]

    return total


if __name__ == "__main__":
    print(rps_score_if_followed(OUTCOMES))
