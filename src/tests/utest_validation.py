import unittest

from ..array_handler import Validator


class ValidationTestCase(unittest.TestCase):

    def setUp(cls):
        cls.incorrect_dimension_obj = "[[1, 2], [3, 4], [1, 2, [0]]]"
        cls.correct_str_obj = "[[1, 2], [3, 4], [5, 6]]"
        cls.incorrect_type_obj = '[["1", "2"], ["3", "4"]]'
        cls.incorrect_array = '{"1": 2, "3": 4}'
        cls.validator = Validator(2, 'int')

    def test_validate_correct_obj(self):
        self.assertTrue(self.validator.set_array(self.correct_str_obj))
        self.assertEqual(self.correct_str_obj, str(self.validator.array))

    def test_validate_incorrect_dimension_obj(self):
        self.assertFalse(self.validator.set_array(self.incorrect_dimension_obj))
        self.assertIsNone(self.validator.array)

    def test_validate_incorrect_type_obj(self):
        self.assertFalse(self.validator.set_array(self.incorrect_type_obj))
        self.assertIsNone(self.validator.array)

    def test_validate_incorrect_array(self):
        self.assertFalse(self.validator.set_array(self.incorrect_array))
        self.assertIsNone(self.validator.array)
