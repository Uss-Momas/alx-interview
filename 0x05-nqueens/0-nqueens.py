#!/usr/bin/python3
"""0-nqueens module
implementation of solution for n-queens problem
"""
import sys

args = sys.argv

if len(args) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
