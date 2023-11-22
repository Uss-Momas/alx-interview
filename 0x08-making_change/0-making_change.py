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
    total_cp = total
    sorted_coins = sorted(coins)
    num_ops = []
    while len(sorted_coins) > 0:
        max_coin = sorted_coins[-1]
        result = total_cp // max_coin
        total_cp = total_cp % max_coin
        num_ops.append(result)
        if total_cp == 0:
            break
        sorted_coins.pop()
    if total_cp != 0:
        return -1
    return sum(num_ops)
