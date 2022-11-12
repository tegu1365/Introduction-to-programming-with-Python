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
    cards = []

    def __init__(self, face_filter=None):

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
        for c in self.cards:
            print(c.get_face() + ": " + c.get_suit())
        return self.cards
