#!/usr/bin/env python3
import sys

#Main function
def GetInput():
    """
    Ask for pin, if it is correct, print out money. If it is wrong, let them try 3 times, if they guess wrong
    3 time, print account locked. Check for pin of length 4
    Input:
        Received view input()
    Output:
        Password match or fail
    """
    realpass = '1234'
    passwd = ""
    for x in range(0,3):
        while len(passwd) != 4:
            passwd = input('Enter your pin: ')
            if len(passwd) != 4:
                print('Invalid PIN length. Correct format is: <XXXX>')

        if passwd == realpass:
            print('Your PIN is correct')
            print('You have $10,000,000 in your account')
            break
        print('Your Pin is incorrect')
        
        if x == 2:
            print('Your credit card has been blocked')
            exit(1)
        passwd = ""

if __name__ == "__main__":
    # Call Main
    GetInput()

    exit(0)
