from readBoard import make_board
from logic import next_move, click_random_corner

def solve_board(region):
    origin = region [:2]
    click_random_corner(region) # Random corner to start

    while True: 
        board = make_board(region)           
        moved = next_move(board, origin)

        if moved: 
            continue

        break
