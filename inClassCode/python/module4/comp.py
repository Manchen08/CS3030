#!/usr/bin/env python3
import sys
from math import factorial as fact
from pprint import pprint as pp

def test_dict_comp():
    """
    Dictionary comprehensions
    """
    nba_teams = {'Jazz':'SLC',
                'Warriors':'Okland',
                'Lakers':'LA',
                'Spurs':'San Antonio',
                'Heat':'Miama'}

    pp(nba_teams)
    # Dict Comprehension
    teams_nba = {city:mascot for mascot,city in nba_teams.items()}
    pp(teams_nba)
    # Task a list of strings, you want to use the 
    # first character of the member as the key
    words = "Today I am very happy to learn comprehension at last".split()
    dict_words = {x[0]:x for x in words}
    pp(dict_words)

def test_list_comp():
    """
    Play iwth list comprehensions
    """
    words = "Today I am very happy to learn comprehensions.".split()
    print(words)
    # iterate over collection
    # Create a list with the words' memers char count
    lwords = []
    for word in words:
        lwords.append(len(word))

    print(lwords)

    # now use a comprehension
    lc = [ len(word) for word in words]
    print(lc)

    # Write a comprehension to find the number of digits
    # for the first 20 factorial number
    # Hint: use range
    for x in range(20):
        print(x, fact(x))

    f = [len(str(fact(x))) for x in range(20)]
    print(f)

#Main function
def main():
    """
    Test Function
    """
    #test_list_comp()
    test_dict_comp()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
