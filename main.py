from read import make_board, TILE_SIZE

if __name__ == "__main__":
    INTERMEDIATE_REGION = (991, 340, 383, 383)

    classified_board_data = make_board(INTERMEDIATE_REGION)

    for r_idx, row in enumerate(classified_board_data):
        print(f"Row{r_idx:2d}: {' '.join(f'{str(tile):<2}' for tile in row)}")