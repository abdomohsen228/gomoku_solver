import tkinter as tk
from tkinter import messagebox

class StartMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku - Start Menu")
        
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.frame = tk.Frame(self.root, bg="#f0f0f0")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.ai_vs_ai_button = tk.Button(
            self.frame,
            text="AI vs AI",
            font=("Arial", 24),
            bg="#4CAF50",
            fg="white",
            width=15,
            command=self.ai_vs_ai
        )
        self.ai_vs_ai_button.pack(pady=10)

        self.human_vs_ai_button = tk.Button(
            self.frame,
            text="Human vs AI",
            font=("Arial", 24),
            bg="#4CAF50",
            fg="white",
            width=15,
            command=self.human_vs_ai
        )
        self.human_vs_ai_button.pack(pady=10)

    def ai_vs_ai(self):
        self.root.destroy()
        from gui.ai_vs_ai_gui import GomokuAIVsAIGUI
        root = tk.Tk()
        app = GomokuAIVsAIGUI(root)
        root.mainloop()

    def human_vs_ai(self):
        self.root.destroy()  
        from gui.main_gui import GomokuGUI
        root = tk.Tk()
        app = GomokuGUI(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = StartMenu(root)
    root.mainloop()
