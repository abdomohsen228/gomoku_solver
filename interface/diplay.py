



from game.board import Board
from game.rules import check_winner


def test_game():
    board = Board(size=15)

    moves = [(7, 5), (7, 6), (7, 7), (7, 8), (7, 9)]
    for r, c in moves:
        board.place_move(r, c, 'X')

    board.print_board()

    if check_winner(board.grid, 'X'):
        print("Test Passed: Player X won!")
    else:
        print("Test Failed: Winning condition not detected.")

if __name__ == "__main__":
    test_game()
