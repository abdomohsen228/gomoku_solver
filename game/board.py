class Board:
    def __init__(self, size=15):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        print("   " + " ".join(f"{i:2}   " for i in range(self.size)))
        
        for idx, row in enumerate(self.grid):
            print(f"{idx:2}   " + "     ".join(row))

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == '.'

    def place_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.grid[row][col] = player
            return True
        return False

    def reset(self):
        self.grid = [['.' for _ in range(self.size)] for _ in range(self.size)]

    def get_empty_cells(self):
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == '.']
    
    def remove_move(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = '.'
