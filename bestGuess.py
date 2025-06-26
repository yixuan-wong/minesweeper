from readBoard import TILE_SIZE
from functions import click_tile, get_neighbors, is_unopened, is_revealed, get_mine_count, get_unopened_count

def best_guess(board, origin):
    origin_x, origin_y = origin

    guesses = []

    for r in range(len(board)):
        for c in range(len(board[0])):
            if is_unopened(board[r][c]):
                adjacent = []

                for nr, nc in get_neighbors(board, r, c):
                    if is_revealed(board[nr][nc]):
                        adjacent.append((nr, nc))

                if adjacent:
                    curr_score = 0
                    num_sources = 0
                    
                    for num_r, num_c in adjacent:
                        num_val = int(board[num_r][num_c])
                        num_flagged = get_mine_count(board, num_r, num_c)
                        num_unopened = get_unopened_count(board, num_r, num_c)

                        mines_left = num_val - num_flagged

                        if num_unopened > 0: 
                            curr_score += (mines_left / num_unopened)
                            num_sources += 1
                        
                    if num_sources > 0: 
                        avg_score = curr_score / num_sources
                        guesses.append((avg_score, r, c))

    if guesses:
        guesses.sort(key = lambda x: x[0])
        best_guess_r, best_guess_c = guesses[0][1], guesses[0][2]

        click_tile(origin_x + best_guess_c * TILE_SIZE + TILE_SIZE // 2, origin_y + best_guess_r * TILE_SIZE + TILE_SIZE // 2)

        return True
    
    return False

