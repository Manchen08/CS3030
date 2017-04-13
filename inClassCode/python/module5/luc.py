#!/usr/bin/env python3
import sys
import time
from math import sqrt

def lucas():
    """
    The series starts with 2 and 1, and each 
    value after that is the sum of the two 
    precedig values. Ex: 2,1,3,4,7 etc
    Yields:
        next value on lucas series
    """

    #First member
    yield 2
    # set your members
    a = 2
    b = 1
    i = 1
    while True:
        yield b
        a, b = b, a + b

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


def test_lucas():
    """
    Test lucas series
    """
    i = 1
    for x in (p for p in lucas() if is_prime(p)):
        print(x, len(str(x)))
        #time.sleep(1)
        i += 1
        if(i == 15):
            break
    print("Done")

#Main function
def main():
    """
    Test Function
    """
    test_lucas()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
