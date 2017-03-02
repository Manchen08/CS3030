#!/usr/bin/env python3
import sys

def modify(k):
    """
    Modify the content of a list of items
    Args:
        k -> a list of items
    Returns:
        Nothing
    """

    # Everything is a reference, m will reflect the same change
    k.append(29)
    print("k=", k)

def replace(g):
    """
    Replace the content of the list
    Args:
        g -> a list of items
    Returns:
        Nothing
    """
    g = [17, 23, 45, 90]
    print("g=",g)

def replace_content(g):
    """
    Replace the content of the list
    Args:
        g -> a list of items
    Returns:
        Nothing
    """
    g[0] = 99
    g[1] = 88
    g[2] = 77
    print("g=",g)


#Main function
def main():
    """
    Test Function
    """

    m = [9, 13, 15]
    print(m)
    print("Original", m)
    modify(m)
    print(m)
    print("After modify", m)
    replace(m)
    print("After replace ",m)
    replace_content(m)
    print("After replace content ", m)



if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
