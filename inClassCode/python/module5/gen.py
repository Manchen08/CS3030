#!/usr/bin/env python3
import sys

"""
Module for demostrating generator
execution
"""

def take(count, iterable):
    """
    Take items from the front of the iterablle
    Args:
        count: The maximim number of items to retrieve
        iterable: the source series
    Yields:
        At most 'count'itmes for 'iterable'
    """ 

    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        print("Now ", item)
        yield item

def test_take():
    """
    test take defenition
    """
    items = [2,4,6,8,10,20,30]
    for item in take(2, items):
        print(item)

def distinct(iterable):
    """
    Returns inuqe items by eliminating duplicates
    Args: 
        iterable: the source series
    Yields: 
        Unique elements in order from iterable
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

def test_distinct():
    items = [5,7,7,6,5,5]
    for item in distinct(items):
        print(item)


def run_pipeline():
    """
    Test combination of both: distinct and take
    """
    items = [3,6,6,2,1,2,1,9]
    for item in take(c, distinct(items)):
        print(item)

#Main function
def main():
    """
    Test Function
    """
    #test_take()
    test_distinct()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
