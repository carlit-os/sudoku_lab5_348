from unittest import TestCase

from student_code import is_board_full


class Test(TestCase):
    def test_is_board_full(self):
        self.assertFalse(is_board_full([[1], [0]]))
        self.assertTrue(is_board_full([[1], [9]]))
