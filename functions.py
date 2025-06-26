from readBoard import TILE_SIZE
import pyautogui
import random

def click_tile(x, y): 
    # pyautogui.moveTo(x, y)
    pyautogui.click(x, y)

def flag_tile(x, y):
    # pyautogui.moveTo(x, y)
    pyautogui.click(x, y, button='right')

def click_random_corner(region): 
    origin_x, origin_y = region[:2]
    width, height = region[2], region[3]

    corners = [
        (origin_x + TILE_SIZE // 2, origin_y + TILE_SIZE // 2), # top left
        (origin_x + width - TILE_SIZE // 2, origin_y + TILE_SIZE // 2), # top right
        (origin_x + TILE_SIZE // 2, origin_y + height - TILE_SIZE // 2), # bottom left
        (origin_x + width - TILE_SIZE // 2, origin_y + height - TILE_SIZE // 2) # bottom right
    ]

    for (x, y) in random.sample(corners, 1):
        click_tile(x, y)

def get_neighbors(board, r, c):
    neighbors = []
    for sr in [-1, 0, 1]: # surrounding rows
        for sc in [-1, 0, 1]: # surrounding columns
            if sr == 0 and sc == 0: # skip self
                continue
            nr, nc = r + sr, c + sc # neighbor row and neighbor column

            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                neighbors.append((nr, nc))
        
    return neighbors

def is_unopened(tile):
    return tile == '-'

def is_flagged(tile): 
    return tile == 'F'

def is_revealed(tile): 
    return tile.isdigit()

def get_mine_count(board, r, c):
    mineCount = 0

    for nr, nc in get_neighbors(board, r, c):
        if is_flagged(board[nr][nc]):
            mineCount += 1

    return mineCount

def get_unopened_count(board, r, c):
    unopenedCount = 0
    
    for nr, nc in get_neighbors(board, r, c):
        if is_unopened(board[nr][nc]):
            unopenedCount += 1

    return unopenedCount