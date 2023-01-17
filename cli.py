from dataclasses import dataclass

from board import Board


@dataclass
class CLI:
    def display_board(self, board: Board) -> None:
        for row in board.board:
            for item in row:
                print(item, end=" ")
            print()

    def display_rules(self) -> None:
        print("Tic Tac Toe...\n Welcome to the game.")
        print("\nRules are simple")
        print("1. The game is played on a grid that's 3 squares by 3 squares.")
        print("2. You are X, your friend is O. Players take turns putting their marks in empty squares.")
        print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
        print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
        print("5. Put values between 1 and 3 for row and column")

    def display_current_round(self, player: str):
        print(f"Player {player} turn\n")

    def display_start_game(self) -> None:
        print("Starting game...\n")

    def display_tie(self) -> None:
        print("It's a tie..")

    def display_winner(self, winner_name: str) -> None:
        print("*" * 20)
        print("CONGRATULATIONS!\n")
        print(f"Player {winner_name} wins the game")
        print("This is the end, my friend!\n")

    def display_error_position(self, row, col) -> None:
        print(f"Positions in row: {row} and col: {col} are not valid. Please insert new values!\n")

    def read_position(self) -> tuple:
        print('**')
        try:
            row, col = list(map(int, input("Enter row value <space> col value to fix a spot: ").split()))
            return row, col
        except ValueError as ex:
            raise Exception("Values differents from integer is not allowed")

