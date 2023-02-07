import math
import time
from player import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToe():
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(letter): # remove square param from the starting code
                self.current_winner = letter
            return True
        return False
    # remove square param from the starting code
    def winner(self, letter):
        #this function should have the logic to check for the winning condition
        #for instance, three O's in a straight line
        win_conditions = [
            self.board[0] == self.board[1] == self.board[2] == letter,
            self.board[3] == self.board[4] == self.board[5] == letter,
            self.board[6] == self.board[7] == self.board[8] == letter,
            self.board[0] == self.board[3] == self.board[6] == letter,
            self.board[1] == self.board[4] == self.board[7] == letter,
            self.board[2] == self.board[5] == self.board[8] == letter,
            self.board[0] == self.board[4] == self.board[8] == letter,
            self.board[2] == self.board[4] == self.board[6] == letter
        ]
        for cond in win_conditions:
            if cond:
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        #this function should compute the available moves on the board
        avail_moves = []
        for i in range(len(self.board)):
            if self.board[i] == " ":
                avail_moves.append(i)
        return avail_moves


def play(game, x_player, o_player, print_game=True):
    #the complete logic for the game should be defined here
    print("Welcome to Tic-Tac-Toe")
    print("The board is marked with numbers as following: ")
    game.print_board_nums()
    print("Current board:")
    while game.available_moves():
        game.make_move(x_player.get_move(game), "X")
        game.print_board()
        if game.winner("X"):
            print("Player X wins!")
            exit()
        if game.available_moves():
            game.make_move(o_player.get_move(game), "O")
            if game.winner("O"):
                print("Player O wins!")
                exit()
    game.print_board()
    # when there is no available move, it is a tie
    print("Its a tie!")
    exit()


if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

