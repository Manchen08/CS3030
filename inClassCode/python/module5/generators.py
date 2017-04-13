#!/usr/bin/env python3
import sys


def test_generator():
    """
    practice Generators
    """
    yield 1
    yield 2
    yield 3

def gen246():
    """
    another generator
    """
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6

#Main function
def main():
    """
    Test Function
    """
    g = test_generator()
    print(g)
    for v in test_generator():
        print(v)

    g = test_generator()
    h = test_generator()
    print(g,h)
    print(g is h)
    print(next(g))
    print(next(g))
    print(next(h))

    for v in gen246():
        print(v)
        print("********")

    h = gen246()
    print(next(h))
    print(next(h))
    print(next(h))
    print(next(h))

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
