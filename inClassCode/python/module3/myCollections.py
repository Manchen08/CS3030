#!/usr/bin/env python3
import sys


def play_tuples():
    """
    Practice Tuples
    """
    # Use () to define tuples
    t = ("Ogden", 1.99, 2)  
    print("First member:", t[0])
    print("Last member:", t[-1]) # negative index
    print("Length of tuple:", len(t))
    # Iterate 
    for item in t:
        print(item)
    # Concatenation
    t = t + ("Hello", 256e10)
    print(t)
    # Repetition
    print(t*3)
    # Nested tuples
    a = ((220,284),(1184,1125), (5020, 1024), (6332, 1))
    print(a)
    # Access one value in nested
    print(a[1])
    print(a[1][1])
    # single element tuples
    h = (391,)  # add comma to make it a tuple
    # parenthesis are optional
    t = 1, 2, 3, 4
    print(t)
    print(min_max([32,56,89,12,50,99]))
    tp = min_max([32,56,89,12,50,99])
    print(tp, tp[0], tp[1])
    print(type(tp))
    # Tuple unpacking
    lower, upper = min_max([32,56,89,12,50,99])
    print(type(lower),lower)
    print(type(upper),upper)
    # swapping
    a = "jelly"
    b = "bean"
    print(a, b)
    a, b = b, a
    print(a, b)

    # Tuple constructor
    l = [2,6,8,2,9]
    tl = tuple(l)
    print(l)
    print(tl)
    print(tuple("Weber State"))
    # Test membership
    print( 8 in tl)
    print( 88 in tl)
    print( 88 not in tl)
    


def min_max(items):
    """
    return the min and max of a collection
    """
    return min(items), max(items)


def play_strings():
    """
    Play with strings
    """
    # Test for length
    print(len("This is super mega cool"))
    # Concatenation
    s = "New" + "found" + "land"
    print(s)
    s = "New"
    s += "found"
    s += "land"
    print(s)
    # join strings
    # Separator.join()
    teams = ";".join(["Real Madrid", "Barcelona", "Bayern", "Juventus"])
    print(teams)
    # Split records split()
    steams = teams.split(";")
    print(steams)
    # String formatting format()
    print("The age of {0} is {1}".format("Jim",32))
    print("The age of {0} is {1}.{0}'s birthday is on {2}".format("Jim",32, "October 31"))
    
    print("The score was {} vs {}".format(6,1))
    # using a name, position is not required
    print("Current position {latitude} {longitude}".format(latitude="60N", longitude="5E"))
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(65.2, 23.1, 82.1)))


def play_range():
    """
    Practice range features
    """
    for i in range(5):
        print(i)
    # Create list of ranges
    print(list(range(5)))
    print(list(range(5, 10)))
    print(list(range(1,5)) + list(range(6,11)))
    # Range by steps
    print(list(range(1, 30, 2)))
    # In reverse order
    print(list(range(30, 1, -2)))

    # Enumerate
    s = [0, 2, 4, 6, 8, 10]
    for i in range(len(s)):
        print(i)

    for p in enumerate(s):
        print(p)

    # Unpack
    for i,v in enumerate(s):
        print("i={} , v={}".format(i,v))


def play_list():
    """
    Practice list
    """
    r = [1, -4, 89, -16, 2]
    print(r)
    # Print last value
    print(r[-1])
    print(r[len(r) -1])
    # Slicing
    print(r[1:3])
    print(r[:3])
    # Full slice
    print(r[:])
    # Copy the list
    full = r
    print(full is r)
    print(full == r)
    # Create a new list with same values
    full = r[:]
    print(full is r)
    print(full == r)
    

# Main function
def main(): 
    """
    Test Function	
    """
    #play_tuples()
    #play_strings()
    #play_range()
    play_list()
    

	


if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
