"""
## Problem Statement

Implement an 'eraser' on a canvas.
The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
We then create an eraser rectangle which, when dragged around the canvas, sets all of the
rectangles it is in contact with to white.
"""

import tkinter as tk

class EraserCanvas:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        # Create grid of blue rectangles
        self.cells = []
        for i in range(0, 400, 20):
            row = []
            for j in range(0, 400, 20):
                rect = self.canvas.create_rectangle(i, j, i+20, j+20, fill='blue')
                row.append(rect)
            self.cells.append(row)

        # Bind mouse events
        self.canvas.bind('<B1-Motion>', self.erase)

    def erase(self, event):
        # Get mouse coordinates
        x, y = event.x, event.y

        # Find cells that intersect with eraser (20x20 pixels around mouse)
        for i in range(max(0, x//20-1), min(20, x//20+2)):
            for j in range(max(0, y//20-1), min(20, y//20+2)):
                if 0 <= i < 20 and 0 <= j < 20:
                    self.canvas.itemconfig(self.cells[i][j], fill='white')

def main():
    root = tk.Tk()
    root.title("Eraser Canvas")
    app = EraserCanvas(root)
    root.mainloop()

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
