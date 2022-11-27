import unittest

from solution import *


class TestChessException(unittest.TestCase):
    """Test the ChessException class."""

    def test_existence(self):
        """Sanity test for the ChessException class."""
        exception = ChessException('Paul Morphy')


class TestChessScore(unittest.TestCase):
    """Test the ChessScore class."""

    def test_simple_init(self):
        """Sanity test for the ChessScore class."""
        score = ChessScore(['p'])
        self.assertEqual(int(score), 1)

    def test_simple_statements(self):
        score_1 = ChessScore(['p'])
        score_2 = ChessScore(['p', 'k'])
        self.assertTrue(score_1 < score_2)
        self.assertFalse(score_1 >= score_2)
        self.assertFalse(score_1 == score_2)


class TestChessPosition(unittest.TestCase):
    """Test the ChessPosition class."""

    def test_simple_init(self):
        """Sanity test for the ChessPosition class."""
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertTrue(hasattr(init_pos, 'get_white_score'))
        self.assertTrue(hasattr(init_pos, 'get_black_score'))
        self.assertTrue(hasattr(init_pos, 'white_is_winning'))
        self.assertTrue(hasattr(init_pos, 'black_is_winning'))
        self.assertTrue(hasattr(init_pos, 'is_equal'))

    def test_raises_exception_kings(self):
        with self.assertRaises(ChessException) as cm:
            ChessPosition('rnbq1bnr/ppp1pppp/3p4/5kK1/3P4/8/PPP2PPP/RNBQ1BNR')
        the_exception = cm.exception
        self.assertEqual(the_exception.__str__(), 'kings')

    def test_raises_exception_multi_kings(self):
        with self.assertRaises(ChessException) as cm:
            ChessPosition('knbq1bnr/p1p1pppp/2Kp4/8/3P4/4K3/PPP2PPP/RNBQ1BNR')
        the_exception = cm.exception
        self.assertEqual(the_exception.__str__(), 'kings')

    def test_raises_exception_pawns(self):
        with self.assertRaises(ChessException) as cm:
            ChessPosition('knbqpbnr/p1p2ppp/2p5/8/3P4/4K3/PPP2PPP/RNBQ1BNR')
        the_exception = cm.exception
        self.assertEqual(the_exception.__str__(), 'pawns')

    def test_raises_multiple_exceptions(self):
        with self.assertRaises(ChessException) as cm:
            ChessPosition('knbqpbnr/p1p2ppp/2p5/8/3P4/4K3/PPPK1PPP/RNBQ1BNR')
        the_exception = cm.exception
        self.assertEqual(the_exception.__str__(), 'kings')

    def test_len_function(self):
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertEqual(len(init_pos), 32)
        figure_4 = ChessPosition("1k6/8/4b3/8/1K4p1/3R4/8/8")
        self.assertEqual(len(figure_4), 5)

    def test_str_func(self):
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertEqual(init_pos.__str__(), 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')

    def test_get_figure(self):
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertEqual(init_pos['E2'], 'P')
        self.assertEqual(init_pos['H8'], 'r')
        self.assertEqual(init_pos['A6'], None)

    def test_get_score(self):
        figure_4 = ChessPosition("8/2k5/8/8/1P3N2/8/4K3/8")
        self.assertEqual(figure_4.get_black_score(), 4)
        self.assertEqual(figure_4.get_white_score(), 4 + 1 + 3)

    def test_score_is_equal(self):
        figure_4 = ChessPosition("8/2k5/8/8/1P3N2/8/4K3/8")
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertTrue(init_pos.is_equal())
        self.assertFalse(figure_4.is_equal())
        self.assertTrue(figure_4.white_is_winning())
        self.assertFalse(figure_4.black_is_winning())


if __name__ == '__main__':
    unittest.main()
