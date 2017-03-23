#!/usr/bin/env python3
"""
This program implements an algorithm that swaps the first and second halves of a list
"""
import sys

def swap (a, i, j):
    """
    Swaps the elemetns of a list at
    a given position
    :param a: the list 
    :param i: the first position
    :param j: the second position
    :returns: nothing
    """

def slice(a):
    l = len(a)
    l2 = len(a)//2

    if l % 2 == 0:
        l = len(a)//2 + 1
        print(l)
        b = a[l:] + a[len(a)//2] + a[:l]
        return b
    else:
        l = len(a)//2
        b = a[l:] + a[:l]
        return b

#Main function
def main():
    """
    Test Function
    """
    val = [9,13,21,4,11,7,1,3]
    print("Orig ", val)
    nval = slice(val)
    print("Modified ", nval)

    
    val = [9,13,21,4,11,7,1,3,99]
    print("Orig ", val)
    nval = slice(val)
    print("Modified ", nval)

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
