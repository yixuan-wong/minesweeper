from readBoard import TILE_SIZE

import pyautogui
import cv2
import numpy as np
import random

def click_tile(x, y): 
    pyautogui.click(x, y, duration=0)

def flag_tile(x, y):
    pyautogui.click(x, y, duration=0, button='right')

def get_corners(region):
    origin_x, origin_y = region[:2]
    width, height = region[2], region[3]

    corners = [
        (origin_x + TILE_SIZE // 2, origin_y + TILE_SIZE // 2), # top left
        (origin_x + width - TILE_SIZE // 2, origin_y + TILE_SIZE // 2), # top right
        (origin_x + TILE_SIZE // 2, origin_y + height - TILE_SIZE // 2), # bottom left
        (origin_x + width - TILE_SIZE // 2, origin_y + height - TILE_SIZE // 2) # bottom right
    ]

    return corners

def click_random_corner(corners): 
    (x, y) = random.choice(corners)
    click_tile(x, y)
    corners.remove((x, y))

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

def check_win():
    regions = [
        (1174, 176, 51, 51), # beginner
        (1250, 176, 51, 51),
        (1055, 82, 449, 199)
    ]

    template_paths = ["tiles/win.png", "tiles/win2.png"]
    threshold = 0.95

    for (x, y, w, h), template_path in zip(regions, template_paths):
        img = np.array(pyautogui.screenshot(region=(x, y, w, h)))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        template = cv2.imread(template_path)
        res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

        if np.any(res >= threshold):
            return True
    
    return False