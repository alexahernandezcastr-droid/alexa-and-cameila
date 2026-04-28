import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [" " for _ in range(9)]
        self.buttons = []
        self._create_board()

    def _create_board(self):
        # Create a 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(
                self.window, 
                text=" ", 
                font=("Arial", 24), 
                width=5, 
                height=2,
                command=lambda i=i: self._on_click(i)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def _on_click(self, index):
        # Check if square is already taken or game over
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            
            if self._check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self._reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self._reset_game()
            else:
                # Switch player
                self.current_player = "O" if self.current_player == "X" else "X"

    def _check_winner(self):
        # All possible winning combinations
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
            (0, 4, 8), (2, 4, 6)             # Diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return True
        return False

    def _reset_game(self):
        self.board = [" " for _ in range(9)]
        for button in self.buttons:
            button.config(text=" ")
        self.current_player = "X"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
