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

output_dir = f"/home/sekwoja/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{id}"
optc_name = f"optc_{id}.png"
file_path = os.path.join(output_dir, optc_name)
fig, ax = plt.subplots(figsize=(12.8, 7.2))


class VirtualRow:

    def __init__(self, X, Y, x, y):
        self.X = X  # Remaining width of the row
        self.Y = Y  # Height of the row
        self.start_x = x  # Starting x position
        self.start_y = y  # Starting y position
        self.formats = []  # List of formats placed in this row
       

    def add_format(self, format_width, format_height):
        if len(self.formats) == 0:
            # Place the first format
            self.X -= format_width + SAW
            self.start_x = format_width + SAW
            self.formats.append([format_width, format_height, 0, self.start_y])
            generate_rectangle(0, self.start_y, format_width, format_height, ax)
            return True

        elif format_height <= self.Y and format_width <= self.X:
            # There is enough space in the current row
            self.X -= format_width + SAW
            generate_rectangle(self.start_x, self.start_y, format_width, format_height, ax)
            self.formats.append([format_width, format_height, self.start_x, self.start_y])
            self.start_x += format_width + SAW
            return True

        else:
            print("Not enough space in that row. Proceed to next one >>")
            
            return False

    def __str__(self):

        virtual_row_report = f"VirtualRow X: {self.X}, Y: {self.Y}, start_x: {self.start_x}, start_y: {self.start_y}, formats: {self.formats}"
        
        return virtual_row_report



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
    #print(formats)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    formats = [[1600, 500], [500, 500], [1000,500]]

    place_elements(formats)
    #print(formats)

    

    plt.savefig(file_path, format='png', dpi=150)

    


def convert_elements(project_data):

    elements = project_data["elements"]

    formats = []


    for element in elements:
        length = element['element']['dimX']
        width = element['element']['dimY']
        #thickness = element['element']['dimZ'] wyÄąâ€šĂ„â€¦czyÄąâ€šĂ„â„˘Äąâ€ş chwilowo gruboÄąâ€şĂ„â€ˇi
        quantity = element['quantity']
        starting_x = 0
        starting_y = 0

        row = [length, width]

        for _ in range(int(quantity)):
            formats.append(row)

    formats.sort(reverse=True)
    return formats

def generate_rectangle(start_position_x, start_position_y, width, height, ax):
    rect = patches.Rectangle(
        xy=(start_position_x, start_position_y),
        width=width,
        height=height,
        edgecolor='black',
        facecolor='#d3e2dc',
        antialiased=True,
        linewidth=None
    )
    ax.add_patch(rect)
    print(f"Placing rectangle in X:{start_position_x}, Y:{start_position_y} format size: X: {width} Y: {height}")


    #text_x = start_position_x + width / 2
    #text_y = start_position_y + height / 2
    #ax.text(text_x, text_y, '{width} x {height}',width,height, ha='center', va='center', fontsize=10, color='black')


def place_elements(formats):
    vrs = []  # List of all VirtualRows (including gaps)
    current_y_position = 0  # Keep track of the Y position for each new row
    current_vr = VirtualRow(3000, 500, 0, current_y_position)  # Initial row
    vrs.append(current_vr)

    while formats:
        width, height = formats.pop(0)
        placed = False

        # Try placing the format in any existing VirtualRow (including gaps)
        for vr in vrs:
            placed = vr.add_format(width, height)
            if placed:
                break  # Stop if the format fits in any existing row

        # If the format could not be placed in any existing VirtualRow
        if not placed:
            if current_vr.X > 0:
                # Save the current row's remaining space as a gap (new VirtualRow)
                new_gap_vr = VirtualRow(current_vr.X, current_vr.Y, current_vr.start_x, current_vr.start_y)
                vrs.append(new_gap_vr)

            # Move to the next row (increment the Y position by the current row height)
            current_y_position += current_vr.Y + SAW

            # Create a new VirtualRow for the next row
            new_vr = VirtualRow(3000, 500, 0, current_y_position)  # Adjust Y position for new row
            vrs.append(new_vr)
            
            # Place the format in the new VirtualRow
            for vr in vrs:
                placed = vr.add_format(width, height)
                if placed:
                    break  # Stop if the format fits in any existing row

    # Visualization: After all formats are placed
    for vr in vrs:
        print(vr)

    return vrs




generate_board(X,Y)