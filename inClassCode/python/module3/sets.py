#!/usr/bin/env python3
import sys

def test_sets():
    """
    Test set properties
    """
    p = {6, 28, 12, 34, 45, 56}
    print(p)
    print(type(p))
    # Constructor set()
    l = [2, 3, 4, 5, 6, 7, 5]
    print("List", l)
    s = set(l)
    print("Sets can not have duplicates.\nSet: ", s)

    # iterate
    for x in s:
        print(x)

    #Test Membership
    print(9 in s)

    # Add element
    s.add(99)
    print("Set", s)

    # Add multiple elemetns
    s.update([99, 99, 99, 100])
    print("Set", s)

    # Eliminate element
    # remove will throw an exception if it cannot find the target s.remove(99)
    s.discard(99)
    s.discard(99)
    print(s)

    # Copy Sets
    j = s.copy()
    print("Set j", j)

    m = s.copy()
    print("Set m", m)
    print(m is s)



def test_algebra():
    """
    Test set functions with algebra
    """
    blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
    blonde_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
    smell_hcn = {'Harry', 'Amelia'}
    taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
    o_blood = {'Mia', 'Joshua', 'Lily'}
    a_blood = {'Harry', 'Jack'}
    ab_blood = {'Olivia'}

    # Unions
    print(blue_eyes.union(blonde_hair))

    # Intersections
    print(blue_eyes.intersection(blonde_hair))

    #Difference
    print(blonde_hair.difference(blue_eyes))

    # Symmetric difference
    print(smell_hcn.symmetric_difference(a_blood))

    # Subsets
    print(ab_blood.issubset(blue_eyes))
    print(o_blood.issubset(blue_eyes))

#Main function
def main():
    """
    Test Function
    """
    #test_sets()
    test_algebra()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
