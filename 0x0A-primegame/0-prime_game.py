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
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [x for x in range(2, n + 1) if is_prime(x)]

        maria_moves = True
        while primes:
            prime = primes.pop(0)
            nums = [x for x in nums if x % prime != 0]

            if not nums:  # No more numbers left
                if maria_moves:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            maria_moves = not maria_moves

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    return None
