#!/usr/bin/env python3

from p1 import core_map_process


def remove_single_dir() -> int:
    core_map: dict[str, int] = core_map_process()

    total_disk: int = 70_000_000
    needed_disk: int = 30_000_000
    used_disk: int = core_map["root"]
    free_disk: int = total_disk - used_disk
    to_delete: int = needed_disk - free_disk

    big_enough_sizes: list[int] = []

    for size in core_map.values():
        if size - to_delete >= 0:
            big_enough_sizes.append(size)

    return min(big_enough_sizes)


if __name__ == "__main__":
    print(remove_single_dir())
