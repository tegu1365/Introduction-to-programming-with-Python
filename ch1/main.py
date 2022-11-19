import unittest

from solution import suffix_ordinals


class TestCalculateFinalVector(unittest.TestCase):
    '''Test the calculate_final_vector function.'''

    def test_simple_move(self):
        '''Sanity test for a simple 2-step move.'''
        self.assertEqual(suffix_ordinals("2.2.2.2"),
                         "2nd of the 2nd of the 2nd of the 2nd")

if __name__ == '__main__':
    unittest.main()