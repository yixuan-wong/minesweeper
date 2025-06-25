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

def next_move(board, origin, flagged_tiles):
    flagged_any = True

    while flagged_any: 
        flagged_any = False 
        for r in range(len(board)):
            for c in range(len(board[0])):
                tile = board[r][c]
                if not tile.isdigit():
                    continue
            
                num = int(tile)
                neighbors = get_neighbors(board, r, c)
                hidden = [(nr, nc) for nr, nc in neighbors if board[nr][nc] == '-']
                flagged = [(nr, nc) for nr, nc in neighbors if board[nr][nc] == 'F']

                if num == len(hidden) + len(flagged) and hidden: 
                    for nr, nc in hidden: 
                        if (nr, nc) not in flagged_tiles:
                            cx = origin[0] + nc * TILE_SIZE + TILE_SIZE // 2
                            cy = origin[1] + nr * TILE_SIZE + TILE_SIZE // 2
                            flag_tile(cx, cy)
                            flagged_tiles.add((nr, nc))
                            board[nr][nc] = 'F'
                            flagged_any = True
                    
        if flagged_any: 
            continue

    for r in range(len(board)):
        for c in range(len(board[0])):
            tile = board[r][c]
            if not tile.isdigit(): 
                continue
            
            num = int(tile)
            neighbors = get_neighbors(board, r, c)
            hidden = [(nr, nc) for nr, nc in neighbors if board[nr][nc] == '-']
            flagged = [(nr, nc) for nr, nc in neighbors if board[nr][nc] == 'F']

            if num == len(flagged) and hidden: 
                for (nr, nc) in hidden: 
                    cx = origin[0] + nc * TILE_SIZE + TILE_SIZE // 2
                    cy = origin[1] + nr * TILE_SIZE + TILE_SIZE // 2
                    click_tile(cx, cy)

                    return True

    return False
