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

    def __init__(self, X,Y,x,y):

        self.X = X #rozmiar rzedu X
        self.Y = Y #rozmiar rzedu Y
        self.start_x = x #pozycja startujaca x
        self.start_y = y #pozycja startujaca y
        self.formats = []
        

    def add_format(self, format_width, format_height):

        if len(self.formats) == 0:
            format_start = self.start_x
            if format_width + SAW > self.X:
                print(f"Not enough space in row. Width left: {self.X}, format width: {format_width}")
                return False
            self.X = self.X - format_width - SAW
            self.start_x = format_start + format_width + SAW
            self.formats.append([format_width,format_height, self.start_x])
            generate_rectangle(0,self.start_y, format_width, format_height, ax)
            return True



        elif format_height <= self.Y and format_width <= self.X:

            format_start = self.start_x
            self.X = self.X - format_width - SAW   
            self.formats.append([format_width, format_height, self.start_x])            
            generate_rectangle(self.start_x,self.start_y, format_width, format_height, ax)
            self.start_x += format_width + SAW
            return True
        
        else:
            print("Not enough space in that raw. Proceed to next one >>")
            
            return False
    
       
    def __str__(self):
        virtual_row_report = f"VirtualRow X: {self.X} ,Y: {self.Y}, start_x: {self.start_x} , start_y: {self.start_y}, formats: {self.formats}"
        
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
    #

    formats = [[1600, 500], [500, 500], [1000,500],[200,500], [200,95],[200,95] ]
    vrs = create_vrs()
    print(vrs[0])

    #place_elements(formats)
    #print(formats)

    

    plt.savefig(file_path, format='png', dpi=150)

    
def create_vrs():
    vrs = []
    for i in range(1,4):
        vr = VirtualRow(300,50,0,0)
        vrs.append(vr)

    return vrs



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

    #text_x = start_position_x + width / 2
    #text_y = start_position_y + height / 2
    #ax.text(text_x, text_y, '{width} x {height}',width,height, ha='center', va='center', fontsize=10, color='black')


def place_elements(formats):
    print(formats)

    vrs = []  # List of all VirtualRows (including gaps)
    current_y_position = 0  # Keep track of the Y position for each new row
    current_vr = VirtualRow(X, 500, 0, 0)  # Initial row
    vrs.append(current_vr)

    while formats:
        width, height = formats.pop(0)
        placed = False

        # Try placing the format in existing virtual rows
        for vr in vrs:
            print(f"Trying to place format at row {vr}, available width: {vr.X}, available height: {vr.Y}")
            placed = vr.add_format(width, height)
            if placed:
                print("Placed->break")
                break

        # If the format wasn't placed, create a new row
        if not placed:
            # Create a gap row based on the current virtual row
            new_gap_vr = VirtualRow(current_vr.X, current_vr.Y, current_vr.start_x, current_vr.start_y)
            vrs.append(new_gap_vr)
            
            # Update Y position for the new row
            current_y_position += current_vr.Y + SAW
            print(f"Current Y position: {current_y_position}")

            # Create a new virtual row with full width and the required height
            new_vr = VirtualRow(X, height, 0, current_y_position)
            print(f"New Virtual Row: {new_vr}")
            vrs.append(new_vr)

            # Try placing the format in the new row
            print(f"Trying to place format at row {vr}, available width: {vr.X}, available height: {vr.Y}")
            placed = new_vr.add_format(width, height)
            print(f"first try : {new_vr}")

            if placed:
                print("Format placed in new row")
                
            else:
                print("Failed to place format in new row")

    for vr in vrs:
        print(vr)
    

    return 0


generate_board(X,Y)