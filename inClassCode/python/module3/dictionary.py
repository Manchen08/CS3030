#!/usr/bin/env python3
import sys

def test_dict():
    """
    Play with dictionaries
    """
    # A list of tuples
    names_and_ages = [('Alice',32), ('Bob', 48), ('Mary', 26)]
    print(names_and_ages)
    # dict() constructor
    d = dict(names_and_ages)
    print(d)
    # Using List
    print(names_and_ages[0][1])
    # Using Dictionary
    print(d['Alice'])

    # Build them directly
    phonetic = dict(a='alpha', b='beta', c='charlie')
    print(phonetic['a'])
    # Copy 
    #e = d shallow copy
    # e = d.copy() deep copy
    # e = dict(d) # const copy

    # Updating
    stocks = {'GOOG':891, 'AAPL':416, 'IBM':194}
    print(stocks)
    # Update one value
    stocks['IBM'] = 220
    print(stocks)
    stocks['YHOO'] = 20 # updates or creates the entry
    print(stocks)
    # update multiple
    stocks.update({'GOOG':894, 'WEBER':350})
    print(stocks)

    # Iterate over
    for k in stocks:
        print('{key} => {value}'.format(key = k, value = stocks[k]))
    for v in stocks.values():
        print('{value}'.format(value = v))
    for k,v in stocks.items():
        print('{key} => {value}'.format(key = k, value = v))
    for k in stocks.items():
        print('{key} => {value}'.format(key = k[0], value = k[1]))
        
    # Test for Membership
    print("Google?", 'GOOG' in stocks)
    print("Gmail?", 'GMAIL' in stocks)

    # Removing Items
    del stocks['YHOO']
    print(stocks)

    # Mutability
    iso = {'H':[1,2,3],
            'HE':[3,4],
            'Li':[6,7],
            'Be':[10,11],
            'C':[11,12,14,14]}

    print("Before", iso)
    iso['H'] += [4,5,6]
    print("After", iso)


#Main function
def main():
    """
    Test Function
    """
    test_dict()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
