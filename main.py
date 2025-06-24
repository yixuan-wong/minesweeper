from read import get_region, make_board, TILE_SIZE

if __name__ == "__main__":
    board_coords = get_region()

    classified_board_data = make_board(board_coords)

    for r_idx, row in enumerate(classified_board_data):
        print(f"Row{r_idx:2d}: {' '.join(f'{str(tile):<2}' for tile in row)}")


