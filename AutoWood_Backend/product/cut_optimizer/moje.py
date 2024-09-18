import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data
from product.cut_optimizer.helpers import set_ticks
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
fig, ax = plt.subplots(figsize=(12.8, 7.2))


class VirtualRow:

    def __init__(self, X, Y, x, y):
        self.X = X  # Width of the row
        self.Y = Y  # Height of the row
        self.start_x = x  # Starting x position
        self.start_y = y  # Starting y position
        self.formats = []  # List of placed formats

    def add_format(self, format_width, format_height):
        # If first element in the row
        if len(self.formats) == 0:
            if format_width + SAW > self.X:
                print(f"Not enough space in row. Width left: {self.X}, format width: {format_width}")
                return False
            
            self.X -= format_width + SAW
            self.formats.append([format_width, format_height, self.start_x])
            print(f"Placing first format in row: start_x={self.start_x}")
            generate_rectangle(self.start_x, self.start_y, format_width, format_height, ax)
            self.start_x += format_width + SAW
            return True

        # If the format fits in both dimensions
        elif format_width <= self.X and format_height <= self.Y:
            self.X -= format_width + SAW
            self.formats.append([format_width, format_height, self.start_x])
            print(f"Placing format in row: start_x={self.start_x}")
            generate_rectangle(self.start_x, self.start_y, format_width, format_height, ax)
            self.start_x += format_width + SAW

            # If the format does not take the entire height, create a new row for the remaining height
            if format_height < self.Y:
                remaining_height = self.Y - format_height
                new_row = VirtualRow(self.X, remaining_height, self.start_x - format_width - SAW , self.start_y + format_height + SAW)
                print(f"Creating new row for remaining height: {remaining_height}")
                return new_row  # Return the new row to append to vrs in place_elements()

            return True

        # If the format doesn't fit
        else:
            print("Not enough space in this row. Proceeding to the next one.")
            return False

    def __str__(self):
        return f"VirtualRow X: {self.X}, Y: {self.Y}, start_x: {self.start_x}, start_y: {self.start_y}, formats: {self.formats}"
    
       

def generate_board(X,Y):

    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title("Rozkroje")
    x_ticks = set_ticks(X, 120)
    y_ticks = set_ticks(Y, 100)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    #project_data = get_data(id)
    #formats = convert_elements(project_data)
    #
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    formats = [[1600, 500], [500, 500], [1000,500],[200,500], [200,95],[200,95], [200,95],[200,95], [200,95],[200,95], [200,95]]
   

    place_elements(formats)
    #print(formats)

    

    plt.savefig(file_path, format='png', dpi=150)

    




def convert_elements(project_data):

    elements = project_data["elements"]

    formats = []


    for element in elements:
        length = element['element']['dimX']
        width = element['element']['dimY']
        quantity = element['quantity']
        starting_x = 0
        starting_y = 0

        row = [length, width, starting_x, starting_y]

        for _ in range(int(quantity)):
            formats.append(row)

    formats.sort(reverse=True)
    return formats

def generate_rectangle(start_position_x, start_position_y, width, height, ax):

    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height, edgecolor='black', facecolor='#d3e2dc', antialiased=True, linewidth=None)
    ax.add_patch(rect)
    print(f"Placing rectangle in X:{start_position_x},Y:{start_position_y} format size:  X: {width} Y:{height}" )

    text_x = start_position_x + width / 2
    text_y = start_position_y + height / 2
    ax.text(text_x, text_y, f'{width} x {height}', ha='center', va='center', fontsize=10, color='black')


def place_elements(formats):
    vrs = []  # List of VirtualRows
    current_y_position = 0  # Y position tracker
    current_vr = VirtualRow(X, 500, 0, 0)  # Create the first VirtualRow
    vrs.append(current_vr)

    while formats:
        width, height = formats.pop(0)
        #Może usuwaj dopiero po dodaniu elementu do vr po komendzie if placed?
        placed = False

        # Try placing the format in existing VirtualRows
        for vr in vrs:
            placed = vr.add_format(width, height)
            if isinstance(placed, VirtualRow):
                # If a new row is returned, append it to vrs
                print("New virtual row created from a gap.")
                vrs.append(placed)
                vrs.sort(key=lambda vr: vr.start_y)
                placed = True
            if placed:
                break

        # If the format wasn't placed, create a new VirtualRow
        if not placed:
            current_y_position += current_vr.Y + SAW  # Update Y position for new row
            new_vr = VirtualRow(X, height, 0, current_y_position)
            vrs.append(new_vr)
            vrs.sort(key=lambda vr: vr.start_y)
            
            for vr in vrs:
                placed = vr.add_format(width, height)
                if isinstance(placed, VirtualRow):
                    # If a new row is returned, append it to vrs
                    print("New virtual row created from a gap.")
                    vrs.append(placed)
                    vrs.sort(key=lambda vr: vr.start_y)
                    placed = True
                if placed:
                    break

    for vr in vrs:
        print(vr)
    

    return 0


generate_board(X,Y)
