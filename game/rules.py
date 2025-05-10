def check_winner(board, player, to_win=5):
    size = len(board)

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    for r in range(size):
        for c in range(size):
            if board[r][c] != player:
                continue
            for dr, dc in directions:
                count = 1
                nr, nc = r + dr, c + dc
                while 0 <= nr < size and 0 <= nc < size and board[nr][nc] == player:
                    count += 1
                    if count == to_win:
                        return True
                    nr += dr
                    nc += dc
    return False
