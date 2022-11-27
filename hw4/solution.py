class ChessException(Exception):
    def __init__(self, text):
        self.text = text
        super().__init__(self.text)

    def __str__(self):
        return f'{self.text}'


class ChessPosition:

    def __init__(self, fen):
        self.fen = fen
        self.chest_board = []
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
        pass

    def get_black_score(self):
        pass

    def white_is_winning(self):
        pass

    def black_is_winning(self):
        pass

    def is_equal(self):
        pass
