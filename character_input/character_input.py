#!/usr/bin/env python3
from datetime import datetime


ITERATION_NUMBER = None
AGE = None


class NotAPositiveIntException(Exception):
    """Raised when an age input is not a positive integer"""
    pass


class LiarException(Exception):
    """Raised when an age input is greater than 122"""
    pass


class NoInputException(Exception):
    """Raised when a name input is empty"""
    pass


def get_name():
    """
    PRE:
    POST: returns the name the user entered if the user entered something
    RAISES: NoInputException if the user entered nothing
    """
    name_input = input("enter your name: ")
    if name_input:
        return name_input
    else:
        raise NoInputException


def get_age():
    """
    PRE:
    POST: returns the age the user entered if it is a number between 0 and 122
    RAISES :    - NotAPositiveIntException if the user didn't enter a positive integer number
                - LiarException if the user entered a number greater than 122
    """
    age_input = input("enter your age: ")
    if age_input.isnumeric():
        age_input = int(age_input)
        if age_input > 122:
            raise LiarException
        return age_input
    else:
        raise NotAPositiveIntException


def number_of_years_to_100(age):
    """
    PRE: age is an integer comprised between 0 and 100 not included
    POST: returns the year in wich the user will turn 100
    """
    years_to_100 = 100 - age
    return datetime.today().year + years_to_100


def get_number_of_iterations():
    """
    PRE:
    POST: returns the number of iterations the user entered if it is a positive integer different from 0
    RAISES : NotAPositiveIntException if the user didn't enter a positive integer number
    """
    number_of_interation = input("enter a number of iterations: ")
    if number_of_interation.isnumeric() and not (int(number_of_interation) == 0):
        return int(number_of_interation)
    else:
        raise NotAPositiveIntException


if __name__ == '__main__':
    try:
        ITERATION_NUMBER = get_number_of_iterations()
        get_name()
        AGE = get_age()
    except NotAPositiveIntException:
        print("error: you were asked for a positive integer number")
    except LiarException:
        print("error: the user is a liar")
    except NoInputException:
        print("error: keep your secrets then")
    else:
        if AGE >= 100:
            print("ok boomer")
        else:
            for i in range(ITERATION_NUMBER):
                print(f"you'll be a 100 years old in {number_of_years_to_100(AGE)}")
