from readBoard import make_board
from logic import next_move, click_random_corner

def solve_board(region):
    origin = region [:2]
    flagged_tiles = set()

    click_random_corner(region) # Random corner to start

    while True: 
        board = make_board(region)           
        moved = next_move(board, origin, flagged_tiles)

        if moved: 
            continue

        print("\nFinal board state:")
        for row in board:
            print(" ".join(row))

        break
