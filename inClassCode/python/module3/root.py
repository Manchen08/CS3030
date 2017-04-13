#!/usr/bin/env python3
import sys

def sqrt(x):
    """
    Computes square roots using the 
    method of Heron of Alexandria
    Args:
        x => The number for which square root
        is to be computed
    """
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess)/2.0
    return guess

    
#Main function
def main():
    """
    Test Function
    """
    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
        print("This is never printed")
    except ZeroDivisionError as e:
        print("cannot compute square root of neg number")


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
