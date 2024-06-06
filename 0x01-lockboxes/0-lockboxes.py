#!/usr/bin/python3
"""
This module provides a function to determine if all boxes can be unlocked.
"""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """
    Determines if all the boxes can be opened.

    :param boxes: A list of lists, where each list contains keys to other boxes.
    :return: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)
