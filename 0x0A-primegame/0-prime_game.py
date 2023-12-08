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


def find_prime(list_nums):
    """find_prime is a function to find a prime number in a list
    Returns:
        - index of the number or None
    """
    for i, num in enumerate(list_nums):
        if is_prime(num):
            return i


def isWinner(x, nums):
    """isWinner function
    Args:
        - x:  number of rounds
        - nums:  is an array of n elements
    Return:
        - the name of the player who won or None if it's even
    """
    if x < 1:
        return None
    maria_score = 0
    ben_score = 0
    who_plays = 1  # maria is odd numbers, ben is even numbers
    # go through number of rounds
    for i in range(x):
        round_numbers = list(range(1, nums[i] + 1))
        while len(round_numbers) != 1:
            index = find_prime(round_numbers)
            if index is not None:
                # remove prime and it's multiples
                prime = round_numbers.pop(index)
                multiple_indexes = get_index_of_multiples(prime, round_numbers)
                # transform multiples of the prime number into None
                for i in multiple_indexes:
                    round_numbers[i] = None
                # remove None from the list
                res = list(filter(
                    lambda item: item is not None, round_numbers))
                round_numbers = res
            else:
                break
            who_plays += 1
        # it means that Maria was the last one who could play
        if who_plays % 2 == 0:
            maria_score += 1
        # it means that Ben was the last one who could play
        elif who_plays % 2 == 1:
            ben_score += 1
        # restart for test purposes
        who_plays = 1
    if maria_score == ben_score:
        return None
    if maria_score > ben_score:
        return 'Maria'
    return 'Ben'
