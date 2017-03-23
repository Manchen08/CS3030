#!/usr/bin/env python3
import sys

def test_shallow_copy():
    """
    Test shallow copy
    """
    a = [[1,2],[3,4]]
    # make a copy of it
    # shallow copy, the object itself is unique, but the values that they point to are still
    # the same. When it is changed, then it will make it's own. They keep sharing the same memory.
    b = a[:]
    print("Same object", a is b)
    print("Same values", a == b)
    print("a[0]=>", a[0])
    print("b[0]=>", b[0])
    print("Same object", a[0] is b[0])
    print("Same object 1", a[1] is b[1])

    # Update a[0]
    a[0] = [8,9]

    print("After update a[0]")
    print("a[0]=>", a[0])
    print("b[0]=>", b[0])
    print("Same object", a[0] is b[0])
    print("Same object 1", a[1] is b[1])

    # Append info to one member
    # The address is still looking at the same object when append is used.
    # Shallow copy is a copy by reference
    # Deep copy is coping by value, new references for each value.
    a[1].append(5);
    print("After append a[1]")
    print("a[1]=>", a[1])
    print("b[1]=>", b[1])
    print("Same object 1", a[1] is b[1])


def rep_list():
    """
    Repeat List properties
    """
    c = [21, 47, 78]
    # Repetition, repeats the reference without a copy of the value
    d = c * 4
    print(c)
    print(d)
    print(c is d)
    s = [0] * 9
    print(s)
    s = [[-1,1]] * 5
    print(s)
    s[3].append(7)
    print(s)
    
    # Test for membership
    print(47 in c)
    print(99 not in c)

def test_list():
    """
    Test List properties
    """
    u = "This is Weber State Home of Waldo".split()
    print(u)
    u.sort(key=len)
    print(u)
    u.sort(reverse=True)
    v = ' '.join(u)
    print(v)
    v = ':'.join(u)
    print(v)
    
    # Built-in sorted, reveresed for All collections
    k = [3,4,2,4,5]
    y = sorted(k)
    print(k)
    print(y)
    
    # Reversed
    y = reversed(k)
    print(y)
    print(list(y))



#Mai function
def main():
    """
    Test Function
    """
    # test_shallow_copy() 
    # rep_list()
    test_list()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
