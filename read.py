import pyautogui
import os
import cv2
import numpy as np
from PIL import Image 

TILE_SIZE = 23
TEMPLATE_DIR = "tiles"

def get_region():
    print("Hover over top left corner of the board and press Enter.")
    input()
    top_left = pyautogui.position()

    print("Hover over bottom right corner of the board and press Enter.")
    input()
    bottom_right = pyautogui.position()

    x, y = top_left.x, top_left.y
    w = bottom_right.x - top_left.x
    h = bottom_right.y - top_left.y

    return (x, y, w, h)

def load_templates():
    return {
        name.split('.')[0]: cv2.imread(os.path.join(TEMPLATE_DIR, name), 0)
        for name in os.listdir(TEMPLATE_DIR)
    }

def classify_tiles(tile_img, templates):
    tile_gray = cv2.cvtColor(tile_img, cv2.COLOR_BGR2GRAY)
    best_match = '-'
    best_score = 0.6

    for label, template in templates.items():
        res = cv2.matchTemplate(tile_gray, template, cv2.TM_CCOEFF_NORMED)
        score = res.max()

        if score > best_score:
            best_score, best_match = score, label

    return best_match

def make_board(region):
    x, y, w, h = region
    img = np.array(pyautogui.screenshot(region=(x, y, w, h)))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    rows = h // TILE_SIZE
    cols = w // TILE_SIZE

    img = img[:rows * TILE_SIZE, :cols * TILE_SIZE]

    templates = load_templates()
    board = []

    for r in range(rows): 
        row = []

        for c in range(cols):
            tile = img[r * TILE_SIZE: (r + 1) * TILE_SIZE, c * TILE_SIZE: (c + 1) * TILE_SIZE]
            label = classify_tiles(tile, templates)
            row.append(label)

        board.append(row)

    return board