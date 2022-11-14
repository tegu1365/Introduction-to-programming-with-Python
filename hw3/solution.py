from random import randint, shuffle

faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['clubs', 'diamonds', 'hearts', 'spades']


class Card:

    def __init__(self, suit, face):
        """ Define card with suit:  'clubs', 'diamonds', 'hearts', 'spades' and face:  '2',...'9', '10', 'J', 'Q',
        'K' или 'A' """
        self._suit = suit
        self._face = face

    def get_suit(self):
        return self._suit

    def get_face(self):
        return self._face


class Deck:

    def __init__(self, face_filter=None):

        self.cards = []
        if face_filter is not None:
            # print("Hi")
            for face in face_filter:
                for suit in suits:
                    self.cards.append(Card(suit, face))
        else:
            for face in faces:
                for suit in suits:
                    self.cards.append(Card(suit, face))

        '''for c in self.cards:
            print(c.get_face() + ": " + c.get_suit())'''

    def cut(self):
        index = randint(1, len(self.cards) - 1)
        first_half = self.cards[:index]
        second_half = self.cards[index:]
        self.cards = second_half + first_half

    def shuffle(self):
        shuffle(self.cards)

    def get_cards(self):
        ''' for c in self.cards:
            print(c.get_face() + ": " + c.get_suit())'''
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def deal_card(self):
        return self.cards.pop()


class Player:

    def __init__(self):
        self.cards = []
        # self.name = name

    def get_cards(self):
        return self.cards

    def add_card(self, card):
        self.cards.append(card)

    def give_cards(self):
        self.cards = []

    def print_cards(self):
        for c in self.cards:
            print(" - " + c.get_face() + ": " + c.get_suit())


class Game:

    def __init__(self, number_of_players, dealing_direction, dealing_instructions):
        self.number_of_players = number_of_players
        self.dealing_direction = dealing_direction
        self.dealing_instructions = dealing_instructions
        self.deck = Deck(faces)
        self.players = []
        for _ in range(number_of_players):
            self.players.append(Player())

    def get_players(self):
        return self.players

    def prepare_deck(self):
        for p in self.players:
            cards = p.get_cards()
            for c in cards:
                # print(f"getting card: {c.face}: {c.suit} from player {p.name}")
                self.deck.add_card(c)
            p.give_cards()

        self.deck.shuffle()
        self.deck.cut()

    def deal(self, start_player):
        start_index = self.players.index(start_player)

        if self.dealing_direction == 'rtl':
            before = self.players[:start_index + 1]
            after = self.players[start_index + 1:]
            before.reverse()
            after.reverse()
            self.players = before + after
        else:
            before = self.players[:start_index]
            after = self.players[start_index:]
            self.players = after + before

        # for p in self.players:
        # print(f"{p.name}")

        for deal_turn in self.dealing_instructions:
            for player in self.players:
                for _ in range(deal_turn):
                    card = self.deck.deal_card()
                    player.add_card(card)
                    # print(f"Player {p.name} gets {card.face}: {card.suit}")

        # for p in self.players:
        # print(f"{p.name}: {p.print_cards()}")

    def get_deck(self):
        return self.deck


class Belot(Game):
    def __init__(self):
        super().__init__(number_of_players=4, dealing_direction='ltr', dealing_instructions=(2, 3, 3))
        self.deck = Deck(['7', '8', '9', '10', 'J', 'Q', 'K', 'A'])

        '''for c in self.deck.get_cards():
            print(f"{c.get_face}: {c.get_suit}")'''


class Poker(Game):
    def __init__(self):
        super().__init__(number_of_players=9, dealing_direction='rtl', dealing_instructions=(1, 1, 1, 1, 1))
        self.deck = Deck(faces)
