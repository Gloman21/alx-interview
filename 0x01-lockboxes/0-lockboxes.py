#!/usr/bin/python3
"""
you have n and it is the number of locked boxes in front of you.
each one of these box is numbered sequentially
from 0 to n - 1 and each box may
contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
     a method to determine if all the boxes can be opened.

    :param boxes:
    :return: True or False
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False