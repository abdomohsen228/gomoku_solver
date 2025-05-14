# gui/main_gui.py
import tkinter as tk
from tkinter import messagebox
from game.board import Board
from game.rules import check_winner
from ai.minimax import minimax

CELL_SIZE = 40
BOARD_SIZE = 15
PADDING = 20

class GomokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku - Human vs AI")

        self.canvas = tk.Canvas(root, width=BOARD_SIZE * CELL_SIZE + PADDING * 2,height=BOARD_SIZE * CELL_SIZE + PADDING * 2, bg="#0cb13f")
        self.canvas.pack()

        self.board = Board(size=BOARD_SIZE)
        self.human = 'X'
        self.ai = 'O'
        self.current_player = self.human

        self.canvas.bind("<Button-1>", self.click_handler)
        self.draw_board()

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

    def click_handler(self, event):
        if self.current_player != self.human:
            return

        col = (event.x - PADDING + CELL_SIZE // 2) // CELL_SIZE
        row = (event.y - PADDING + CELL_SIZE // 2) // CELL_SIZE

        if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
            return

        if self.board.place_move(row, col, self.human):
            self.draw_piece(row, col, self.human)
            if self.check_game_over(self.human):
                return
            self.root.after(300, self.ai_move)

    def ai_move(self):
        print("AI is thinking...")
        _, move = minimax(self.board, depth=2, maximizing_player=True, player=self.ai, opponent=self.human)
        if move:
            r, c = move
            self.board.place_move(r, c, self.ai)
            self.draw_piece(r, c, self.ai)
            if self.check_game_over(self.ai):
                return
        self.current_player = self.human

    def check_game_over(self, player):
        if check_winner(self.board.grid, player):
            winner = "You" if player == self.human else "AI"
            messagebox.showinfo("Game Over", f"{winner} won!")
            self.root.quit()
            return True
        elif not self.board.get_empty_cells():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.root.quit()
            return True
        self.current_player = self.ai if player == self.human else self.human
        return False

if __name__ == "__main__":
    root = tk.Tk()
    app = GomokuGUI(root)
    root.mainloop()
