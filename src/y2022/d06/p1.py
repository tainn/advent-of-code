#!/usr/bin/env python3

from src.ext import IN


def detect_first_marker(chunk: int) -> int:
    for idx, _ in enumerate(IN):
        if len(set(IN[idx : idx + chunk])) == chunk:
            return idx + chunk


if __name__ == "__main__":
    print(detect_first_marker(4))
