import unittest
import os

from ..array_handler import Saver


class SaveTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.correct_obj = [[1, 2], [3, 4], [5, 6]]
        cls.csv_path = 'test_file.csv'
        cls.json_path = 'test_file.json'
        cls.txt_path = 'test_file.txt'
        cls.saver = Saver()

    def tearDown(self) -> None:
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)

        if os.path.exists(self.json_path):
            os.remove(self.json_path)

    def test_save_to_json(self):
        save_result = self.saver.array_save(self.json_path, self.correct_obj)
        self.assertTrue(save_result)
        self.assertTrue(os.path.exists(self.json_path))

    def test_save_to_csv(self):
        save_result = self.saver.array_save(self.csv_path, self.correct_obj)
        self.assertTrue(save_result)
        self.assertTrue(os.path.exists(self.csv_path))

    def test_save_to_json_already_exists(self):
        save_result = self.saver.array_save(self.json_path, self.correct_obj)
        self.assertTrue(save_result)

        save_result = self.saver.array_save(self.json_path, self.correct_obj)
        self.assertFalse(save_result)

    def test_save_to_csv_already_exists(self):
        save_result = self.saver.array_save(self.csv_path, self.correct_obj)
        self.assertTrue(save_result)

        save_result = self.saver.array_save(self.csv_path, self.correct_obj)
        self.assertFalse(save_result)

    def test_save_to_unexpexted_extension(self):
        save_result = self.saver.array_save(self.txt_path, self.correct_obj)
        self.assertFalse(save_result)
        self.assertFalse(os.path.exists(self.txt_path))
