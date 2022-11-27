class ChessException(Exception):
    def __init__(self, text):
        self.text = text
        super().__init__(self.text)

    def __str__(self):
        return f'{self.text}'


class ChessScore:
    _points = {'r': 5, 'n': 3, 'b': 3, 'q': 9, 'k': 4, 'p': 1, '_': 0}

    def __init__(self, figures):
        self.figures = figures
        self.score = 0
        for figure in figures:
            self.score += self._points[figure]

    def __int__(self):
        return self.score

    def __add__(self, other):
        return self.score + int(other)

    def __sub__(self, other):
        return self.score - int(other)

    def __eq__(self, other):
        return self.score == int(other)

    def __ne__(self, other):
        return self.score != int(other)

    def __gt__(self, other):
        return self.score > int(other)

    def __ge__(self, other):
        return self.score >= int(other)

    def __lt__(self, other):
        return self.score < int(other)

    def __le__(self, other):
        return self.score <= int(other)


class ChessPosition:

    def __init__(self, fen):
        self.fen = fen
        self.chest_board = []
        self.number_of_figures = 0
        self.create_chess_board()
        flag_kings, flag_pawns = 0, 0
        white_kings, black_kings = 0, 0
        i, j = 0, 0
        for x in self.chest_board:
            for y in x:
                if y == 'K' or y == 'k':
                    if self.king_validate(i, j):
                        flag_kings = 1
                    if y == 'K':
                        white_kings += 1
                    if y == 'k':
                        black_kings += 1
                if i == 0 or i == 7:
                    if y == 'p' or y == 'P':
                        flag_pawns = 1
                j += 1
            i += 1
            j = 0
        if white_kings != 1 or black_kings != 1:
            flag_kings = 1

        if flag_kings:
            raise ChessException("kings")
        elif flag_pawns:
            raise ChessException("pawns")

    def create_chess_board(self):
        self.chest_board = self.fen.split("/")
        # print(self.chest_board)
        new_chess_board = []
        for x in self.chest_board:
            new_string = ''
            for y in x:
                num = ord(y) - ord('0')
                if 1 <= num <= 8:
                    for _ in range(0, num):
                        new_string += '_'
                else:
                    new_string += y
                    self.number_of_figures += 1
            # print(new_string)
            new_chess_board.append(new_string)
        self.chest_board = new_chess_board
        # print(self.chest_board)

    def king_validate(self, index_x, index_y):
        if index_y != 0:
            if self.chest_board[index_x][index_y - 1] == 'K' or self.chest_board[index_x][index_y - 1] == 'k':
                return 1
            if index_x != 7:
                if self.chest_board[index_x + 1][index_y - 1] == 'K' or self.chest_board[index_x + 1][
                    index_y - 1] == 'k':
                    return 1
        if index_x != 0 and index_y != 0:
            if self.chest_board[index_x - 1][index_y - 1] == 'K' or self.chest_board[index_x - 1][index_y - 1] == 'k':
                return 1
        if index_x != 0:
            if self.chest_board[index_x - 1][index_y] == 'K' or self.chest_board[index_x - 1][index_y] == 'k':
                return 1
            if index_y != 7:
                if self.chest_board[index_x - 1][index_y + 1] == 'K' or self.chest_board[index_x - 1][
                    index_y + 1] == 'k':
                    return 1
        if index_y != 7:
            if self.chest_board[index_x][index_y + 1] == 'K' or self.chest_board[index_x][index_y + 1] == 'k':
                return 1
        if index_y != 7 and index_x != 7:
            if self.chest_board[index_x + 1][index_y + 1] == 'K' or self.chest_board[index_x + 1][index_y + 1] == 'k':
                return 1
        if index_x != 7:
            if self.chest_board[index_x + 1][index_y] == 'K' or self.chest_board[index_x + 1][index_y] == 'k':
                return 1
        return 0

    def get_white_score(self):
        white_figures = []
        for x in self.fen:
            if 'A' <= x <= 'Z':
                white_figures.append(x.lower())

        return ChessScore(white_figures)

    def get_black_score(self):
        black_figures = []
        for x in self.fen:
            if 'a' <= x <= 'z':
                black_figures.append(x)

        return ChessScore(black_figures)

    def white_is_winning(self):
        return self.get_black_score() < self.get_white_score()

    def black_is_winning(self):
        return self.get_black_score() > self.get_white_score()

    def is_equal(self):
        return self.get_black_score() == self.get_white_score()

    def __str__(self):
        return self.fen

    def __len__(self):
        return self.number_of_figures

    def __getitem__(self, key):
        """A=1 B=2 C=3 D=4 E=5 F=6 G=7 H=8"""
        key = key.upper()
        indexes = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        # print(f'{(key[1],key[0])}')
        item = self.chest_board[-(int(key[1]))][indexes[key[0]]]
        return None if item == '_' else item
