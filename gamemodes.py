from solveBoard import solve_board
import pyautogui
import numpy as np
import time

def restart_game():
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(1)

def win_percentage(region, win_region, num_games):
    wins = 0
    losses = 0

    for i in range(num_games):
        print(f"--- Game {i + 1} ---")
        result = solve_board(region, win_region)

        if result:
            wins += 1
            print(f"Game {i + 1} won.\n")

        else: 
            losses += 1
            print(f"Game {i + 1} lost.\n")

        restart_game()

    win_percent = (wins / num_games * 100) if wins > 0 else 0
    print(f"Games played: {num_games}\n Wins: {wins}\n Losses: {losses}\n Win Percentage: {win_percent}%")

def first_win(region, win_region):
    game_num = 1

    while True:
        print(f"--- Game {game_num} ---")
        restart_game()
        win = solve_board(region, win_region)

        if win: 
            print(f"First win achieved after {game_num} games(s)!\n")
            return 
        
        else:
            print("Retrying...\n")
            game_num += 1