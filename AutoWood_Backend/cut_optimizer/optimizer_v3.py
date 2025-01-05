import os
import time
import sys
import django
from django.conf import settings
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np




SAW = 3.2


class Board:

    def __init__(self, width, height, start_x, start_y):
        self.width = width  # Width of the row
        self.height = height  # Height of the row
        self.start_x = start_x  # Starting x position
        self.start_y = start_y  # Starting y position
        self.occupied = False # is the Board occupied ?

    def can_fit(self, format_width, format_height):
        return self.width >= format_width and self.height >= format_height
    
    def split(self, format_width, format_height, saw_thickness):

        remaining_width = self.width - format_width - saw_thickness
        remaining_height = self.height - format_height - saw_thickness

        new_boards = []

        if remaining_width > 0:
            new_boards.append(Board(remaining_width, self.height, self.start_x + format_width + saw_thickness, self.start_y ))

        if remaining_height > 0:
            new_boards.append(Board(self.width, remaining_height, self.start_x, self.start_y + format_height + saw_thickness))

        self.width = format_width
        self.height = format_height
        self.occupied = True
        return new_boards
    

class BoardManager:

    def __init__(self, initial_width, initial_height):
        self.boards = [Board(initial_width, initial_height)]
    
    def place_format(self, format_width, format_height):
        for board in self.boards:
            if board.can_fit(format_width, format_height) and not board.occupied:
                new_boards = board.split(format_width, format_height, SAW)
                self.boards.extend(new_boards)
                return True
        return False
        
        
    def merge_gaps(self):
        pass

class Visualizer:

    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.ax.set_xlim(0, board_width)
        self.ax.set_ylim(0, board_height)
        self.ax.set_aspect('equal', adjustable='box')
        self.ax.invert_yaxis()  # Invert Y-axis for a top-down view
        self.ax.set_title("Board Visualization")
        self.ax.set_xlabel("Width (X)")
        self.ax.set_ylabel("Height (Y)")

    def draw_board(self, boards):
        """Draw all boards (formats and gaps) on the main canvas."""
        for board in boards:
            color = "red" if board.occupied else "lightgray"
            self.draw_rectangle(
                board.start_x, board.start_y, board.width, board.height, color
            )

    def draw_rectangle(self, start_x, start_y, width, height, color="lightgray"):
        """Draw a single rectangle on the canvas."""
        rect = patches.Rectangle(
            (start_x, start_y), width, height, linewidth=1, edgecolor="black", facecolor=color
        )
        self.ax.add_patch(rect)

    def annotate_rectangle(self, start_x, start_y, width, height, label):
        """Annotate a rectangle with text (e.g., dimensions)."""
        center_x = start_x + width / 2
        center_y = start_y + height / 2
        self.ax.text(
            center_x, center_y, label,
            ha="center", va="center", fontsize=8, color="black", bbox=dict(facecolor="white", edgecolor="none", alpha=0.7)
        )

    def show(self):
        """Display the visualization."""
        plt.show()

    def save(self, filepath):
        """Save the visualization to a file."""
        self.fig.savefig(filepath)


def main():

    board_width = 3000
    board_height = 1500
    visualizer = Visualizer(board_width, board_height)

    # Example boards (replace with your actual Board objects)
    boards = [
        Board(1000, 500, 0, 0),  # Format placed at the bottom-left
        Board(2000, 500, 1000, 0),  # Format placed to the right of the first
        Board(3000, 1000, 0, 500, occupied=False),  # Free space above the first two formats
    ]

    # Draw all boards (occupied and free spaces)
    visualizer.draw_board(boards)

    # Optionally, annotate formats with dimensions or labels
    for board in boards:
        visualizer.annotate_rectangle(
            board.start_x, board.start_y, board.width, board.height,
            f"{board.width}x{board.height}"
        )

    # Show the visualization
    visualizer.show()

main()