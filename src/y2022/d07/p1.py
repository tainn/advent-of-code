#!/usr/bin/env python3

import os
import shutil
from collections import defaultdict
from pathlib import Path

from src.ext import IN


def small_dirs_sum() -> int:
    core_map: dict[str, int] = core_map_process()

    total_size: int = 0

    for size in core_map.values():
        if size <= 100_000:
            total_size += size

    return total_size


def core_map_process(cleanup: bool = True) -> dict[str, int]:
    init_path: Path = Path(os.getcwd())
    create_fs_struct(init_path)
    core_map: dict[str, int] = get_core_map(init_path)

    if cleanup:
        shutil.rmtree(init_path / "root")

    return core_map


def create_fs_struct(init_path: Path) -> None:
    curr_path: Path = Path(os.getcwd())

    for line in IN.splitlines():
        linetype: str = line_type(line)

        if linetype == "cd":
            dst: str = line.split()[2] if line.split()[2] != "/" else "root"

            if dst == "..":
                os.chdir("..")
                curr_path: Path = Path(os.getcwd())

            else:
                Path(curr_path / dst).mkdir(exist_ok=True)
                os.chdir(curr_path / dst)
                curr_path: Path = Path(os.getcwd())

        if linetype == "file":
            size = line.split()[0]
            Path(curr_path / size).touch(exist_ok=True)

    os.chdir(init_path)


def line_type(line: str) -> str:
    if line.startswith("$"):
        if line.split()[1] == "cd":
            return "cd"
        elif line.split()[1] == "ls":
            return "ls"

    elif line.split()[0] == "dir":
        return "dir"

    elif line.split()[0].isdigit():
        return "file"


def get_core_map(init_path: Path) -> dict[str, int]:
    flat_map: dict[str, int] = defaultdict(int)

    for root, _, files in os.walk(init_path / "root"):
        local_root: str = root.replace(f"{str(init_path)}/", "")
        filesizes: int = sum(map(int, files))
        flat_map[local_root] += filesizes

        for key in flat_map:
            if key in local_root and key != local_root:
                flat_map[key] += filesizes

    return flat_map


if __name__ == "__main__":
    print(small_dirs_sum())
