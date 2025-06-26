from readBoard import TILE_SIZE
from functions import click_tile, flag_tile, get_neighbors

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
