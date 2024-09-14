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
            self.X = self.X - format_width - SAW
            self.start_x = 0 + format_width + SAW
            self.formats.append([format_width,format_height, self.start_x])
            generate_rectangle(0,0, format_width, format_height, ax)



        elif format_height <= self.Y and format_width <= self.X:
            self.X = self.X - format_width - SAW
            
            self.formats.append([format_width, format_height, self.start_x])
            generate_rectangle(self.start_x,self.start_y, format_width, format_height, ax)
            self.start_x = self.X + SAW
            return True
        return False
    
        #this needs to be implemented when there is no free space in row which is: create new vr and place item there

   
            
    
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
    x_ticks = set_ticks(X, 100)
    y_ticks = set_ticks(Y, 100)
    ax.set_xticks(x_ticks)
    ax.set_yticks(y_ticks)

    vr1 = VirtualRow(3000, 500, 0, 0)

    
    vr1.add_format(1600,500)

    
    vr1.add_format(500,500)
    

    print(vr1)

    



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

        row = [length, width, starting_x, starting_y]

        for _ in range(int(quantity)):
            formats.append(row)

    return formats


def generate_rectangle(start_position_x, start_position_y, width, height, ax):

    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height, edgecolor='black', facecolor='#d3e2dc', antialiased=True, linewidth=None)
    ax.add_patch(rect)
    print(f"Placing rectangle in X:{start_position_x},Y:{start_position_y} format size:  X: {width} Y:{height}" )

    #text_x = start_position_x + width / 2
    #text_y = start_position_y + height / 2
    #ax.text(text_x, text_y, '{width} x {height}',width,height, ha='center', va='center', fontsize=10, color='black')





generate_board(X,Y)