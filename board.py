from dataclasses import dataclass, field

@dataclass
class Board:
    size: int = 3  # Standardgröße des Spielfelds
    board: list = field(default_factory=list)

    def create_board(self):
        self.board = [['-' for _ in range(self.size)] for _ in range(self.size)]

    def is_board_filled(self):
        return all(cell != '-' for row in self.board for cell in row)
