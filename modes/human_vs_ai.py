from game.board import Board
from ai.minimax import minimax
from game.rules import check_winner

def human_vs_ai():
    board = Board()
    human = 'X'
    ai = 'O'
    current_player = human

    player_name = input("Enter your name: ").strip() or "Player"

    while True:
        board.print_board()

        if current_player == human:
            try:
                move = input(f"{player_name}, enter your move (row col): ")
                r, c = map(int, move.strip().split())
            except:
                print("Invalid input format. Try again.")
                continue

            if not board.place_move(r, c, human):
                print("Invalid move. Try again.")
                continue
        else:
            print("AI is thinking...")
            _, move = minimax(board, depth=2, maximizing_player=True, player=ai, opponent=human)
            if move:
                board.place_move(*move, ai)
                print(f"AI played: {move}")
            else:
                print("No moves left for AI.")
                break

        # Check winner
        if check_winner(board.grid, current_player):
            board.print_board()
            winner = player_name if current_player == human else "AI"
            print(f"{winner} wins!")
            break

        if not board.get_empty_cells():
            board.print_board()
            print("It's a draw!")
            break

        current_player = ai if current_player == human else human
