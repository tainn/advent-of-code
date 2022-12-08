#!/usr/bin/env python3

from src.ext import IN


def visible_trees() -> int:
    coordinate_heights: dict[str, int] = dict()

    for rowidx, row in enumerate(IN.splitlines()):
        for colidx, val in enumerate(row):
            coordinate_heights[f"{colidx}-{rowidx}"]: int = int(val)

    end: int = int(len(coordinate_heights) ** (1 / 2) - 1)
    visible: int = 0

    for point in coordinate_heights:
        x, y = map(int, point.split("-"))

        if x == 0 or y == 0 or x == end or y == end:
            visible += 1
            continue

        for left in range(x):
            if coordinate_heights[f"{left}-{y}"] >= coordinate_heights[point]:
                break
        else:
            visible += 1
            continue

        for right in range(x + 1, end + 1):
            if coordinate_heights[f"{right}-{y}"] >= coordinate_heights[point]:
                break
        else:
            visible += 1
            continue

        for up in range(y):
            if coordinate_heights[f"{x}-{up}"] >= coordinate_heights[point]:
                break
        else:
            visible += 1
            continue

        for down in range(y + 1, end + 1):
            if coordinate_heights[f"{x}-{down}"] >= coordinate_heights[point]:
                break
        else:
            visible += 1
            continue

    return visible


if __name__ == "__main__":
    print(visible_trees())
