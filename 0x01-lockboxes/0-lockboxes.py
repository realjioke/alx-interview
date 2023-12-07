#!/usr/bin/python3
""" Lets play a game of locked boxes """


def canUnlockAll(boxes):
    """ Can we unlock all the boxes, where boxes is a list of lists """

    bunch = list(range(1, len(boxes)))

    for key in bunch:
        found = False
        for idx, box in enumerate(boxes):
            if idx == key:
                continue
            if key in box:
                found = True
                break
        if not found:
            return False

    return True
