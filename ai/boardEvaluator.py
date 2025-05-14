def evaluate_board(board, player):
    opponent = 'O' if player == 'X' else 'X'
    score = 0

    patterns = [
        (player * 5, 100000),
        (player * 4 + '.', 10000),
        ('.' + player * 4, 10000),
        (player * 3 + '..', 1000),
        ('..' + player * 3, 1000),
        (player * 2 + '...', 100),
        ('...' + player * 2, 100),

        (opponent * 5, -100000),
        (opponent * 4 + '.', -8000),
        ('.' + opponent * 4, -8000),
        (opponent * 3 + '..', -800),
        ('..' + opponent * 3, -800),
        (opponent * 2 + '...', -80),
        ('...' + opponent * 2, -80),
    ]

    lines = []

    size = len(board)

    for i in range(size):
        row = ''.join(board[i])
        col = ''.join(board[j][i] for j in range(size))
        lines.append(row)
        lines.append(col)

    for r in range(size - 4):
        for c in range(size - 4):
            diag = ''.join(board[r + i][c + i] for i in range(5))
            lines.append(diag)

    for r in range(4, size):
        for c in range(size - 4):
            diag = ''.join(board[r - i][c + i] for i in range(5))
            lines.append(diag)

    for line in lines:
        for pattern, value in patterns:
            score += line.count(pattern) * value

    return score
