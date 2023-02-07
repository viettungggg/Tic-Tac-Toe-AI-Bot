import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    # assign value to game states. Win: 1. Lose: -1. Tie: 0.
    def evaluate(self, game):
        if game.winner("X"):
            return 1;
        elif game.winner("O"):
            return -1;
        return 0


    def minimax(self, game, depth, maximizing):
        # base case when the game end, returning value 1, -1, or 0
        if game.winner("X"):
            return (1, None)
        if game.winner("O"):
            return (-1, None)
        if not game.empty_squares():
            return (0, None)

        best_move = None
        # minimax algorithm to get the best score (maximizer) and save the move accordingly
        if maximizing:
            best_score = float('-inf')
            # check for the move with best score in all available moves
            for move in game.available_moves():
                game.make_move(move, "X")
                cur_score, _ = self.minimax(game, depth + 1, not maximizing)
                # reset the move after each try
                game.board[move] = " "
                if cur_score > best_score:
                    best_score = cur_score
                    best_move = move
        else:
            best_score = float('inf')
            # check for the move with the lowest score (minimizer) in all available moves
            for move in game.available_moves():
                game.make_move(move, "O")
                cur_score, _ = self.minimax(game, depth + 1, not maximizing)
                # reset the move after each try
                game.board[move] = " "
                if cur_score < best_score:
                    best_score = cur_score
                    best_move = move
        return (best_score, best_move)

    def get_move(self, game):
        # only need to get the move
        _, best_move = self.minimax(game, 0, True)
        return best_move



