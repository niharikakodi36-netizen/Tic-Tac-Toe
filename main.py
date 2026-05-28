import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("400x500")
root.config(bg="#1e1e2f")

# Variables
current_player = "X"
board = [""] * 9

# Title
title_label = tk.Label(
    root,
    text="Tic Tac Toe",
    font=("Helvetica", 24, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title_label.pack(pady=20)

# Status Label
status_label = tk.Label(
    root,
    text="Player X's Turn",
    font=("Arial", 14),
    bg="#1e1e2f",
    fg="#00ffcc"
)
status_label.pack(pady=10)

# Frame for Buttons
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

buttons = []

# Check Winner Function
def check_winner():
    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in winning_combinations:
        a, b, c = combo

        if board[a] == board[b] == board[c] != "":
            return board[a]

    return None

# Check Draw
def check_draw():
    return "" not in board

# Button Click Function
def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        winner = check_winner()

        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} Wins!")
            restart_game()
            return

        if check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            restart_game()
            return

        current_player = "O" if current_player == "X" else "X"

        status_label.config(
            text=f"Player {current_player}'s Turn"
        )

# Restart Game Function
def restart_game():
    global current_player
    current_player = "X"

    status_label.config(text="Player X's Turn")

    for i in range(9):
        board[i] = ""
        buttons[i].config(text="")

# Create Board Buttons
for i in range(9):
    button = tk.Button(
        frame,
        text="",
        font=("Arial", 24, "bold"),
        width=5,
        height=2,
        bg="#2d2d44",
        fg="white",
        activebackground="#00adb5",
        relief="flat",
        command=lambda i=i: button_click(i)
    )

    button.grid(row=i//3, column=i%3, padx=5, pady=5)

    buttons.append(button)

# Restart Button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14, "bold"),
    bg="#ff4d4d",
    fg="white",
    padx=20,
    pady=10,
    relief="flat",
    command=restart_game
)
restart_button.pack(pady=20)

# Run App
root.mainloop()