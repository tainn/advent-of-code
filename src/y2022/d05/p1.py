#!/usr/bin/env python3

"""
Initial crate structure:

[H]                 [Z]         [J]
[L]     [W] [B]     [G]         [R]
[R]     [G] [S]     [J] [H]     [Q]
[F]     [N] [T] [J] [P] [R]     [F]
[B]     [C] [M] [R] [Q] [F] [G] [P]
[C] [D] [F] [D] [D] [D] [T] [M] [G]
[J] [C] [J] [J] [C] [L] [Z] [V] [B]
[M] [Z] [H] [P] [N] [W] [P] [L] [C]
 1   2   3   4   5   6   7   8   9
"""

CRATE_STRUCT: dict[int, list[str]] = {
    1: ["M", "J", "C", "B", "F", "R", "L", "H"],
    2: ["Z", "C", "D"],
    3: ["H", "J", "F", "C", "N", "G", "W"],
    4: ["P", "J", "D", "M", "T", "S", "B"],
    5: ["N", "C", "D", "R", "J"],
    6: ["W", "L", "D", "Q", "P", "J", "G", "Z"],
    7: ["P", "Z", "T", "F", "R", "H"],
    8: ["L", "V", "M", "G"],
    9: ["C", "B", "G", "P", "F", "Q", "R", "J"],
}


def stack_top_crates() -> str:
    with open("input", "r") as rf:
        data: str = rf.read().strip()

    for line in data.splitlines():
        cuts: list[str] = line.split()
        quantity, from_stack, to_stack = (
            int(cuts[1]),
            int(cuts[3]),
            int(cuts[5]),
        )

        for idx in range(quantity):
            crate: str = CRATE_STRUCT[from_stack].pop()
            CRATE_STRUCT[to_stack].append(crate)

    build: str = ""

    for stack in CRATE_STRUCT:
        build += CRATE_STRUCT[stack][-1]

    return build


if __name__ == "__main__":
    print(stack_top_crates())
