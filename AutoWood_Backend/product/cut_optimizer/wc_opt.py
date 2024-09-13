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


class VirtualRow:
    def __init__(self, X,Y,x,y):
        self.X = X #rozmiar rzedu X
        self.Y = Y #rozmiar rzedu Y
        self.start_x = x #pozycja startujaca x
        self.start_y = y #pozycja startujaca y
        self.formats = []



    def add_format(self, format_width, format_height):

        if format_height <= self.Y and format_width <= self.X:
            self.X = self.X - format_width - SAW
            self.start_x = self.X + SAW
            self.formats.append([format_width, format_height, self.start_x])
            return True
        return False
        #tu bedzie logika jak nie wejdzie

    
    def f(self):
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



    fig, ax = plt.subplots(figsize=(12.8, 7.2))
    formats = [
    [1600,250,0,0],



    ]



    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title("Rozkroje")
    x_ticks = set_ticks(X, 130)
    y_ticks = set_ticks(Y, 100)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    i = 0
    j = 0
    start_position_x = 0
    start_position_y = 0

    define_starting_position(formats, ax)

    plt.show()


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

        row = [length, width, starting_x, starting_y]

        for _ in range(int(quantity)):
            formats.append(row)

    return formats


def generate_rectangle(start_position_x, start_position_y, width, height, ax):

    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height, edgecolor='black', facecolor='#d3e2dc', antialiased=True, linewidth=None)
    ax.add_patch(rect)

    #text_x = start_position_x + width / 2
    #text_y = start_position_y + height / 2
    #ax.text(text_x, text_y, '{width} x {height}',width,height, ha='center', va='center', fontsize=10, color='black')


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
        print("X: {format[i]}, Y: {format[i+1]}", format[i], format[i+1])
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
        #print("Wchodzi idelnie mÄ‚Ĺ‚j Panie")
        return capacity_left, True
    else:
        #print("Masz za duÄąÄ˝ego Panie")
        return capacity_left,False





def define_starting_position(formats, ax):
    board = (X, Y)  # Board dimensions
    """
    virtual_row[0] = "size_x"
    virtual_row[1] = "size_y"
    virtual_row[2] = "remaining_space_x"
    virtual_row[3] = "remaining_space_y"

    """
      # List to hold all virtual rows
    i=0


    start_position_y = 0  # Starting Y position for the first row

    print(formats)

    while formats:
        format = formats.pop(0)
        format_width = format[0]
        format_height = format[1]
        virtual_rows = [[X,format[1],0,0]]

        # Try to place the piece in an existing row
        placed = False
        """
        for row in virtual_rows:
            remaining_width, row_height, row_start_y = row
            print(row)
            if width <= remaining_width:
                start_position_x = X - remaining_width
                print("start position x: %s",start_position_x)
                """


        if not placed:
            if start_position_y + format_width <= Y:  # Check if we still have vertical space
                row = [X, format_height]


                print("ROW: %s" %row)
                print("VR: %s" %virtual_rows)

                # Generate the rectangle at the new position
                generate_rectangle(virtual_rows[i][3], start_position_y, format_width, format_height, ax)






        # Re-check earlier rows for remaining space after placing in a new row
        """
        for row in virtual_rows:
            remaining_width, row_height, row_start_y = row
            if remaining_width > 0:
                print("Remaining space in row starting at Y={row_start_y}: {remaining_width} mm", row_start_y, remaining_width)


        """





#generate_board(X, Y)
vr1 = VirtualRow(3000, 500, 0, 0)
print(vr1.add_format(1600,500))
print(vr1.f())
print(vr1.add_format(300,500))
print(vr1.f())



