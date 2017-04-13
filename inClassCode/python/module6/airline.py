#!/usr/bin/env python3


class Flight:
    """
    A flight class
    """
    def __int__(self, number):
        # Check the number has the following format
        # 2 chars + 3 digits
        self._number = number
        if not number[:2].isalpha():
            raise ValueError("No airline code")

        if not number[:2].isupper():
            raise ValueError("No airline code")

        if not number[2:].isdigit() and int(number[2:]) < 1000:
            raise ValueError("Invalid route number")

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


def test_flight():
    """
    Test Flight class
    """
    f = Flight("PP103")
    num = f.number()
    print(num)


def main():
    """
    test function
    """
    test_flight()


if __name__ == "__main__":
    main()

    exit(0)
