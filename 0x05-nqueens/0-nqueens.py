#!/usr/bin/python3
"""
0-nqueens module
implement a solution for the n-queens puzzle problem
"""
import sys

args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
