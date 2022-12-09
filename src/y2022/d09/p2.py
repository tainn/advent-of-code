#!/usr/bin/env python3

from src.ext import IN


def ninetails_position_visits() -> int:
    pos: dict[int, list[int]] = {
        0: [0, 0],  # head
        1: [0, 0],
        2: [0, 0],
        3: [0, 0],
        4: [0, 0],
        5: [0, 0],
        6: [0, 0],
        7: [0, 0],
        8: [0, 0],
        9: [0, 0],  # true tail
    }
    all_true_tail_pos: set[tuple[int, ...]] = set()

    for move in IN.splitlines():
        mv_direction: str = move.split()[0]
        mv_amount: int = int(move.split()[1])

        for _ in range(mv_amount):

            match mv_direction:
                case "L":
                    pos[0][0] -= 1
                case "R":
                    pos[0][0] += 1
                case "D":
                    pos[0][1] -= 1
                case "U":
                    pos[0][1] += 1

            for idx in range(len(pos) - 1):
                # 2x2 head-tail diff
                if pos[idx][0] - pos[idx + 1][0] == 2 and pos[idx][1] - pos[idx + 1][1] == 2:
                    pos[idx + 1][0] += 1
                    pos[idx + 1][1] += 1

                elif pos[idx][0] - pos[idx + 1][0] == 2 and pos[idx][1] - pos[idx + 1][1] == -2:
                    pos[idx + 1][0] += 1
                    pos[idx + 1][1] -= 1

                elif pos[idx][0] - pos[idx + 1][0] == -2 and pos[idx][1] - pos[idx + 1][1] == 2:
                    pos[idx + 1][0] -= 1
                    pos[idx + 1][1] += 1

                elif pos[idx][0] - pos[idx + 1][0] == -2 and pos[idx][1] - pos[idx + 1][1] == -2:
                    pos[idx + 1][0] -= 1
                    pos[idx + 1][1] -= 1

                # 2x1 or 2x0 head-tail diff
                elif pos[idx][0] - pos[idx + 1][0] == 2:
                    pos[idx + 1][0] += 1
                    pos[idx + 1][1]: int = pos[idx][1]

                elif pos[idx][0] - pos[idx + 1][0] == -2:
                    pos[idx + 1][0] -= 1
                    pos[idx + 1][1]: int = pos[idx][1]

                elif pos[idx][1] - pos[idx + 1][1] == 2:
                    pos[idx + 1][1] += 1
                    pos[idx + 1][0]: int = pos[idx][0]

                elif pos[idx][1] - pos[idx + 1][1] == -2:
                    pos[idx + 1][1] -= 1
                    pos[idx + 1][0]: int = pos[idx][0]

            all_true_tail_pos.add(tuple(pos[9]))

    return len(all_true_tail_pos)


if __name__ == "__main__":
    print(ninetails_position_visits())
