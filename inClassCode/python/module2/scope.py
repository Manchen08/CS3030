#!/usr/bin/env python3
import sys

count = 0

def show_count():
    """
    prints currnet count
    """
    print(count)

def set_count(c):
    """
    sets counter
    Args:
        c-> value to set the counter
    """
    count = c


#Main function
def main():
    """
    Test Function
    """
    show_count()
    set_count(7)
    show_count()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
