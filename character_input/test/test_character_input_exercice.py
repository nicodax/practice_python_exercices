#!/usr/bin/env python3
import unittest
from datetime import datetime, date
from unittest.mock import patch

from character_input.character_input import get_age, NoInputException, get_name, LiarException, \
    NotAPositiveIntException, number_of_years_to_100, get_number_of_iterations


class TestGetName(unittest.TestCase):
    test_no_name_side_effect = [""]
    test_name_side_effect = ["Nicolas Daxhelet", "Mr. Test", "user_name", "dylandu8012"]

    @patch('builtins.input', side_effect=test_no_name_side_effect)
    def test_no_name(self, side_effect):
        self.assertRaises(NoInputException, get_name)

    @patch('builtins.input', side_effect=test_name_side_effect)
    def test_name(self, side_effect):
        mocked_inputs = self.test_name_side_effect
        for mocked_input in mocked_inputs:
            self.assertEqual(mocked_input, get_name())


class TestGetAge(unittest.TestCase):
    test_age_greater_than_122_side_effect = ["123", "548", "15699852"]
    test_input_not_positive_int_side_effect = ["-1", "-10", "-1584526", "", "characters",
                                               "characters_mixed_with_1562285",
                                               "spaced out characters"]
    test_input_comprised_between_0_and_122_side_effect = ["0", "1", "10", "25", "50", "75", "100", "111", "121", "122"]

    @patch('builtins.input', side_effect=test_age_greater_than_122_side_effect)
    def test_age_greater_than_122(self, side_effect):
        mocked_inputs = self.test_age_greater_than_122_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(LiarException, get_age)

    @patch('builtins.input', side_effect=test_input_not_positive_int_side_effect)
    def test_input_not_positive_int(self, side_effect):
        mocked_inputs = self.test_input_not_positive_int_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NotAPositiveIntException, get_age)

    @patch('builtins.input', side_effect=test_input_comprised_between_0_and_122_side_effect)
    def test_input_comprised_between_0_and_122(self, side_effect):
        mocked_inputs = self.test_input_comprised_between_0_and_122_side_effect
        for mocked_input in mocked_inputs:
            self.assertEqual(int(mocked_input), get_age())


class TestNumberOfYearsTo100(unittest.TestCase):
    test_inputs_values = [0, 1, 5, 10, 25, 50, 75, 99]
    test_inputs_values_complemented_to_100 = [100, 99, 95, 90, 75, 50, 25, 1]

    def test_return_value_with_argument_age_respecting_pre_condition(self):
        for idx in range(len(self.test_inputs_values)):
            current_date = datetime.today()
            date_to_100 = date(current_date.year + self.test_inputs_values_complemented_to_100[idx], current_date.month,
                               current_date.day)
            self.assertEqual(date_to_100.year, number_of_years_to_100(self.test_inputs_values[idx]))


class TestGetNumberOfIterations(unittest.TestCase):
    test_number_is_positive_integer_side_effect = ["1", "5", "10", "25", "50", "75", "100", "156842"]
    test_number_is_not_positive_integer_side_effect = ["-1", "-5", "-10", "-25", "characters", "",
                                                       "characters_mixed_with_1566845"]
    test_number_is_positive_zero_side_effect = ["0"]

    @patch('builtins.input', side_effect=test_number_is_positive_integer_side_effect)
    def test_number_is_positive_integer(self, side_effect):
        mocked_inputs = self.test_number_is_positive_integer_side_effect
        for mocked_input in mocked_inputs:
            self.assertEqual(int(mocked_input), get_number_of_iterations())

    @patch('builtins.input', side_effect=test_number_is_not_positive_integer_side_effect)
    def test_number_is_not_positive_integer(self, side_effect):
        mocked_inputs = self.test_number_is_not_positive_integer_side_effect
        for mocked_input in mocked_inputs:
            self.assertRaises(NotAPositiveIntException, get_number_of_iterations)

    @patch('builtins.input', side_effect=test_number_is_positive_zero_side_effect)
    def test_number_is_zero_integer(self, side_effect):
        self.assertRaises(NotAPositiveIntException, get_number_of_iterations)
