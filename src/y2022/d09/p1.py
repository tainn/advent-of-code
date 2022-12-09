#!/usr/bin/env python3

from src.ext import IN


def tail_position_visits() -> int:
    head_pos: list[int] = [0, 0]
    tail_pos: list[int] = [0, 0]
    all_tail_pos: set[tuple[int, ...]] = set()

    for move in IN.splitlines():
        mv_direction: str = move.split()[0]
        mv_amount: int = int(move.split()[1])

        for _ in range(1, mv_amount + 1):

            match mv_direction:
                case "L":
                    head_pos[0] -= 1
                case "R":
                    head_pos[0] += 1
                case "D":
                    head_pos[1] -= 1
                case "U":
                    head_pos[1] += 1

            if head_pos[0] - tail_pos[0] == 2:
                tail_pos[0] += 1
                tail_pos[1]: int = head_pos[1]

            elif head_pos[0] - tail_pos[0] == -2:
                tail_pos[0] -= 1
                tail_pos[1]: int = head_pos[1]

            elif head_pos[1] - tail_pos[1] == 2:
                tail_pos[1] += 1
                tail_pos[0]: int = head_pos[0]

            elif head_pos[1] - tail_pos[1] == -2:
                tail_pos[1] -= 1
                tail_pos[0]: int = head_pos[0]

            all_tail_pos.add(tuple(tail_pos))

    return len(all_tail_pos)


if __name__ == "__main__":
    print(tail_position_visits())
