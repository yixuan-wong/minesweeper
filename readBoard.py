import pyautogui
import os
import cv2
import numpy as np
from PIL import Image 

TILE_SIZE = 32
TEMPLATE_DIR = "tiles"

def load_templates():
    return {
        name.split('.')[0]: cv2.imread(os.path.join(TEMPLATE_DIR, name), cv2.IMREAD_COLOR)
        for name in os.listdir(TEMPLATE_DIR)
    }

def classify_tiles(tile_img, templates):
    best_match = '-'
    best_score = 0

    for label, template in templates.items():
        res = cv2.matchTemplate(tile_img, template, cv2.TM_CCOEFF_NORMED)
        score = res.max()

        if score > best_score:
            best_score, best_match = score, label

    return best_match

def make_board(region):
    x, y, w, h = region
    img = np.array(pyautogui.screenshot(region=(x, y, w, h)))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    rows = round(h / TILE_SIZE)
    cols = round(w / TILE_SIZE)

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