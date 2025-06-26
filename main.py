# Minesweeper website: https://minesweeperonline.com/#200

from readBoard import make_board
from gamemodes import win_percentage, first_win
import time

def select_device():
    while True:
        print("\nSelect your device:\n 1. PC\n 2. Laptop\n")
        choice = input("Enter 1 or 2:\n").strip()

        if choice == '1':
            return "pc"
        elif choice == '2':
            return "laptop"
        else:
            print("\nInvalid choice. Try again.")

def select_game_mode():
    while True: 
        print("\nSelect game difficulty:\n 1. Beginner\n 2. Intermediate\n 3. Expert\n 4. Insane\n")
        choice = input("Enter 1-4:\n").strip()

        if choice == '1':
            return 'beginner'
        elif choice == '2':
            return 'intermediate'
        elif choice == '3':
            return 'expert'
        elif choice == '4':
            return 'insane'
        else:
            print("\nInvalid choice. Try again.")

def select_bot_type():
    while True:
        print("\nSelect bot type:\n 1. Win Percentage\n 2. First Win\n")
        choice = input("Enter 1 or 2:\n").strip()

        if choice == '1':
            return '1'
        elif choice == '2':
            return '2'
        else: 
            print("\nInvalid choice. Try again.")


if __name__ == "__main__":
    device = select_device()
    gamemode = select_game_mode()
    type = select_bot_type()

    if type == '1':
        num_games = int(input("\nEnter number of games: "))

    regions = {
        "pc": {
            "beginner": (1056, 254, 287, 287),
            "intermediate": (1020, 254, 511, 511),
            "expert": (796, 254, 959, 511),
            "insane": (477, 202, 1583, 1199) # Zoom 100% 75x99, TILE = 15
        },
        "laptop": {
            "beginner": (),
            "intermediate": (),
            "expert": (),
            "insane": ()
        }
    }

    region = regions.get(device, {}).get(gamemode)

    print("\nStarting in:")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    # board = make_board(region)
    # for row in board:
    #         print(" ".join(row))

    if type == '1':
        win_percentage(region, num_games)
    elif type == '2':
        first_win(region)