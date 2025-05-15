import tkinter as tk
from tkinter import messagebox
from game.board import Board
from game.rules import check_winner
from ai.minimax import minimax
from ai.alpha_beta import alpha_beta_pruning

CELL_SIZE = 40
BOARD_SIZE = 15
PADDING = 20

class GomokuAIVsAIGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku - AI vs AI")

        self.canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE + PADDING * 2, height=BOARD_SIZE * CELL_SIZE + PADDING * 2, bg="#0cb13f")
        self.canvas.pack()

        self.board = Board(size=BOARD_SIZE)
        self.ai1 = 'X' 
        self.ai2 = 'O' 
        self.current_player = self.ai1

        self.draw_board()
        self.root.after(500, self.play_ai_move)

    def draw_board(self):
        for i in range(BOARD_SIZE):
            x = y = PADDING + i * CELL_SIZE
            self.canvas.create_line(PADDING, y, PADDING + (BOARD_SIZE - 1) * CELL_SIZE, y, fill="#444")
            self.canvas.create_line(x, PADDING, x, PADDING + (BOARD_SIZE - 1) * CELL_SIZE, fill="#444")

    def draw_piece(self, row, col, player):
        x = PADDING + col * CELL_SIZE
        y = PADDING + row * CELL_SIZE
        radius = CELL_SIZE // 3
        color = "red" if player == 'X' else "blue"
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="black")

    def play_ai_move(self):
        if not self.board.get_empty_cells():
            return

        print(f"{'AI1' if self.current_player == self.ai1 else 'AI2'} is thinking...")
        if self.current_player == self.ai1:
            _, move = minimax(self.board, depth=2, maximizing_player=True, player=self.ai1, opponent=self.ai2)
        else:
            score, row, col = alpha_beta_pruning(self.board, depth=2, alpha=float('-inf'), beta=float('inf'), is_maximizing=True, max_player=self.ai2, min_player=self.ai1)
            move = [row, col] if row is not None and col is not None else None

        if move:
            r, c = move
            self.board.place_move(r, c, self.current_player)
            self.draw_piece(r, c, self.current_player)
            if self.check_game_over(self.current_player):
                return

        self.current_player = self.ai2 if self.current_player == self.ai1 else self.ai1
        self.root.after(500, self.play_ai_move)

    def check_game_over(self, player):
        if check_winner(self.board.grid, player):
            winner = "AI1" if player == self.ai1 else "AI2"
            messagebox.showinfo("Game Over", f"{winner} won!")
            self.root.quit()
            return True
        elif not self.board.get_empty_cells():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.root.quit()
            return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = GomokuAIVsAIGUI(root)
    root.mainloop()
