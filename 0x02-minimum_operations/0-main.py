#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

print(minOperations(1))

print(minOperations(-12))

print(minOperations(2147483640))

n = 9
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 5
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 6
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 7
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 11
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 13
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


n = 17
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
