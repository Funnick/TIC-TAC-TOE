class TIC_TAC_TOE_game:
    def __init__(self):
        self._board = [[0 for i in range(3)] for j in range(3)]

    def get_valid_moves(self):
        moves = []

        for i in range(3):
            for j in range(3):
                if self._board[i][j] == 0:
                    moves.append([i, j])
                
        return moves

    def change_state(self, player, move):
        self._board[move[0]][move[1]] = player

    def game_status(self):
        for i in range(3):
            sum = 0
            for j in range(3):
                sum += self._board[i][j]
            if sum == 3:
                return 1
            elif sum == -3:
                return -1
        
        for j in range(3):
            sum = 0
            for i in range(3):
                sum += self._board[i][j]
            if sum == 3:
                return 1
            elif sum == -3:
                return -1
            
        sum = self._board[0][0] + self._board[1][1] + self._board[2][2]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1

        sum = self._board[0][2] + self._board[1][1] + self._board[2][0]
        if sum == 3:
            return 1
        elif sum == -3:
            return -1

        for i in range(3):
            for j in range(3):
                if self._board[i][j] == 0:
                    return 2

        return 0

    def get_board(self):
        temp_board = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                temp_board[i][j] = self._board[i][j]
        return temp_board

    def print_board(self):
        for i in range(3):
            print(self._board[i])