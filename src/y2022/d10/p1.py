#!/usr/bin/env python3

from src.ext import IN


def six_signal_sum() -> int:
    register: int = 1
    cycle: int = 0

    expenses: dict[str, int] = {
        "noop": 1,
        "addx": 2,
    }

    breakpoints: dict[int, int | None] = {
        20: None,
        60: None,
        100: None,
        140: None,
        180: None,
        220: None,
    }

    for line in IN.splitlines():
        act: str = line.split()[0]
        cycle += expenses[act]

        for bp in breakpoints:
            if cycle >= bp and breakpoints[bp] is None:
                breakpoints[bp]: int = bp * register

        if act == "addx":
            register += int(line.split()[1])

    return sum([breakpoints[bp] for bp in breakpoints])


if __name__ == "__main__":
    print(six_signal_sum())
