from readBoard import make_board
from basicLogic import next_move
from bestGuess import best_guess
from functions import get_corners, click_random_corner, check_win

def solve_board(region, win_region):
    origin = region [:2]
    flagged_tiles = set()

    corners = get_corners(region)
    click_random_corner(corners) # Random corner to start

    while True: 
        board = make_board(region)

        if check_win(win_region):
            return True

        # Check if bomb has been clicked either D for bomb we clicked or X that is revealed bomb after loss
        check = [tile for row in board for tile in row]
        if 'D' in check or 'X' in check: 
            return False
               
        # Choose a next move if there is a valid move do it and restart loop
        moved = next_move(board, origin, flagged_tiles)
        if moved: 
            continue

        # Check corners to see if they are clicked, if not click it and restart loop
        # print("corner")
        # if corners:
        #     click_random_corner(corners)
        #     continue
        
        # Make the best guess
        print("Guessing...")
        guess = best_guess(board, origin)
        if guess: 
            continue
        
