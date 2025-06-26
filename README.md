# 🧠 Minesweeper Solver

> ⚠️ **DISCLAIMER:**  
> This project is for **educational use only**.  
> Do **not** use this tool to gain a competitive advantage in online leaderboards.  
> The author is **not responsible** for how this code is used.

## 📖 Overview

This is a Python-based bot that plays Minesweeper automatically by:

- Reading the screen
- Classifying tiles using image matching
- Applying logical deduction to safely click or flag tiles

It uses basic inference logic similar to how a human would play Minesweeper.
> 🔄 **Note**: This bot currently uses basic logic rules only. I plan to add support for more advanced solving techniques and common Minesweeper patterns as I learn them. I'm still new to solving Minesweeper, so this project is part of my learning process.
---

## 🔧 How It Works

1. **Read the Board**:  
   The screen is captured using `pyautogui.screenshot()`. The image is then divided into grid tiles (typically 24×24 pixels) and each tile is matched against template images using OpenCV.

2. **Logic Rules Applied**:
   - If the number of hidden + flagged tiles equals the number on a tile → all hidden tiles must be bombs.
   - If the number of flagged tiles equals the number on a tile → all other hidden tiles must be safe and are clicked.

3. **Automation**:  
   The bot uses `pyautogui.moveTo()` and `click()` to interact with the game.

---

## 🖼️ How to Get Game Dimensions

To use this solver, you need to know the screen coordinates of the game board.

### Steps:

1. Open the Minesweeper game in your browser.
2. Make sure the board is fully visible and doesn't move.
3. Take a screenshot (`PrtScn` key or Windows + Shift + S).
4. Open the screenshot in **MS Paint**.
5. Hover your mouse over the **top-left corner** of the game board.  
   Note the pixel coordinates shown in the bottom bar — this is `(x, y)`.
6. Then move your mouse to the **bottom-right corner** of the board.  
   Subtract the top-left values to get `width` and `height`.

   For example:
   ```
   Top-left: (1000, 300)
   Bottom-right: (1400, 700)
   → width = 1400 - 1000 = 400
   → height = 700 - 300 = 400
   ```

7. Your region is:  
   ```python
   (1000, 300, 400, 400)  # (x, y, w, h)
   ```

8. Insert this into the dictionary in `main.py` under your desired device and difficulty:

   ```python
   regions = {
       "pc": {
           "beginner": (1000, 300, 400, 400),
           "intermediate": (...),
           ...
       },
       ...
   }
   ```

---

## ✅ Requirements

Install the necessary packages:

```bash
pip install pyautogui opencv-python numpy pillow
```

---

## 🚀 Running the Bot

1. Launch the Minesweeper game in your browser.
2. Make sure the game board matches the dimensions you configured.
3. Run the bot:
   ```bash
   python main.py
   ```
4. Choose your device and difficulty.
5. Watch it solve the board automatically!
