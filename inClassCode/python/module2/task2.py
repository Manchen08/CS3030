#!/usr/bin/env python3
import sys

def GetInput():
    x = int(input('Please enter the first integer'))
    y = int(input('Please enter the second integer'))
    #use formated output 'C Style'
    print("%-12s%6d" % ("Sum: ", x + y))
    print("%-12s%6d" % ("Difference: ", x - y))
    print("%-12s%6d" % ("Product: ", x * y))
    print("%-12s%6d" % ("Average: ", (x + y)/2))
    print("%-12s%6d" % ("Distance: ", abs(x-y)))
    print("%-12s%6d" % ("Min: ", min(x,y)))
    print("%-12s%6d" % ("Max: ", max(x,y)))
    
#Main function
def main():
    """
    Test Function
    """
    GetInput()
    pass

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
