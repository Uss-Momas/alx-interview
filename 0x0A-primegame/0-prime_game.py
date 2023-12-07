#!/usr/bin/python3
"""0-prime_game module
"""


def is_prime(num):
    """is_prime function
    """
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Check divisibility up to the square root of the number
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


def isWinner(x, nums):
    """isWinner function
    Args:
        - x:  number of rounds
        - nums:  is an array of n elements
    Return:
        - the name of the player who won or None if it's even
    """
    return None
