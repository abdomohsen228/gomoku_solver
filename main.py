from game.board import Board
from interface.diplay import test_game
from modes.human_vs_ai import human_vs_ai

def main():
    b = Board()
    # b.print_board()
    # print(b.get_empty_cells())
    # t  = test_game();
    human_vs_ai()


if __name__ == "__main__":
    main()
