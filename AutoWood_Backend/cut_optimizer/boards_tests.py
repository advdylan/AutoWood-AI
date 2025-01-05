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

from board_based_optimizer_copy import Board, generate_board, place_elements, format_fit_check, add_format,set_ticks
fig, ax = plt.subplots(figsize=(12.8, 7.2))

#piszesz funkcje ktora wykryje kolizje z rzedem po prawej

SAW = 3.2

def main():
    
    initial_board_x = 2500
    initial_board_y = 700
    
    output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/cut_optimizer/optimized_cuts/"
    id = 135
    optc_name = f"optimized_cut_{id}.png"
    file_path = os.path.join(output_dir, optc_name)

    ax.set_xlim(0, initial_board_x)
    ax.set_ylim(0, initial_board_y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title("Rozkroje")
    x_ticks = set_ticks(initial_board_x, 100)
    y_ticks = set_ticks(initial_board_y, 100)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)


    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    

    board_1 = Board(838.8, 340.4, 1661.2,0)
    board_2 = Board(2500, 359.59, 0 , 340.4)

    

    boards = []
    boards.append(board_1)
    boards.append(board_2)

    scan_boards(boards)
    plt.savefig(file_path, format='png', dpi=150)

    format = [1658, 168]

    for board in boards:

        width, height = format[0],format[1]
        if format_fit_check(board, width,height) and board.occupied == False:
                

                add_format(board, width,height)
                cut_next_board(boards,board, width,height, initial_board_x, initial_board_y)
                scan_boards(boards)
                plt.savefig(file_path, format='png', dpi=150)
    

    scan_boards(boards)
    plt.savefig(file_path, format='png', dpi=150)


def check_boards_presence(board, boards, initial_board_x, initial_board_y):


    for board_to_check in boards:
        pass






def cut_next_board(boards,board,format_width, format_height,initial_board_x, initial_board_y):

    # Return the remaining size of the board in the same Y
    remaining_Y = board.Y - format_height - SAW
    new_board_start_y = board.start_y + format_height + SAW 
    remaining_X = board.X - format_width - SAW
    new_board_start_x = board.start_x + format_width + SAW
    #print(f"remaining_y: {remaining_Y},new_board_start_y: {new_board_start_y}\nremaining_X: {remaining_X},new_board_start_x: {new_board_start_x}")

    # CUT

    board.Y = format_height

    # Created the initual_board_x variable for cutting boards in different places than start_x = 0
    #initial_board_x = board.X

    board.X = format_width

    # Create new board in the same ROW

    
    
    if (remaining_X + board.start_x) < initial_board_x:
        
        new_board_same_row = Board(remaining_X, board.Y, new_board_start_x, board.start_y)
        boards.append(new_board_same_row )      
    # Create new board above the row


    if remaining_Y > 0 or remaining_Y < initial_board_y and remaining_Y > 40:

        #maybe create a function that detects the board in the same line? 

        if board.start_x > 0:
         
            new_board_higher_row = Board(remaining_X, remaining_Y, board.start_x, new_board_start_y)
            boards.append(new_board_higher_row)

            
        else:

            new_board_higher_row = Board(initial_board_x, remaining_Y, board.start_x, new_board_start_y)
            boards.append(new_board_higher_row)     

def draw_gaps(board):
    """
    Draws red boundary lines for all virtual rows on the board.
    """
 
        # Draw a red rectangle to represent the virtual row boundaries
    if board.occupied == False:
        edgecolor = 'green'
    else:
        edgecolor = 'red'
    rect = patches.Rectangle(
        xy=(board.start_x, board.start_y), 
        width=board.X, 
        height=board.Y, 
        edgecolor=edgecolor , 
        facecolor='none', 
        linestyle='--', 
        linewidth=1
    )
    ax.add_patch(rect)
    #print(f"Drawing board boundary: Start X={board.start_x}, Y={board.start_y}, Width={board.X}, Height={board.Y}")

def scan_boards(boards):
    #function to scan free spaces on the board and mark free areas on the board for debug purposes


    if isinstance(boards,Board): # Single board case
        draw_gaps(boards)
    elif isinstance(boards, list):
        for board in boards:
            if isinstance(board, Board):
                draw_gaps(board)
            else:
                raise ValueError(f"Expected a Board got {type(board).__name__}")
    else:
        raise TypeError(f"Invalid input type {type(boards).__name__}")
main()




