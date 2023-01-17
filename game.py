from dataclasses import dataclass
from random import randint

from board import Board
from cli import CLI


class Players:
    one = "X"
    two = "O"


@dataclass
class Game:
    board: Board
    cli: CLI

    def play(self):
        self.board.create_board()
        self.cli.display_rules()
        player = Players.one if randint(0, 1) == 1 else Players.two
        self.cli.display_start_game()

        while True:
            self.cli.display_current_round(player)
            self.cli.display_board(self.board)

            row, col = self.cli.read_position()
            row, col = row - 1, col - 1
            value_ok = False
            while not value_ok:
                value_ok = self.check_if_position_is_valid(row, col)
                if not value_ok:
                    self.cli.display_error_position(row + 1, col + 1)
                    row, col = self.cli.read_position()

            self.fix_spot(row, col, player)

            if self.is_winner(player):
                self.cli.display_winner(player)
                self.cli.display_board(self.board)
                break

            if self.board.is_board_filled():
                self.cli.display_tie()
                self.cli.display_board(self.board)
                break

            player = self.swap_player_turn(player)

    def swap_player_turn(self, player):
        return Players.one if player == Players.two else Players.two

    def check_if_position_is_valid(self, row, col) -> bool:
        if not isinstance(row, int) or not isinstance(col, int):
            return False

        if row < 0 or col < 0:
            return False

        if row > 4 or col > 4:
            return False

        return not self.board.board[row][col] != "-"

    def fix_spot(self, row, col, player):
        self.board.board[row][col] = player

    def is_winner(self, player):
        # Three in a row
        for i in range(3):
            if self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] == player:
                return True
            if self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i] == player:
                return True

        # Diagonals
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] == player:
            return True

        if self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] == player:
            return True

        return False

