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
        if face_filter is not None:
            cards = []
            for face in face_filter:
                for s in suits:
                    cards.append(Card(s, face))
