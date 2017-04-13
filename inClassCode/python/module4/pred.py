#!/usr/bin/env python3
import sys
from math import sqrt

def is_prime(x):
    """
    Test if number is prime
    Arg: 
        value to be tested
    Returns:
        True if value is prime
        False if value is not prime
    """
    if x < 2:
        return False

    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def test_pred():
    """
    Test Predicates
    """
    l = [x for x in range(101) if is_prime(x)]
    print(l)

#Main function
def main():
    """
    Test Function
    """
    test_pred()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
