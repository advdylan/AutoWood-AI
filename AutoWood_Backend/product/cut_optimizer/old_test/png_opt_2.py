import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data
from AutoWood_Backend.cut_optimizer.helpers import set_ticks
from AutoWood_Backend.product.cut_optimizer.old_test.or_tools_mbo import pack_pieces_on_boards
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from ortools.linear_solver import pywraplp
import numpy as np


X = 3000
Y = 2000
SAW = 3.2

X_IN = X / 25.4
Y_IN = Y / 25.4

id = 62


output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{id}"
optc_name = f"optc_{id}.png"
file_path = os.path.join(output_dir, optc_name)

def generate_board(output_dir, optc_name,X,Y):

    file_path = os.path.join(output_dir, optc_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    project_data = get_data(id)
    formats = convert_elements(project_data)

    fig, ax = plt.subplots(figsize=(12.8, 7.2))

    
    
    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_xlabel('Długość płyty')
    ax.set_ylabel('Wysokość płyty')
    ax.set_title(f"Rozkrój płyty o wymiarze {X} x {Y}")
    x_ticks = set_ticks(X, 130)
    y_ticks = set_ticks(Y, 100)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    i = 0
    j = 0
    start_position_x = 0
    start_position_y = 0

    define_starting_position(formats, ax)
       
    plt.savefig(file_path, format='png', dpi=150)


def convert_elements(project_data):

    elements = project_data["elements"]

    formats = []

    for element in elements:
        length = element['element']['dimX']
        width = element['element']['dimY']
        #thickness = element['element']['dimZ'] wyłączyłęś chwilowo grubośći
        quantity = element['quantity']
        starting_x = 0
        starting_y = 0

        row = [length, width, starting_x, starting_y]

        for _ in range(int(quantity)):
            formats.append(row)

    return formats

   
def generate_rectangle(start_position_x, start_position_y, width, height, ax):
  
    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height, edgecolor='black', facecolor='#d3e2dc', antialiased=True, linewidth=None)
    ax.add_patch(rect)

    text_x = start_position_x + width / 2
    text_y = start_position_y + height / 2
    ax.text(text_x, text_y, f'{width} x {height}', ha='center', va='center', fontsize=10, color='black')


def calculate_rows(formats):
    i=0
    j=0
    lengths = []
    heights = []
    rows = []
    free_x = 0
    free_y = 0
    for format in formats:
        #print(f"Format numer {j}")       
        print(f"X: {format[i]}, Y: {format[i+1]}")
        lengths.append(format[i])
        heights.append(format[i+1])
        j+=1

    lengths.sort()
    heights.sort(reverse=True)
    return lengths,heights
 
def create_virtual_row(height, X, Y):
    board = (X, height)
    return board

def control_board_capacity(format, board):
    
    capacity_left = (board[0] - format[0], board[1])
    positive = all(num >= 0 for num in capacity_left)
    if positive:
        #print("Wchodzi idelnie mój Panie")
        return capacity_left, True
    else:
        #print("Masz za dużego Panie")
        return capacity_left,False





def define_starting_position(formats, ax):
    board = (X, Y)  # Board dimensions
    lengths, heights = calculate_rows(formats)
    
    virtual_row = create_virtual_row(heights[0], X, Y)  # Virtual row based on the first piece's height
    virtual_rows = [virtual_row]
    
    start_position_x = 0  # Starting X position
    start_position_y = 0  # Starting Y position
    current_row_height = heights[0]  # Set initial row height based on the first piece

    while formats:
        format = formats.pop(0)
        width = format[0]
        height = format[1]

        # Check if the piece fits horizontally in the current row
        if start_position_x + width <= X:
            # Piece fits in the current row, place it
            format[2] = start_position_x  # Update format start X position
            format[3] = start_position_y  # Update format start Y position

            # Generate the rectangle at the current position
            generate_rectangle(start_position_x, start_position_y, width, height, ax)

            # Move start_position_x by the width of the placed piece + saw thickness
            start_position_x += width + SAW
        else:
            # Piece doesn't fit in the current row, move to the next row
            start_position_x = 0  # Reset X position for the new row
            start_position_y += current_row_height + SAW  # Move Y position down by the height of the current row

            # Update the row height to the new piece's height
            current_row_height = height

            # Now check if the piece fits in the new row
            if start_position_x + width <= X:
                format[2] = start_position_x
                format[3] = start_position_y

                generate_rectangle(start_position_x, start_position_y, width, height, ax)

                start_position_x += width + SAW  # Update start_position_x for the next piece in the row
            else:
                # In case the piece itself exceeds the width of the board (an edge case to handle)
                print(f"Piece {width}x{height} is too large for the board width!")
                # Handle this situation (either warn or adjust)




        
    #print(f"first loop end, virtual row: {virtual_rows}")






    

    
        

  
generate_board(output_dir, optc_name, X, Y)




    