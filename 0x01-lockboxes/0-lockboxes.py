#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """Method that verifies if all
    Boxes can be unlocked
        - Return:
            - true -> when all can be unlock
            - false -> when we cant
    """
    size = len(boxes)
    print(boxes[0])
    goNext(boxes[0], boxes)
    return True

def goNext(box, boxes):
    """test"""
    if len(box) == 0:
        return 0
    next_box = boxes[box.pop(0)]
    # next_box = boxes[box[0]]
    # print(box)
    print(next_box)
    goNext(next_box, boxes)