#!/usr/bin/env python3
import unittest
from unittest.mock import patch

from odd_or_even.odd_or_even import get_number, NotAnIntException, NumberIsMultipleOf4Flag, number_type, \
    NumberIsEvenFlag, NumberIsOddFlag, NumberIsZeroException, division_check


class TestGetNumber(unittest.TestCase):
    test_number_is_int_side_effect = ["-100", "-75", "-50", "-25", "-1", "1", "25", "50", "75", "100"]
    test_number_is_not_int_side_effect = ["", "characters", "mixed_characters_with_16513518"]
    test_number_is_zero_side_effect = ["0"]

    @patch('builtins.input', side_effect=test_number_is_int_side_effect)
    def test_number_is_int(self, side_effect):
        mocked_inputs = self.test_number_is_int_side_effect
        for mocked_input in mocked_inputs:
            self.assertEqual(int(mocked_input), get_number(""))

    @patch('builtins.input', side_effect=test_number_is_not_int_side_effect)
    def test_number_is_not_int(self, side_effect):
        mocked_inputs = self.test_number_is_not_int_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NotAnIntException, get_number, "")

    @patch('builtins.input', side_effect=test_number_is_zero_side_effect)
    def test_number_is_zero(self, side_effect):
        mocked_inputs = self.test_number_is_zero_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NumberIsZeroException, get_number, "")


class TestNumberType(unittest.TestCase):
    test_number_is_multiple_of_4_side_effect = ["8", "16", "32", "40", "80", "-8", "-16", "-32", "-40", "-80"]
    test_number_is_even_side_effect = ["-246", "-4852694", "8415122", "2654", "-10", "-6", "-2", "2", "6", "10"]
    test_number_is_odd_side_effect = ["-147", "-48651523", "-11", "-5", "-1", "1", "5", "11", "15465289", "1563"]

    def test_number_is_multiple_of_4(self):
        mocked_inputs = self.test_number_is_multiple_of_4_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NumberIsMultipleOf4Flag, number_type, int(mocked_input))

    def test_number_is_even(self):
        mocked_inputs = self.test_number_is_even_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NumberIsEvenFlag, number_type, int(mocked_input))

    def test_number_is_odd(self):
        mocked_inputs = self.test_number_is_odd_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NumberIsOddFlag, number_type, int(mocked_input))


class TestDivisionCheck(unittest.TestCase):
    mocked_initial_side_effect = ["16", "15", "56", "32", "192", "-25"]
    test_number_is_multiple_of_check_side_effect = ["4", "3", "14", "16", "48", "-5"]
    test_number_is_not_multiple_of_check_side_effect = ["45", "17", "46", "33", "269", "-54"]

    @patch('builtins.input', side_effect=test_number_is_multiple_of_check_side_effect)
    def test_number_is_multiple_of_check(self, side_effect):
        initial_mocked_inputs = self.mocked_initial_side_effect
        for initial_mocked_input in initial_mocked_inputs:
            self.assertEqual(True, division_check(int(initial_mocked_input)))

    @patch('builtins.input', side_effect=test_number_is_not_multiple_of_check_side_effect)
    def test_number_is_not_multiple_of_check(self, side_effect):
        initial_mocked_inputs = self.mocked_initial_side_effect
        for initial_mocked_input in initial_mocked_inputs:
            self.assertEqual(False, division_check(int(initial_mocked_input)))
