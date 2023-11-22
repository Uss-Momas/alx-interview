#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

total, coins = 11, [1, 2, 5]
print(makeChange(coins, total))
total, coins = 3, [2]
print(makeChange(coins, total))
total, coins = 0, [1]
print(makeChange(coins, total))

total, coins = 6249, [186, 419, 83, 408]
print(makeChange(coins, total))
