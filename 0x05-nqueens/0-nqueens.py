#!/usr/bin/python3
"""0-nqueens module
implementation of solution for n-queens problem
"""
import sys

args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = args[1]
if not n.isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(n)
if n < 4:
    print("N must be at least 4")
