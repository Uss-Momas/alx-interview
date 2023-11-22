#!/usr/bin/python3
"""0-making_change module documentation
"""


def makeChange(coins, total):
    """makeChange function
    Args:
        - coins: is a stack/list of the values of the coins in your possession
        - totaL: the target value
    Return:
        - fewest number of coins needed to meet the given amount total.
    """
    if total <= 0:
        return 0
    coins = sorted(coins)
    max_value = max(coins)
    sum_values = 0
    number_ops = 0
    while sum_values < total:
        sum_values += max_value
        size = len(coins)
        if sum_values > total:
            if size - 1 <= 0:
                break
            sum_values -= max_value
            coins.pop()
            max_value = max(coins)
        else:
            number_ops += 1
    if sum_values != total:
        return -1
    return number_ops
