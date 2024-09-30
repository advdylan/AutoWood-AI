import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


X = 3000
Y = 2000
SAW = 3.2

X_IN = X / 25.4
Y_IN = Y / 25.4

id = 62

#output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{id}"
#optc_name = f"optc_{id}.png"
fig, ax = plt.subplots(figsize=(12.8, 7.2))


class VirtualRow:

    def __init__(self, X, Y, x, y):
        self.X = X  # Width of the row
        self.Y = Y  # Height of the row
        self.start_x = x  # Starting x position
        self.start_y = y  # Starting y position
        self.formats = []  # List of placed formats

    def add_format(self, format_width, format_height, vrs):
        # If first element in the row
        if len(self.formats) == 0:
            if format_width + SAW > self.X:
                print("Not enough space in row. Width left: %i, format width: %i" %(self.X,format_width))
                return False

            self.X -= format_width + SAW
            self.formats.append([format_width, format_height, self.start_x])
            print("Placing first format in row: start_%i" %(self.start_x))
            generate_rectangle(self.start_x, self.start_y, format_width, format_height, ax)
            self.start_x += format_width + SAW
            return True

        # If the format fits in both dimensions
        elif format_width <= self.X and format_height <= self.Y:

            self.X -= format_width + SAW
            self.formats.append([format_width, format_height, self.start_x])
            print("Placing format in row: start_%i" %(self.start_x))
            generate_rectangle(self.start_x, self.start_y, format_width, format_height, ax)
            self.start_x += format_width + SAW

            # If the format does not take the entire height, create a new row for the remaining height
            if format_height < self.Y:
                #sprawdz czy nie ma rzedow na tej samej wysokosc????:D
                remaining_height = self.Y - format_height
                new_row = VirtualRow(self.X - format_width - SAW, remaining_height, self.start_x - format_width - SAW , self.start_y + format_height + SAW)
                print("Creating new row for remaining height: %i" %(remaining_height))
                return new_row  # Return the new row to append to vrs in place_elements()

            return True

        # If the format doesn't fit
        else:
            print("Not enough space in this row. Proceeding to the next one.")
            return False

    def __str__(self):
        return "VirtualRow X: %f ,Y: %f, start_x: %f , start_y: %f, formats: %s" %(self.X,self.Y,self.start_x,self.start_y,self.formats)


def set_ticks(X,scale):
    ticks = []
    x = 0
    tick = x / scale
    while x <= X:
        if len(ticks) == 0:
            ticks.append(0)

        elif len(ticks) >= 1:
            ticks.append(x)

        x+=scale


    return ticks

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
    #if not os.path.exists(output_dir):
        #.makedirs(output_dir)

    formats = [[1600, 500], [500, 500], [1000,500],[200,500], [200,95],[200,95], [200,95],[450,95],[450,95],[450,95],[200,95], [200,95],[450,95],[450,95],[450,95],[200,95], [200,95],[450,95],[450,95],[450,95]]
    formats.sort(reverse=True)
    print(formats)

    place_elements(formats)
    #print(formats)



    plt.show()






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
    print("Placing rectangle in X:%i,Y:%i format size:  X:%i  Y:%i" %(start_position_x,start_position_y,width,height) )

    #text_x = start_position_x + width / 2
    #text_y = start_position_y + height / 2
    #ax.text(text_x, text_y, f'{width} x {height}', ha='center', va='center', fontsize=10, color='black')


def place_elements(formats):
    vrs = []  # List of VirtualRows
    current_y_position = 0  # Y position tracker
    current_vr = VirtualRow(X, 500, 0, 0)  # Create the first VirtualRow
    vrs.append(current_vr)

    while formats:
        width = formats[0][0]
        height = formats[0][1]
        placed = False

        # Try placing the format in existing VirtualRows
        for vr in vrs:
            placed = vr.add_format(width, height, vrs)
            if isinstance(placed, VirtualRow):
                # If a new row is returned, append it to vrs
                print("New virtual row created from a gap.")
                vrs.append(placed)
                vrs.sort(key=lambda vr: vr.start_y)
                placed = True
            if placed:
                formats.pop(0)
                break

        # If the format wasn't placed, create a new VirtualRow
        if not placed:
            current_y_position += current_vr.Y + SAW  # Update Y position for new row # ETA PROBLEMA
            print(current_y_position)
            #tworzenie nowych rzedow??
            #czyli on tworzy rzedu z X(3000)
            #moze posortowane rzedy po X, sprawdz start_x i wolne miejsca?
            #cos w tej desen musisz stworzyc
            new_vr = VirtualRow(X, height, 0, current_y_position)
            vrs.append(new_vr)
            vrs.sort(key=lambda vr: vr.start_y)

            for vr in vrs:
                placed = vr.add_format(width, height, vrs)
                if isinstance(placed, VirtualRow):
                    # If a new row is returned, append it to vrs
                    print("New virtual row created from a gap.")
                    vrs.append(placed)
                    vrs.sort(key=lambda vr: vr.start_y)
                    placed = True
                if placed:
                    formats.pop(0)
                    break

    for vr in vrs:
        print(vr)


    return 0


generate_board(X,Y)