import tkinter as tk
from tkinter import messagebox
import random
import subprocess

root = tk.Tk()
root.title("Tic Tac Toe")

board = [""] * 9
buttons = []
current_player = "X"

difficulty = tk.StringVar(value="Easy")  # Default difficulty

def check_winner():
    win_combinations = [(0,1,2),(3,4,5),(6,7,8),
                        (0,3,6),(1,4,7),(2,5,8),
                        (0,4,8),(2,4,6)]
    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def ai_move():
    if difficulty.get() == "Easy":
        empty_cells = [i for i in range(9) if board[i] == ""]
        move = random.choice(empty_cells)
    else:
        move = best_move()
    board[move] = "O"
    buttons[move].config(text="O", state="disabled")
    check_game_over()

def best_move():
    # Simple minimax for harder difficulty
    best_score = -float("inf")
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move

def minimax(board_state, is_maximizing):
    result = check_winner()
    if result == "X":
        return -1
    elif result == "O":
        return 1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if board_state[i] == "":
                board_state[i] = "O"
                score = minimax(board_state, False)
                board_state[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float  ("inf")
        for i in range(9):
            if board_state[i] == "":
                board_state[i] = "X"
                score = minimax(board_state, True)
                board_state[i] = ""
                best_score = min(score, best_score)
        return best_score

def play_video(video_path):
    subprocess.Popen(["start", "", video_path], shell=True)  # Windows
    # For macOS: subprocess.Popen(["open", video_path])
    # For Linux: subprocess.Popen(["xdg-open", video_path])

def check_game_over():
    winner = check_winner()
    if winner:
        if winner == "X":
            play_video(r"C:\Users\Akilan\cloud\AI\EX.5_Tic-Tac-Toe\Soorarai pottru climax scene - Cinemas (720p, h264).mp4")
        elif winner == "O":
            play_video(r"C:\Users\Akilan\cloud\AI\EX.5_Tic-Tac-Toe\gp muthu nakku dialogue - SIVA (480p, h264).mp4")
        else:
            play_video(r"C:\Users\Akilan\cloud\AI\EX.5_Tic-Tac-Toe\neeum nanum vera illa da rendu peru loosu pu.... da  natpu status 🥰 - TN PAIN GAMEING FF (720p, h264).mp4")
        reset_game()

def player_move(i):
    if board[i] == "":
        board[i] = "X"
        buttons[i].config(text="X", state="disabled")
        check_game_over()
        if "" in board:
            ai_move()

def reset_game():
    global board
    board = [""] * 9
    for btn in buttons:
        btn.config(text="", state="normal")

# Difficulty dropdown
tk.Label(root, text="Difficulty:").grid(row=0, column=0, columnspan=3)
tk.OptionMenu(root, difficulty, "Easy", "Hard").grid(row=0, column=3, columnspan=2)

# Create board buttons
for i in range(9):
    btn = tk.Button(root, text="", width=10, height=3, 
                    command=lambda i=i: player_move(i))
    btn.grid(row=1 + i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
