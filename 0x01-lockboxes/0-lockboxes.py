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
    # Mark as False all the nodes
    visited = [False] * len(boxes)
    queue = []
    # The first Node is 0
    queue.append(0)
    # Mark the first node has visited
    visited[0] = True
    # count of the number of nodes that are visited during BFS
    count = 0
    while len(queue) > 0:
        current_node = queue.pop(0)
        count = count + 1
        for j in boxes[current_node]:
            # node was not explored
            if visited[j] is False:
                queue.append(j)
                visited[j] = True
    if count == len(boxes):
        return True
    return False
