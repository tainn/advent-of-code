#!/usr/bin/env python3


def detect_first_marker(chunk: int) -> int:
    with open("input", "r") as rf:
        data: str = rf.read().strip()

    for idx, _ in enumerate(data):
        if len(set(data[idx : idx + chunk])) == chunk:
            return idx + chunk


if __name__ == "__main__":
    print(detect_first_marker(4))
