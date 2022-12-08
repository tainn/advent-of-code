#!/usr/bin/env python3

from src.ext import IN


def highest_scenic_score() -> int:
    coordinate_heights: dict[str, int] = dict()

    for rowidx, row in enumerate(IN.splitlines()):
        for colidx, val in enumerate(row):
            coordinate_heights[f"{colidx}-{rowidx}"]: int = int(val)

    end: int = int(len(coordinate_heights) ** (1 / 2) - 1)
    high_scenic: int = 0

    for point in coordinate_heights:
        x, y = map(int, point.split("-"))

        left_scenic: int = 0
        right_scenic: int = 0
        up_scenic: int = 0
        down_scenic: int = 0

        for left in range(x)[::-1]:
            if coordinate_heights[f"{left}-{y}"] < coordinate_heights[point]:
                left_scenic += 1
            else:
                left_scenic += 1
                break

        for right in range(x + 1, end + 1):
            if coordinate_heights[f"{right}-{y}"] < coordinate_heights[point]:
                right_scenic += 1
            else:
                right_scenic += 1
                break

        for up in range(y)[::-1]:
            if coordinate_heights[f"{x}-{up}"] < coordinate_heights[point]:
                up_scenic += 1
            else:
                up_scenic += 1
                break

        for down in range(y + 1, end + 1):
            if coordinate_heights[f"{x}-{down}"] < coordinate_heights[point]:
                down_scenic += 1
            else:
                down_scenic += 1
                break

        scenic_mult: int = left_scenic * right_scenic * up_scenic * down_scenic

        if scenic_mult > high_scenic:
            high_scenic: int = scenic_mult

    return high_scenic


if __name__ == "__main__":
    print(highest_scenic_score())
