import random

class RandomBot:
    def play(self, moves, board):
        r = random.randint(0, len(moves) - 1)
        return moves[r]



class VBot:
    def __init__(self, player, V, weights):
        self.player = player
        self.V = V
        self.weights = weights

    def play(self, moves, board):
        best_move = moves[0]
        best_score = self.V(self.get_successor_board(moves[0], board), self.weights)
        best_score = best_score[len(best_score) - 1]
        
        for m in moves:
            b_score = self.V(self.get_successor_board(m, board), self.weights)
            b_score = b_score[len(b_score) - 1]

            if best_score < b_score:
                best_score = b_score
                best_move = m

        return best_move

    def get_successor_board(self, move, board):
        temp_board = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                temp_board[i][j] = board[i][j]
        temp_board[move[0]][move[1]] = self.player
        return temp_board


class MixedBot:
    def __init__(self, player, V, weights):
        self.player = player
        self.V = V
        self.weights = weights

    def play(self, moves, board):
        if random.random() >= 0.5:
            best_move = moves[0]
            best_score = self.V(self.get_successor_board(moves[0], board), self.weights)
            best_score = best_score[len(best_score) - 1]

            for m in moves:
                b_score = self.V(self.get_successor_board(m, board), self.weights)
                b_score = b_score[len(b_score) - 1]
                
                if best_score < b_score:
                    best_score = b_score
                    best_move = m
            return best_move
        else:
            return moves[random.randint(0, len(moves) - 1)]
            

    def get_successor_board(self, move, board):
        temp_board = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                temp_board[i][j] = board[i][j]
        temp_board[move[0]][move[1]] = self.player
        return temp_board