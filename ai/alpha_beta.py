
from ai.boardEvaluator import evaluate_board
from game.rules import check_winner

def alpha_beta_pruning(board, depth, alpha, beta, is_maximizing, max_player, min_player):
    player = max_player if is_maximizing else min_player
    opponent = min_player if is_maximizing else max_player

    # Base case
    if depth <= 0:
        return evaluate_board(board.grid, max_player), None, None

    # Terminal states
    if check_winner(board.grid, max_player):
        return 100000, None, None
    if check_winner(board.grid, min_player):
        return -100000, None, None
    if board.get_empty_cells() == []:
        return 0, None, None

    # Move ordering
    valid_moves = board.get_empty_cells()
    if not valid_moves:
        center = board.size // 2
        return 0, center, center

    best_move = None, None

    if is_maximizing:
        best_score = float('-inf')
        for x, y in valid_moves:
            board.place_move(x, y, player)
            score, _, _ = alpha_beta_pruning(board, depth - 1, alpha, beta, False, max_player, min_player)
            board.remove_move(x, y)

            if score > best_score:
                best_score = score
                best_move = x, y

            alpha = max(alpha, best_score)
            if beta <= alpha:
                break  # Beta cutoff
        return best_score, best_move[0], best_move[1]

    else:
        best_score = float('inf')
        for x, y in valid_moves:
            board.place_move(x, y, player)
            score, _, _ = alpha_beta_pruning(board, depth - 1, alpha, beta, True, max_player, min_player)
            board.remove_move(x, y)

            if score < best_score:
                best_score = score
                best_move = x, y

            beta = min(beta, best_score)
            if beta <= alpha:
                break  # Alpha cutoff
        return best_score, best_move[0], best_move[1]


