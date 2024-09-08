import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from product.pdf_generator_scripts.pdf_generator import get_data
from or_tools_optimizer import pack_pieces_on_board
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from ortools.linear_solver import pywraplp
import numpy as np


X = 8000
Y = 2000
SAW = 3.2

id = 60

output_dir = f"/home/dylan/AutoWood/AutoWood_Backend/product/cut_optimizer/optimized_cuts/{id}"
optc_name = f"optc_{id}.png"
file_path = os.path.join(output_dir, optc_name)

def generate_board(output_dir, optc_name,X,Y):

    file_path = os.path.join(output_dir, optc_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)


    project_data = get_data(id)
    formats = convert_elements(project_data)

    fig, ax = plt.subplots()
    ax.set_xlim(0, X)
    ax.set_ylim(0, Y)
    

    i = 0
    j = 0
    start_position_x = 0
    start_position_y = 0
    
    #print(formats)
    pack_pieces_on_board(pieces=formats, board_length=X, board_width=Y, saw_thickness=SAW)
    

    for format in formats:
        #print(f"X: {format[i]}, Y: {format[i+1]}")

        generate_rectangle(start_position_x, start_position_y,format[i], format[i+1], ax)
       
    plt.savefig(file_path, format='png')


def convert_elements(project_data):

    elements = project_data["elements"]

    formats = []

    for element in elements:
        length = element['element']['dimX']
        width = element['element']['dimY']
        #thickness = element['element']['dimZ'] wyłączyłęś chwilowo grubośći
        quantity = element['quantity']

        row = [length,width]

        for _ in range(int(quantity)):
            formats.append(row)

    return formats

   
def generate_rectangle(start_position_x, start_position_y, width, height, ax):
  
    rect = patches.Rectangle(xy=(start_position_x,start_position_y), width=width, height=height, edgecolor='#bed4d4', facecolor='#d3e2dc', antialiased=True, linewidth=None)
    ax.add_patch(rect)


def calculate_rows(formats):
    i=0
    j=0
    lengths = []
    heigths = []
    free_x = 0
    free_y = 0
    for format in formats:
        #print(f"Format numer {j}")       
        #print(f"X: {format[i]}, Y: {format[i+1]}")
        lengths.append(format[i])
        heigths.append(format[i+1])
        j+=1

    lengths.sort()
    heigths.sort()
    




        

    
generate_board(output_dir, optc_name, X, Y)




    