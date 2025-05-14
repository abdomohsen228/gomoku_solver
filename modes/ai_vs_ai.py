from ai.alpha_beta import alpha_beta
from ai.minimax import minimax
from game.board import Board
from game.rules import check_winner

def ai_vs_ai():
    board = Board()
    ai_1 = 'X'
    ai_2 = 'O'
    curr_player = ai_1

    while True:
        board.print_board()
        print(f"Current Player: {curr_player}")
        
        if curr_player == ai_1:
            print("AI_1  is thinking...")
            _, move = minimax(board, depth=2, maximizing_player=True, player=ai_1, opponent=ai_2)
        # else:
        #     print("AI_2 is thinking...")
        #     _, move = alpha_beta(board, depth=2, alpha=float('-inf'), beta=float('inf'),
        #                          maximizing_player=True, player=ai_2, opponent=ai_1)
            
        if move:
            board.place_move(*move, curr_player)
            print(f"{curr_player} played: {move}")
        else:
            print("No valid moves left.")
            break

        if check_winner(board.grid, curr_player):
            board.print_board()
            print(f"Game Over: {curr_player} wins!")
            break

        if not board.get_empty_cells():
            board.print_board()
            print("Game Over: It's a draw!")
            break

        curr_player = ai_2 if curr_player == ai_1 else ai_1

