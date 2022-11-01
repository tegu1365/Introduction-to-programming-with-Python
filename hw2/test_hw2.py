import unittest

from solution import (nums_to_text, text_to_nums, nums_to_angle,
                      angles_to_nums, is_phone_tastic)


class TestNumsToText(unittest.TestCase):
    """Test the nums_to_text function."""

    def test_simple_conversion(self):
        """Sanity test for a single number."""
        self.assertEqual(nums_to_text([2]).lower(), 'a')

    def test_hello(self):
        self.assertEqual(nums_to_text([4, 4, 3, 3, 5, 5, 5, -1, 5, 5, 5, 6, 6, 6]), 'HELLO')

    def test_python(self):
        self.assertEqual(nums_to_text([7, 9, 9, 9, 8, 4, 4, 6, 6, 6, -1, 6, 6]), 'PYTHON')

    def test_single_letter(self):
        self.assertEqual(nums_to_text([2, 2, 2, 2, 2, 2, 2, 2]), 'B')

    def test_interval(self):
        self.assertEqual(nums_to_text([2, 2, 0, 1, 3, 3]), 'B E')

    def test_pass(self):
        self.assertEqual(nums_to_text([2, 2, 1, 1, 2, 1]), 'BA')

    def test_multi_intervals(self):
        self.assertEqual(nums_to_text([0, 0, 0, 0, 0, 0, 0]), '       ')

    def test_multi_pass(self):
        self.assertEqual(nums_to_text([1, 2, 1, 1, 1, 2]), 'AA')


class TestTextToNums(unittest.TestCase):
    """Test the text_to_nums function."""

    def test_simple_conversion(self):
        """Sanity test for a single letter."""
        self.assertEqual(text_to_nums('a'), [2])

    def test_hello(self):
        self.assertEqual(text_to_nums('hello'), [4, 4, 3, 3, 5, 5, 5, -1, 5, 5, 5, 6, 6, 6])

    def test_python(self):
        self.assertEqual(text_to_nums('PyThon'), [7, 9, 9, 9, 8, 4, 4, 6, 6, 6, -1, 6, 6])

    def test_interval(self):
        self.assertEqual(text_to_nums('asl pls'), [2, 7, 7, 7, 7, 5, 5, 5, 0, 7, 5, 5, 5, 7, 7, 7, 7])

    def test_multi_letter(self):
        self.assertEqual(text_to_nums('aAaA Bbb'), [2, -1, 2, -1, 2, -1, 2, 0, 2, 2, -1, 2, 2, -1, 2, 2])


'''       

class TestNumsToAngles(unittest.TestCase):
    """Test the nums_to_angle function."""

    def test_simple_conversion(self):
        """Sanity test for a single number."""
        self.assertEqual(nums_to_angle([1]), 30)


class TestAnglesToNums(unittest.TestCase):
    """Test the angles_to_nums function."""

    def test_simple_conversion(self):
        """Sanity test for a single angle."""
        self.assertEqual(angles_to_nums([30]), [1])


class TestIsPhonetastic(unittest.TestCase):
    """Test the is_phone_tastic function."""

    def test_simple_word(self):
        """Sanity test for a single letter word."""
        self.assertTrue(is_phone_tastic('a'))

'''
if __name__ == '__main__':
    unittest.main()
