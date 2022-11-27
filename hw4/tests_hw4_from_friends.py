# import unittest
#
# from solution import *
#
#
# class TestChessException(unittest.TestCase):
#     """Test the ChessException class."""
#
#     def test_existence(self):
#         """Sanity test for the ChessException class."""
#         exception = ChessException('Paul Morphy')
#
#
# class TestChessScore(unittest.TestCase):
#     """Test the ChessScore class."""
#     score1 = ChessScore(['p', 'p', 'p'])
#     score2 = ChessScore(['p', 'p', 'p', 'p', 'p', 'p'])
#
#     def test_simple_init(self):
#         """Sanity test for the ChessScore class."""
#         score = ChessScore(['p'])
#
#     def test_add(self):
#         score1 = ChessScore(['p', 'p', 'p'])
#         score2 = ChessScore(['p', 'p', 'p', 'p', 'p', 'p'])
#         self.assertEqual(score1 + score2, 9)
#
#     def test_sub(self):
#         score1 = ChessScore(['p', 'p', 'p'])
#         score2 = ChessScore(['p', 'p', 'p', 'p', 'p', 'p'])
#         self.assertEqual(score2 - score1, 3)
#
#     def test_int(self):
#         score1 = ChessScore(['p', 'p', 'p'])
#         self.assertEqual(int(score1), 3)
#
#     def test_bool_oprs(self):
#         score1 = ChessScore(['p', 'p', 'p'])
#         score2 = ChessScore(['p', 'p', 'p', 'p', 'p', 'p'])
#
#         self.assertTrue(score2 > score1)
#         self.assertFalse(score1 > score2)
#
#         self.assertTrue(score1 < score2)
#         self.assertFalse(score2 < score1)
#
#         self.assertTrue(score1 <= score2)
#         self.assertFalse(score2 <= score1)
#
#         self.assertTrue(score1 != score2)
#
#         score1 = ChessScore(['p', 'p', 'p'])
#         score2 = ChessScore(['p', 'p', 'p'])
#         self.assertTrue(score2 == score1)
#         self.assertTrue(score1 <= score2)
#
#
# class TestChessPosition(unittest.TestCase):
#     """Test the ChessPosition class."""
#
#     def test_simple_init(self):
#         """Sanity test for the ChessPosition class."""
#         init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#         self.assertTrue(hasattr(init_pos, 'get_white_score'))
#         self.assertTrue(hasattr(init_pos, 'get_black_score'))
#         self.assertTrue(hasattr(init_pos, 'white_is_winning'))
#         self.assertTrue(hasattr(init_pos, 'black_is_winning'))
#         self.assertTrue(hasattr(init_pos, 'is_equal'))
#
#     def test_get_white_and_black(self):
#         init_pos = ChessPosition('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3')
#         self.assertEqual(init_pos.get_white_score(), ChessScore(["P", "P", "P", "P", "P", "P", "P", "P", "K"]))
#         self.assertEqual(init_pos.get_white_score(), ChessScore(["p", "p", "p", "p", "p", "p", "p", "p", "k"]))
#
#     def test_white_and_black_winning_or_equal(self):
#         whites1 = ChessPosition('4k3/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#         equal_ones = ChessPosition('4k3/pppppppp/8/8/8/8/PPPPPPPP/4K3')
#         blacks1 = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/4K3')
#
#         self.assertTrue(whites1.white_is_winning())
#         self.assertFalse(blacks1.white_is_winning())
#         self.assertTrue(blacks1.black_is_winning())
#         self.assertFalse(whites1.black_is_winning())
#         self.assertTrue(equal_ones.is_equal())
#
#     def test_print(self):
#         init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#         self.assertEqual(init_pos.__str__(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#
#     def test_len(self):
#         init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#         self.assertEqual(len(init_pos), 32)
#
#     def test_pos(self):
#         init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
#         self.assertEqual(init_pos["A1"], "R")
#
#     def test_exceptions(self):
#         with self.assertRaises(ChessException) as cm1:
#             ChessPosition('pnbqkbnr/pppppppp/r7/8/8/8/PPPPPPPP/RNBQKBNR')
#         self.assertEqual(str(cm1.exception), "pawns")
#         with self.assertRaises(ChessException) as cm2:
#             ChessPosition('rnbqkbnr/pppppppp/kK6/8/8/8/PPPPPPPP/RNBQKBNR')
#         self.assertEqual(str(cm2.exception), "kings")
#         with self.assertRaises(ChessException) as cm3:
#             ChessPosition('rnbq1bnr/pppppppp/3Kk3/8/8/8/PPPPPPPP/RNBQ1BNR')
#         self.assertEqual(str(cm3.exception), "kings")
#
#
# if __name__ == '__main__':
#     unittest.main()