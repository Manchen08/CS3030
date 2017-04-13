"""
a module to demonstrate exceptions
"""
#!/usr/bin/env python3
import sys

def convert(s):
    """
    Convert to an int
    """
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("\tConversion error:{}"\
                .format(str(e)), file=sys.stderr)
        return -1

#Main function
def main():
    """
    Test Function
    """
    i = convert(55)
    print(i)
    i = convert(55.5)
    print("As float ", i, type(i))
    i = convert("55")
    print("As string ", i, type(i))
    i = convert("Hello")
    print("As hello ", i, type(i))
    i = convert([2,5,6])
    print("As list ", i, type(i))

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
