import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data
from product.cut_optimizer.helpers import set_ticks
from or_tools_mbo import pack_pieces_on_boards
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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
    virtual_rows = []  # List to hold all virtual rows
    start_position_y = 0  # Starting Y position for the first row

    print(formats)

    while formats:
        format = formats.pop(0)
        width = format[0]
        height = format[1]

        # Try to place the piece in an existing row
        placed = False
        for row in virtual_rows:
            remaining_width, row_height, row_start_y = row
            if width <= remaining_width:
                # The piece fits in this row
                start_position_x = X - remaining_width  # Calculate the X position
                format[2] = start_position_x  # Update format start X position
                format[3] = row_start_y  # Set Y position based on the row's start Y position
                
                # Generate the rectangle at the current position
                generate_rectangle(start_position_x, row_start_y, width, height, ax)

                # Update the remaining width for the row
                row[0] -= width + SAW
                placed = True
                break  # Exit the loop once the piece is placed

        if not placed:
            # If the piece doesn't fit in any existing row, create a new row
            if start_position_y + height <= Y:  # Check if we still have vertical space
                start_position_x = 0  # New row starts at X=0
                format[2] = start_position_x
                format[3] = start_position_y

                # Generate the rectangle at the new position
                generate_rectangle(start_position_x, start_position_y, width, height, ax)

                # Add a new virtual row with the remaining space
                new_row = [X - (width + SAW), height, start_position_y]
                virtual_rows.append(new_row)

                # Update the Y position for the next row
                start_position_y += height + SAW
            else:
                print(f"No space left for piece {width}x{height}!")

        # Re-check earlier rows for remaining space after placing in a new row
        for row in virtual_rows:
            remaining_width, row_height, row_start_y = row
            if remaining_width > 0:
                print(f"Remaining space in row starting at Y={row_start_y}: {remaining_width} mm")






    

    
        

  
generate_board(output_dir, optc_name, X, Y)




    