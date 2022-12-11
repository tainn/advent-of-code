#!/usr/bin/env python3

from collections import defaultdict


def monkey_business() -> int:
    # order: operation > floor 3 division > test

    # initial inventory state
    monkey_inv: dict[int, list[int]] = {
        0: [89, 74],
        1: [75, 69, 87, 57, 84, 90, 66, 50],
        2: [55],
        3: [69, 82, 69, 56, 68],
        4: [72, 97, 50],
        5: [90, 84, 56, 92, 91, 91],
        6: [63, 93, 55, 53],
        7: [50, 61, 52, 58, 86, 68, 97],
    }

    monkey_inspect: defaultdict[int, int] = defaultdict(int)
    remove_stack: list[int] = []

    for round_ in range(20):
        for monkey in range(8):
            for item in monkey_inv[monkey]:
                monkey_inspect[monkey] += 1

                monkey_op: int = monkey_operation(monkey, item)
                relief: int = monkey_op // 3
                throw_to: int = monkey_test_throw(monkey, relief)

                monkey_inv[throw_to].append(relief)
                remove_stack.append(item)

            for item in remove_stack:
                monkey_inv[monkey].remove(item)

            remove_stack.clear()

    max_monkey: int = max(monkey_inspect, key=monkey_inspect.get)
    max_inspect: int = monkey_inspect[max_monkey]
    monkey_inspect[max_monkey]: int = 0
    second_max_inspect: int = monkey_inspect[max(monkey_inspect, key=monkey_inspect.get)]

    return max_inspect * second_max_inspect


def monkey_operation(monkey: int, old: int) -> int:
    monkey_ops: dict[int, int] = {
        0: old * 5,
        1: old + 3,
        2: old + 7,
        3: old + 5,
        4: old + 2,
        5: old * 19,
        6: old * old,
        7: old + 4,
    }

    return monkey_ops[monkey]


def monkey_test_throw(monkey: int, relief: int) -> int:
    monkey_test: dict[int, bool] = {
        0: relief % 17 == 0,
        1: relief % 7 == 0,
        2: relief % 13 == 0,
        3: relief % 2 == 0,
        4: relief % 19 == 0,
        5: relief % 3 == 0,
        6: relief % 5 == 0,
        7: relief % 11 == 0,
    }

    monkey_throw: dict[int, int] = {
        0: 4 if monkey_test[0] else 7,
        1: 3 if monkey_test[1] else 2,
        2: 0 if monkey_test[2] else 7,
        3: 0 if monkey_test[3] else 2,
        4: 6 if monkey_test[4] else 5,
        5: 6 if monkey_test[5] else 1,
        6: 3 if monkey_test[6] else 1,
        7: 5 if monkey_test[7] else 4,
    }

    return monkey_throw[monkey]


if __name__ == "__main__":
    print(monkey_business())
