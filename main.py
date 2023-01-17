from board import Board
from cli import CLI
from game import Game


def main() -> None:
    cli = CLI()
    game = Game(Board(), cli)
    game.play()


if __name__ == "__main__":
    main()
