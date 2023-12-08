#!/usr/bin/python3
"""0-prime_game module
"""


def is_prime(n):
    """is_prime function verifies if n is a prime number
    """
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def get_index_of_multiples(n, nums):
    """get_multiples of n in the nums list
    """
    return [i for i, x in enumerate(nums) if x is not None and x % n == 0]


def isWinner(x, nums):
    """isWinner function
    Args:
        - x:  number of rounds
        - nums:  is an array of n elements
    Return:
        - the name of the player who won or None if it's even
    """
    return None
