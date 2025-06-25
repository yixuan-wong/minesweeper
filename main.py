# Minesweeper website: https://minesweeper.online/

from solveBoard import solve_board
from readBoard import make_board
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

if __name__ == "__main__":
    device = select_device()
    gamemode = select_game_mode()

    regions = {
        "pc": {
            "beginner": (991, 340, 215, 215),
            "intermediate": (991, 340, 383, 383),
            "expert": (991, 340, 719, 383),
            "insane": (909, 215, 1650, 799) # Zoom 33% 100x100
        },
        "laptop": {
            "beginner": (),
            "intermediate": (),
            "expert": (),
            "insane": ()
        }
    }

    region = regions.get(device, {}).get(gamemode)

    time.sleep(3)

    # board = make_board(region)
    # for row in board:
    #         print(" ".join(row))

    solve_board(region)