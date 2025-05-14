import math
from ai.boardEvaluator import evaluate_board
from game.rules import check_winner

def minimax(board, depth, maximizing_player, player, opponent):
    if check_winner(board.grid, player):
        return 10 - depth, None
    if check_winner(board.grid, opponent):
        return depth - 10, None
    if not board.get_empty_cells() or depth == 0:
        eval_score = evaluate_board(board.grid, player)
        return eval_score, None

    best_move = None

    if maximizing_player:
        max_eval = -math.inf
        for (r, c) in board.get_empty_cells():
            board.grid[r][c] = player
            eval, _ = minimax(board, depth - 1, False, player, opponent)
            board.grid[r][c] = '.'
            if eval > max_eval:
                max_eval = eval
                best_move = (r, c)
        return max_eval, best_move
    else:
        min_eval = math.inf
        for (r, c) in board.get_empty_cells():
            board.grid[r][c] = opponent
            eval, _ = minimax(board, depth - 1, True, player, opponent)
            board.grid[r][c] = '.'
            if eval < min_eval:
                min_eval = eval
                best_move = (r, c)
        return min_eval, best_move
