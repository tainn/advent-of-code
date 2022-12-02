#!/usr/bin/env python3

from p1 import rps_score_if_followed

OUTCOMES: dict[str: int] = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

if __name__ == "__main__":
    print(rps_score_if_followed(OUTCOMES))
