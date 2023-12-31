#!/usr/bin/python3
"""
0-nqueens module
implement a solution for the n-queens puzzle problem
"""
import sys


def solveNQueens(n):
    """
    solveNQueens function implementation
    """
    col = set()
    posDiag = set()  # row + column
    negativeDiag = set()  # r - c
    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(row):
        """backtrack function"""
        if row == n:
            copy = ["".join(r) for r in board]
            result.append(copy)
            return

        for c in range(n):
            if c in col or (row + c) in posDiag or (row - c) in negativeDiag:
                continue
            col.add(c)
            posDiag.add(row + c)
            negativeDiag.add(row - c)
            board[row][c] = "Q"

            backtrack(row + 1)

            col.remove(c)
            posDiag.remove(row + c)
            negativeDiag.remove(row - c)
            board[row][c] = "."
    backtrack(0)
    return result


def printSolution(results):
    """printSolution - function to print the solution for the NQueens problem
    it should print a array of positions for every queen in the puzzle
    Args:
        - results: a list os lists containing the results in a string format
    Return:
        - None
    """
    for result in results:
        index_result = list(zip(range(len(result)), result))
        queen_positions = [
            [(i, j) for j, letter in list(zip(range(len(element)), element))
             if letter == "Q"] for i, element in index_result]
        positions = [list(element[0]) for element in queen_positions]
        print(positions)


args = sys.argv
if len(args) != 2:
    print("Usage: nqueens N")
    exit(1)

if not args[1].isdigit():
    print("N must be a number")
    exit(1)

if int(args[1]) < 4:
    print("N must be at least 4")
    exit(1)


n = int(args[1])
printSolution(solveNQueens(n))
