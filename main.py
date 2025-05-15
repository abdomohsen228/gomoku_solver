from game.board import Board
from interface.diplay import test_game
from modes.ai_vs_ai import ai_vs_ai
from modes.human_vs_ai import human_vs_ai

def main():
    while True:
        print("\n=== Gomoku Game Menu ===")
        print("1. Human vs AI")
        print("2. AI vs AI")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            print("Starting Human vs AI...")
            human_vs_ai()
        elif choice == "2":
            print("Starting AI vs AI...")
            ai_vs_ai()
        elif choice == "3":
            print("Exiting game. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()