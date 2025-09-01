import tkinter as tk
import math
import subprocess
import os

board = [" " for _ in range(9)]
player_score = 0
ai_score = 0
draw_score = 0

# ======= CHANGE THESE PATHS TO YOUR LOCAL VIDEO FILES =======
PLAYER_WIN_VIDEO = r"C:\Users\Akilan\OneDrive\Desktop\temp\Soorarai pottru climax scene - Cinemas (720p, h264).mp4"
AI_WIN_VIDEO = r"C:\Users\Akilan\OneDrive\Desktop\temp\gp muthu nakku dialogue - SIVA (480p, h264).mp4"
DRAW_VIDEO = r"C:\Users\Akilan\OneDrive\Desktop\temp\neeum nanum vera illa da rendu peru loosu pu.... da  natpu status 🥰 - TN PAIN GAMEING FF (720p, h264).mp4"
# ============================================================

def play_video(file_path):
    if os.path.exists(file_path):
        subprocess.Popen([file_path], shell=True)  # Opens with default player
    else:
        print(f"Video file not found: {file_path}")

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    return " " not in board

def get_valid_moves(board):
    return [i for i in range(9) if board[i] == " "]

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_valid_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_valid_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in get_valid_moves(board):
        board[i] = "O"
        score = minimax(board, 0, False)
        board[i] = " "
        if score > best_score:
            best_score = score
            move = i
    return move

def button_click(index):
    global player_score, ai_score, draw_score

    if board[index] == " " and not is_winner(board, "X") and not is_winner(board, "O"):
        board[index] = "X"
        buttons[index].config(text="X", state="disabled")
        
        if is_winner(board, "X"):
            player_score += 1
            status_label.config(text="You win!")
            update_score()
            disable_all_buttons()
            play_video(PLAYER_WIN_VIDEO)
            return
        elif is_board_full(board):
            draw_score += 1
            status_label.config(text="Draw!")
            update_score()
            play_video(DRAW_VIDEO)
            return
        
        ai_index = best_move(board)
        board[ai_index] = "O"
        buttons[ai_index].config(text="O", state="disabled")
        
        if is_winner(board, "O"):
            ai_score += 1
            status_label.config(text="AI wins!")
            update_score()
            disable_all_buttons()
            play_video(AI_WIN_VIDEO)
        elif is_board_full(board):
            draw_score += 1
            status_label.config(text="Draw!")
            update_score()
            play_video(DRAW_VIDEO)

def disable_all_buttons():
    for btn in buttons:
        btn.config(state="disabled")

def reset_game():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ", state="normal")
    status_label.config(text="You are X, AI is O")

def update_score():
    score_label.config(text=f"Score - You: {player_score}  AI: {ai_score}  Draws: {draw_score}")

# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe (Minimax AI)")

buttons = []
for i in range(9):
    btn = tk.Button(root, text=" ", font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

status_label = tk.Label(root, text="You are X, AI is O", font=('Arial', 14))
status_label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text="Score - You: 0  AI: 0  Draws: 0", font=('Arial', 12))
score_label.grid(row=4, column=0, columnspan=3)

reset_button = tk.Button(root, text="Restart Game", font=('Arial', 12), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3)

root.mainloop()
