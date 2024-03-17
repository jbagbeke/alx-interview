#!/usr/bin/python3
"""
Locakboxes problem solution
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    """
    if len(boxes) == 0 or not boxes:
        print('1')
        return False

    visitedBoxes = [0]
    expectedKeys = [i for i in range(len(boxes))]

    for thisBox in boxes:
        if len(thisBox) == 0:
            truthVal = (sorted(visitedBoxes) == expectedKeys)
            return truthVal

        for boxKey in thisBox:
            if boxKey >= len(boxes):
                continue
            if boxKey not in visitedBoxes:
                visitedBoxes.append(boxKey)
    truthVal = (sorted(visitedBoxes) == expectedKeys)
    return truthVal
