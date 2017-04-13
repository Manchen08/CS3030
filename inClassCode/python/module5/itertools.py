#!/usr/bin/env python3
import sys
from itertools import islice, count
from luc import is_prime

def test_itertools():
    thousand_primes = islice((x for x in count() if is_prime(x)),10000)
    print(thousand_primes)
    print(list(thousand_primes))

#Main function
def main():
    """
    Test Function
    """
    #test_itertools()
    # Built-in any: test ANY member to be true in the collection
    print(any([False,False,True]))
    # Built-in all: test ALL member to be true in the collection
    print(all([False,False,True]))
    #Check with primes
    print(any(is_prime(x) for x in range (1328, 1361)))
    print(all(name == name.title() for name in ['London', 'New York', 'Sydney']))
    # Built-in zip: synchronize iterations over iterables series
    sunday = [12,14,15,17,21,22,22,23,25,20]
    monday = [13,14,14,13,12,15,16,16,17,16]
    tuesday = [10,11,11,12,12,14,14,13,12,10]

    for items in zip(sunday,monday):
        print(items)

    for sun,mon in zip(sunday,monday):
        print("avg= ", (sun+mon/2)

    for temp in zip(sunday,monday,tuesday):
        print("min = [:4.1f], max={:4.1f}, avg={:4.1f}".format(min(temp), max(temp), sum(temp)/len(temp)))

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
