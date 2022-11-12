from random import randint, shuffle

suits = ['clubs', 'diamonds', 'hearts', 'spades']


class Card:

    def __init__(self, suit, face):
        ''' Define card with suit:  'clubs', 'diamonds', 'hearts', 'spades' and face:  '2',...'9', '10', 'J', 'Q',
        'K' или 'A' '''
        self.suit = suit
        self.face = face

    def get_suit(self):
        return self.suit

    def get_face(self):
        return self.face


class Deck:

    def __init__(self, face_filter=None):
        self.cards = []
        if face_filter is not None:
            for face in face_filter:
                for s in suits:
                    self.cards.append(Card(s, face))

        '''for c in self.cards:
            print(c.get_face() + ": " + c.get_suit())'''

    def cut(self):
        index = randint(1, len(self.cards))
        first_half = self.cards[:index]
        second_half = self.cards[index:]
        self.cards = second_half + first_half

    def shuffle(self):
        shuffle(self.cards)

    def get_cards(self):
        """ for c in self.cards:
             print(c.get_face() + ": " + c.get_suit())"""
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def deal_card(self):
        card = self.cards[-1]
        self.cards.remove(card)
        return card


class Player:

    def __init__(self):
        self.cards = Deck()

    def get_cards(self):
        return self.cards.get_cards()

    def add_card(self, card):
        self.cards.add_card(card)

    def give_card(self, card):
        self.cards.cards.remove(card)


class Game:
    def __init__(self, number_of_players, dealing_direction, dealing_instructions):
        self.number_of_players = number_of_players
        self.dealing_direction = dealing_direction
        self.dealing_instructions = dealing_instructions

        self.players = []
        for i in range(0, number_of_players):
            self.players.append(Player())

        self.deck = Deck()

    def get_players(self):
        return self.players

    def prepare_deck(self):
        for p in self.players:
            for c in p.get_cards():
                self.deck.add_card(c)
                p.give_card(c)

        self.deck.shuffle()
        self.deck.cut()

    def deal(self, start_player):
        pass

    def get_deck(self):
        return self.deck
