#!/usr/bin/env python3

from p1 import CRATE_STRUCT


def stack_top_crates_mult() -> str:
    with open("input", "r") as rf:
        data: str = rf.read().strip()

    for line in data.splitlines():
        cuts: list[str] = line.split()
        quantity, from_stack, to_stack = (
            int(cuts[1]),
            int(cuts[3]),
            int(cuts[5]),
        )

        crates: list[str] = CRATE_STRUCT[from_stack][-quantity:]
        CRATE_STRUCT[to_stack].extend(crates)
        CRATE_STRUCT[from_stack]: list[str] = CRATE_STRUCT[from_stack][:-quantity]

    build: str = ""

    for stack in CRATE_STRUCT:
        build += CRATE_STRUCT[stack][-1]

    return build


if __name__ == "__main__":
    print(stack_top_crates_mult())
