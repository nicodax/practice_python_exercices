#!/usr/bin/env python3

NUMBER = None
CHECK = None


class NotAnIntException(Exception):
    """Raised when a number input is not an integer"""
    pass


class NumberIsMultipleOf4Flag(Exception):
    """Raised when the number is a multiple of 4"""
    pass


class NumberIsEvenFlag(Exception):
    """Raised if the number is even"""
    pass


class NumberIsOddFlag(Exception):
    """Raised if the number is odd"""
    pass


class NumberIsZeroException(Exception):
    """Raised if the number or the check number is zero"""
    pass


def get_number(string):
    """
    PRE: string is an instruction string for the console prompt
    POST: returns the number entered by the user if it is an integer
    RAISES: - NotAnIntException if the user didn't enter an integer
            - NumberIsZeroException if the number is zero
    """
    number = input(string)
    if number.isnumeric() or (number[1:].isnumeric() and number[0] == "-"):
        if int(number) == 0:
            raise NumberIsZeroException
        return int(number)
    else:
        raise NotAnIntException


def number_type(x):
    """
    PRE: x is an integer and different from 0
    POST: raises a flag depending if x is odd, even or a multiple of 4
    RAISES: - NumberIsMultipleOf4Flag if x is a multiple of 4
            - NumberIsEvenFlag if x is even
            - NumberIsOddFlag if x is odd
    """
    if (x % 4) == 0:
        raise NumberIsMultipleOf4Flag
    elif (x % 2) == 0:
        raise NumberIsEvenFlag
    else:
        raise NumberIsOddFlag


def division_check(num):
    """
    PRE: NUMBER is an integer and different from zero
    POST: raises a flag if num is divisible by the number entered by the user and none of them are equal to 0
                Otherwise, does nothing
    RAISES: NumberIsMultipleOfCheckFlag if num is a multiple of 4
    """
    global CHECK
    CHECK = get_number("enter a check number (different from zero): ")
    return (num % CHECK) == 0


if __name__ == '__main__':
    try:
        NUMBER = get_number("enter a number: ")
        number_is_multiple_of_check = division_check(NUMBER)
        if number_is_multiple_of_check:
            print(f'{NUMBER} is a multiple of {CHECK}')
        else:
            print(f'{NUMBER} is not a multiple of {CHECK}')
        number_type(NUMBER)
    except NotAnIntException:
        print("error: you were asked for an integer number")
    except NumberIsMultipleOf4Flag:
        print(f"{NUMBER} is a multiple of 4")
    except NumberIsEvenFlag:
        print(f"{NUMBER} is even")
    except NumberIsOddFlag:
        print(f"{NUMBER} is odd")
    except NumberIsZeroException:
        print("error: 0 is not an acceptable value")
