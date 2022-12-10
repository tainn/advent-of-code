#!/usr/bin/env python3

from src.ext import IN


def eight_capital_letters() -> str:
    # order: cycle increment > draw pixel > addx
    register: int = 1
    cycle: int = 0
    display: str = ""

    expenses: dict[str, int] = {
        "noop": 1,
        "addx": 2,
    }

    for line in IN.splitlines():
        act: str = line.split()[0]

        for _ in range(expenses[act]):
            cycle += 1

            if (cycle - 1) % 40 == 0:
                display += "\n"
                cycle: int = 1

            sprite_pos: tuple = register - 1, register, register + 1
            display += "#" if cycle - 1 in sprite_pos else "."

        if act == "addx":
            register += int(line.split()[1])

    return display


if __name__ == "__main__":
    print(eight_capital_letters())
