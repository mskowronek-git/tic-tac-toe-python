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

    # New function for testing doc generation
    def restart_game(self):
        self.board.create_board()
        self.play()

    # Aktuell prüft is_winner nur für ein 3×3-Board. 
    # Wenn du ein größeres Spielfeld (z. B. 5×5) verwendest, funktioniert das nicht korrekt.
    # Du kannst die Gewinnprüfung so ändern, dass sie drei gleiche Zeichen in Folge erkennt – egal wo sie stehen.
    def is_winner(self, player):
        size = len(self.board.board)
        win_length = 3  # Anzahl der gleichen Zeichen in Folge für Sieg

        # Zeilen und Spalten prüfen
        for i in range(size):
            for j in range(size - win_length + 1):
                # Zeile
                if all(self.board.board[i][j + k] == player for k in range(win_length)):
                    return True
                # Spalte
                if all(self.board.board[j + k][i] == player for k in range(win_length)):
                    return True

        # Diagonalen prüfen
        for i in range(size - win_length + 1):
            for j in range(size - win_length + 1):
                # Hauptdiagonale
                if all(self.board.board[i + k][j + k] == player for k in range(win_length)):
                    return True
                # Nebendiagonale
                if all(self.board.board[i + k][j + win_length - 1 - k] == player for k in range(win_length)):
                    return True
        return False


