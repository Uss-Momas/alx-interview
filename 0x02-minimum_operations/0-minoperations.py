#!/usr/bin/python3
"""minnimum operations
"""
copied_message = ''


def isprime(num: int) -> bool:
    """fun to verify if number is prime or not"""
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True


def minOperations(n: int) -> int:
    """method that calculates the fewest number of operations needed
    to result in exactly n 'H' chars in a file
    Can only execute 2 operations at each time:
        - Copy All
        - Paste
    Example:
        if n is 9, how many operations is necessary to have exaclty 9 H's?

        Answer:
        H => Copy All => Paste => HH => Paste =>HHH => Copy All
        => Paste => HHHHHH => Paste => HHHHHHHHH

        We need of exactly 6 operations
    """
    n_operations = 0
    message = 'H'

    if n < 5:
        return n

    if isprime(n):
        return n

    while len(message) < n:
        if len(message) == 1:
            copyAll(message)
            message += paste()
            n_operations += 2
        else:
            if n % len(message) == 0:
                copyAll(message)
                message += paste()
                n_operations += 2
            else:
                message += paste()
                n_operations += 1
    return n_operations


def copyAll(message: str) -> None:
    """Copy alls"""
    global copied_message
    copied_message = message


def paste() -> str:
    """paste the copied message"""
    return copied_message
