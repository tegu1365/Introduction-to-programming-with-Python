import unittest

from solution import Card, Deck, Player, Game, Belot, Poker


class TestCard(unittest.TestCase):
    """Test the Card class."""

    def test_simple_init(self):
        """Sanity test for the Card class."""
        card = Card('clubs', '2')
        self.assertTrue(hasattr(card, 'get_suit'))
        self.assertTrue(hasattr(card, 'get_face'))


class TestDeck(unittest.TestCase):
    """Test the Deck class."""

    def test_simple_init(self):
        """Sanity test for the Deck class."""
        deck = Deck()
        self.assertTrue(hasattr(deck, 'cut'))
        self.assertTrue(hasattr(deck, 'shuffle'))
        self.assertTrue(hasattr(deck, 'get_cards'))

    def test_deck_with_8_cards(self):
        deck = Deck(['A', 'K'])
        self.assertTrue(deck.get_cards(),
                        [Card('clubs', 'A'), Card('diamonds', 'A'), Card('hearts', 'A'), Card('spades', 'A'),
                         Card('clubs', 'K'), Card('diamonds', 'K'), Card('hearts', 'K'), Card('spades', 'K')])

        '''print("_______________________________________________________")
        deck.shuffle()
        deck.get_cards()
        print("_______________________________________________________")
        deck.cut()
        deck.get_cards()'''


class TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def test_simple_init(self):
        """Sanity test for the Player class."""
        player = Player()
        self.assertTrue(hasattr(player, 'get_cards'))


class TestGame(unittest.TestCase):
    """Test the Game class."""

    def test_simple_init(self):
        """Sanity test for the Game class."""
        game = Game(2, 'rtl', (1, 2))
        self.assertTrue(hasattr(game, 'get_players'))
        self.assertTrue(hasattr(game, 'prepare_deck'))
        self.assertTrue(hasattr(game, 'deal'))
        self.assertTrue(hasattr(game, 'get_deck'))

        # print(len(game.get_deck().get_cards()))

        # print("__________________________________________")
        game1 = Game(4, 'ltr', (1, 1))
        # print(len(game1.get_deck().get_cards()))
        # print("__________________________________________")
        game1.deck = Deck(['A', 'K'])
        # print(len(game1.get_deck().get_cards()))
        players = game1.get_players()
        game1.deal(players[1])


class TestBelot(unittest.TestCase):
    """Test the Belot class."""

    def test_simple_init(self):
        """Sanity test for the Belot class."""
        belot = Belot()
        self.assertIsInstance(belot, Game)
        players = belot.get_players()
        for c in belot.get_deck().get_cards():
            print(f"{c.get_face()}: {c.get_suit()}")
        belot.prepare_deck()
        belot.deal(players[0])
        # Play the game, argue about the rules, curse, fight, argue about who should deal the cards during second round...
        belot.prepare_deck()
        print("____________________________________")
        for c in belot.get_deck().get_cards():
            print(f"{c.get_face()}: {c.get_suit()}")
        belot.deal(players[1])


class TestPoker(unittest.TestCase):
    """Test the Poker class."""

    def test_simple_init(self):
        """Sanity test for the Poker class."""
        poker = Poker()
        self.assertIsInstance(poker, Game)


if __name__ == '__main__':
    unittest.main()
